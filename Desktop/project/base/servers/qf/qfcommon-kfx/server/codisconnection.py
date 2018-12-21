from __future__ import with_statement
import random
import time
import etcd
import json

from redis.connection import *

import redis

from redis._compat import (b, xrange, imap, byte_to_chr, unicode, bytes, long,
                           BytesIO, nativestr, basestring, iteritems,
                           LifoQueue, Empty, Full, urlparse, parse_qs,
                           recv, recv_into, select, unquote)

from redis.exceptions import (
    RedisError,
    ConnectionError,
    TimeoutError,
    BusyLoadingError,
    ResponseError,
    InvalidResponse,
    AuthenticationError,
    NoScriptError,
    ExecAbortError,
    ReadOnlyError
)


class ReadWriteLock(object):
    def __init__(self):
        self.r_lock = threading.Lock()
        self.w_lock = threading.Lock()
        self.readers = 0

    def acquire_read(self):
        with self.r_lock:
            self.readers += 1
            if self.readers == 1:
                self.w_lock.acquire()

    def release_read(self):
        with self.r_lock:
            self.readers -= 1
            if self.readers == 0:
                self.w_lock.release()

    def acquire_write(self):
        self.w_lock.acquire()

    def release_write(self):
        self.w_lock.release()


class CodisProxy(object):
    def __init__(self, codis_proxy_list=None, codis_proxy_etcd_dir=None, etcd_list=None):
        self.codis_proxy_list = []
        self.codis_proxy_disabled_list = []
        self.client = None
        if isinstance(codis_proxy_etcd_dir, str):
            if etcd_list is None:
                raise Exception

            self.client = etcd.Client(host=etcd_list, allow_reconnect=True)
            try:
                directory = self.client.read(codis_proxy_etcd_dir, recursive=True)

                for result in directory.children:
                    info = json.loads(result.value)
                    print(info)
                    addr = info['addr']
                    index = addr.find(':')
                    host = addr[:index]
                    port = addr[index + 1:]

                    token = info['token']

                    endpoint = {'host': host, 'port': int(port), 'token': token}
                    self.codis_proxy_list.append(endpoint)
            except etcd.EtcdKeyNotFound:
                pass
        else:
            self.codis_proxy_list = codis_proxy_list

        self.is_usable_flag = True
        self.rw_lock = ReadWriteLock()
        self.check_thread = None
        self.is_run_thread = False
        self.db = None

    def set_db(self, db=0):
        self.db = db

    def is_usable(self):
        self.rw_lock.acquire_read()
        if 0 == len(self.codis_proxy_list):
            self.is_usable_flag = False
        else:
            self.is_usable_flag = True
        self.rw_lock.release_read()
        return self.is_usable_flag

    def selector(self):
        self.rw_lock.acquire_read()
        selector_index = random.randint(0, len(self.codis_proxy_list)-1)
        endpoint = self.codis_proxy_list[selector_index]
        self.rw_lock.release_read()
        return endpoint

    def disable_endpoint(self, endpoint):
        self.rw_lock.acquire_write()
        for node in self.codis_proxy_list:
            if node['token'] == endpoint['token']:
                self.codis_proxy_disabled_list.append(node)
                self.codis_proxy_list.remove(node)
                if self.is_run_thread is False:
                    #print('start check thread...')
                    self.is_run_thread = True
                    self.check_thread = threading.Thread(target=CodisProxy.endpoint_usable_check, args=(self,))
                    self.check_thread.start()

        self.rw_lock.release_write()

    def endpoint_usable_check(self):
        while len(self.codis_proxy_disabled_list):
            print(self.codis_proxy_disabled_list)
            time.sleep(5)
            for endpoint in self.codis_proxy_disabled_list:
                conn = Connection(host=endpoint['host'], port=endpoint['port'], db=self.db)
                try:
                    conn.connect()
                    self.rw_lock.acquire_write()
                    for node in self.codis_proxy_disabled_list:
                        if node['token'] == endpoint['token']:
                            self.codis_proxy_list.append(node)
                            self.codis_proxy_disabled_list.remove(node)
                    self.rw_lock.release_write()
                except:
                    pass

        self.is_run_thread = False
        #print('end check thread...')


class QFPayCodisConnection(object):
    "Manages TCP communication to and from a Redis server"
    description_format = "connection_class=QFPayCodisConnection"

    def __init__(self, codis_proxy=None, db=0, password=None,
                 socket_timeout=None, socket_connect_timeout=None,
                 socket_keepalive=False, socket_keepalive_options=None,
                 retry_on_timeout=False, encoding='utf-8',
                 encoding_errors='strict', decode_responses=False,
                 parser_class=DefaultParser, socket_read_size=65536):
        self.pid = os.getpid()
        if not isinstance(codis_proxy, CodisProxy):
            raise Exception
        self.codis_proxy = codis_proxy
        self.codis_proxy_disabled_list = []
        self.db = db
        self.codis_proxy.set_db(self.db)
        self.endpoint = None
        self.password = password
        self.socket_timeout = socket_timeout
        self.socket_connect_timeout = socket_connect_timeout or socket_timeout
        self.socket_keepalive = socket_keepalive
        self.socket_keepalive_options = socket_keepalive_options or {}
        self.retry_on_timeout = retry_on_timeout
        self.encoder = Encoder(encoding, encoding_errors, decode_responses)
        self._sock = None
        self._parser = parser_class(socket_read_size=socket_read_size)
        self._connect_callbacks = []

    def __repr__(self):
        return self.description_format

    def __del__(self):
        try:
            self.disconnect()
        except Exception:
            pass

    def register_connect_callback(self, callback):
        self._connect_callbacks.append(callback)

    def clear_connect_callbacks(self):
        self._connect_callbacks = []

    def connect(self):
        "Connects to the Redis server if not already connected"
        if self._sock:
            return
        try:
            if self.codis_proxy is not None:
                self.endpoint = self.codis_proxy.selector()
            sock = self._connect()
        except socket.timeout:
            raise TimeoutError("Timeout connecting to server")
        except socket.error:
            e = sys.exc_info()[1]
            raise ConnectionError(self._error_message(e))

        self._sock = sock
        try:
            self.on_connect()
        except RedisError:
            # clean up after any error in on_connect
            self.disconnect()
            raise

        # run any user callbacks. right now the only internal callback
        # is for pubsub channel/pattern resubscription
        for callback in self._connect_callbacks:
            callback(self)

    def _connect(self):
        "Create a TCP socket connection"
        # we want to mimic what socket.create_connection does to support
        # ipv4/ipv6, but we want to set options prior to calling
        # socket.connect()
        err = None

        for res in socket.getaddrinfo(self.endpoint['host'], self.endpoint['port'], 0,
                                      socket.SOCK_STREAM):
            family, socktype, proto, canonname, socket_address = res
            sock = None
            try:
                sock = socket.socket(family, socktype, proto)
                # TCP_NODELAY
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

                # TCP_KEEPALIVE
                if self.socket_keepalive:
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    for k, v in iteritems(self.socket_keepalive_options):
                        sock.setsockopt(socket.SOL_TCP, k, v)

                # set the socket_connect_timeout before we connect
                sock.settimeout(self.socket_connect_timeout)

                # connect
                sock.connect(socket_address)

                # set the socket_timeout now that we're connected
                sock.settimeout(self.socket_timeout)
                return sock

            except socket.error as _:
                err = _
                if sock is not None:
                    sock.close()

        if err is not None:
            raise err
        raise socket.error("socket.getaddrinfo returned an empty list")

    def _error_message(self, exception):
        # args for socket.error can either be (errno, "message")
        # or just "message"
        if len(exception.args) == 1:
            return "Error connecting to %s:%s. %s." % \
                (self.endpoint['host'], self.endpoint['port'], exception.args[0])
        else:
            return "Error %s connecting to %s:%s. %s." % \
                (exception.args[0], self.endpoint['host'], self.endpoint['port'], exception.args[1])

    def on_connect(self):
        "Initialize the connection, authenticate and select a database"
        self._parser.on_connect(self)

        # if a password is specified, authenticate
        if self.password:
            self.send_command('AUTH', self.password)
            if nativestr(self.read_response()) != 'OK':
                raise AuthenticationError('Invalid Password')

        # if a database is specified, switch to it
        if self.db:
            self.send_command('SELECT', self.db)
            if nativestr(self.read_response()) != 'OK':
                raise ConnectionError('Invalid Database')

    def disconnect(self):
        "Disconnects from the Redis server"
        self._parser.on_disconnect()
        if self._sock is None:
            return
        try:
            self._sock.shutdown(socket.SHUT_RDWR)
            self._sock.close()
        except socket.error:
            pass
        self._sock = None

    def send_packed_command(self, command):
        "Send an already packed command to the Redis server"
        if not self._sock:
            while True:
                try:
                    self.connect()
                    break
                except ConnectionError:
                    self.disconnect()
                    self.codis_proxy.disable_endpoint(self.endpoint)
                    if not self.codis_proxy.is_usable:
                        raise

        try:
            if isinstance(command, str):
                command = [command]
            for item in command:
                self._sock.sendall(item)
        except socket.timeout:
            self.disconnect()
            raise TimeoutError("Timeout writing to socket")
        except socket.error:
            e = sys.exc_info()[1]
            self.disconnect()
            if len(e.args) == 1:
                errno, errmsg = 'UNKNOWN', e.args[0]
            else:
                errno = e.args[0]
                errmsg = e.args[1]
            raise ConnectionError("Error %s while writing to socket. %s." %
                                  (errno, errmsg))
        except:
            self.disconnect()
            raise

    def send_command(self, *args):
        "Pack and send a command to the Redis server"
        self.send_packed_command(self.pack_command(*args))

    def can_read(self, timeout=0):
        "Poll the socket to see if there's data that can be read."
        sock = self._sock
        if not sock:
            self.connect()
            sock = self._sock
        return self._parser.can_read() or \
            bool(select([sock], [], [], timeout)[0])

    def read_response(self):
        "Read the response from a previously sent command"
        try:
            response = self._parser.read_response()
        except:
            self.disconnect()
            raise
        if isinstance(response, ResponseError):
            raise response
        return response

    def pack_command(self, *args):
        "Pack a series of arguments into the Redis protocol"
        output = []
        # the client might have included 1 or more literal arguments in
        # the command name, e.g., 'CONFIG GET'. The Redis server expects these
        # arguments to be sent separately, so split the first argument
        # manually. All of these arguements get wrapped in the Token class
        # to prevent them from being encoded.
        command = args[0]
        if ' ' in command:
            args = tuple([Token.get_token(s)
                          for s in command.split()]) + args[1:]
        else:
            args = (Token.get_token(command),) + args[1:]

        buff = SYM_EMPTY.join(
            (SYM_STAR, b(str(len(args))), SYM_CRLF))

        for arg in imap(self.encoder.encode, args):
            # to avoid large string mallocs, chunk the command into the
            # output list if we're sending large values
            if len(buff) > 6000 or len(arg) > 6000:
                buff = SYM_EMPTY.join(
                    (buff, SYM_DOLLAR, b(str(len(arg))), SYM_CRLF))
                output.append(buff)
                output.append(arg)
                buff = SYM_CRLF
            else:
                buff = SYM_EMPTY.join((buff, SYM_DOLLAR, b(str(len(arg))),
                                       SYM_CRLF, arg, SYM_CRLF))
        output.append(buff)
        return output

    def pack_commands(self, commands):
        "Pack multiple commands into the Redis protocol"
        output = []
        pieces = []
        buffer_length = 0

        for cmd in commands:
            for chunk in self.pack_command(*cmd):
                pieces.append(chunk)
                buffer_length += len(chunk)

            if buffer_length > 6000:
                output.append(SYM_EMPTY.join(pieces))
                buffer_length = 0
                pieces = []

        if pieces:
            output.append(SYM_EMPTY.join(pieces))
        return output


if __name__ == '__main__':
    host_list = [{'host': '172.100.101.150', 'port': 19000, 'token': '1111'},
                 {'host': '172.100.101.151', 'port': 19000, 'token': '2222'},
                 {'host': '172.100.101.152', 'port': 19000, 'token': '3333'}]

    # codis_proxy = CodisProxy(codis_proxy_etcd_dir='/jodis/codis-test-01/',
    #                             etcd_list=(('172.100.101.131', 2379), ('172.100.101.132', 2379)))

    codis_proxy = CodisProxy(codis_proxy_list=host_list)

    pool = redis.ConnectionPool(connection_class=QFPayCodisConnection,
                                codis_proxy=codis_proxy,
                                password='qfpay',
                                db=0)

    r = redis.Redis(connection_pool=pool)

    r.set('key', 'hello ')

    print(r.get('key'))
