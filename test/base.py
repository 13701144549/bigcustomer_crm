# coding:utf-8

import time
import json
import redis

from hashids import Hashids
from requests import post, get
from functools import wraps

from huepy import red, info, lightpurple, purple

redis_pool = redis.Redis('172.100.101.156')
hids = Hashids('qfpay')

env = 'debug'
# env = 'product'
# env = 'qa'
SKEY = 'test_org_sid'
CUSTOMER_ID = 24

if env == 'product':
    HOST = 'https://o.qa.qfpay.net'

    USERNAME = 14400001234 # 12
    PASSWORD = '001234'

elif env == 'qa':
    HOST = 'https://o.qa.qfpay.net'

    USERNAME = 14700000291
    PASSWORD = '000291'
else:
    HOST = 'http://127.0.0.1:6500'

    # USERNAME = 14000000007 # 20
    # USERNAME = 17000000000# 12

    # USERNAME = 'funailhk' # ID 21012662
    # PASSWORD = 'funailhk'

    USERNAME = 'shasha'
    PASSWORD = 'shasha'

    # USERNAME = 'korg5'  # ID 21011596
    # PASSWORD = '1111'
    # PASSWORD = 'qfpay123456'

    #USERNAME = 14000000000 # 13
    #PASSWORD = 'qfpay123456'

    # USERNAME = 'korg_4_1'
    # PASSWORD = '1111'

    #USERNAME = '12#0006'
    #PASSWORD = '12133X'


unicode_to_utf8 = lambda v: v.encode('utf-8') if isinstance(v, unicode) else str(v)
decode_from_utf8 = lambda v: v if isinstance(v, unicode) else v.decode('utf-8')


def del_func(func):
    @wraps(func)
    def _(self, *arg, **kw):
        timeit = kw.pop('timeit', False)
        if not timeit:
            ret = func(self, *arg, **kw)
            if hasattr(ret, 'text'):
                try:
                    data = json.loads(ret.text)
                except:
                    data = ret.text
            else:
                data = ret

            if data:
                print info(purple('执行结果:'))

                print red(
                    unicode_to_utf8(json.dumps(
                        data, indent = 2, ensure_ascii = False
                    ))
                )
        else:
            st = time.time()
            for i in xrange(10000):
                func()
            print time.time() - st
    return _

class Log(type):

    def __new__(cls, cls_nm, cls_parents, cls_attrs):
        for attr_nm in cls_attrs:
            if (not attr_nm.startswith('_')  and callable(cls_attrs[attr_nm])
                and attr_nm not in ('print_env', )):
                cls_attrs[attr_nm] = del_func(cls_attrs[attr_nm])
        return super(Log, cls).__new__(cls, cls_nm, cls_parents, cls_attrs)

class Base(object):

    __metaclass__ = Log

    def print_env(self):
        self.username = redis_pool.get(SKEY+'_username') or USERNAME
        self.password = redis_pool.get(SKEY+'_pwd') or PASSWORD
        self.host = redis_pool.get(SKEY+'_host') or HOST
        print info(purple('环境:'))
        print info(lightpurple(('username: %s' % self.username)))
        print info(lightpurple('password: %s' % self.password))
        print info(lightpurple('host:     %s' % self.host))
        print ''

    def __init__(self):
        self.print_env()
        self.hids = Hashids('qfpay')

    def _change_env(self, **kw):
        '''修改环境变量'''

        fields = ['username', 'password', 'class', 'host']
        for field in fields:
            if field in kw:
                redis_pool.set(SKEY+'_'+field, kw[field])
        self.del_sid()
        self.print_env()

    def _clear_env(self):
        fields = ['username', 'password', 'class', 'host']
        for field in fields:
            redis_pool.delete(SKEY+'_'+field)
        self.del_sid()
        self.print_env()

    def del_sid(self):
        redis_pool.delete(SKEY)

    def _login(self):
        data = {
            'username' : self.username,
            'password' : self.password,
        }
        return post('http://127.0.0.1:6500/org/user/login',
                data=data)

    def _get_sid(self):
        try:
            sid = redis_pool.get(SKEY)
            if not sid:
                ret = self._login()
                sid = json.loads(ret.text)['data']['sessionid']
            return sid
        finally:
            if sid:
                try:
                    redis_pool.setex(SKEY, sid, 2 * 24 * 3600)
                except:
                    pass

    def request(self, method, **kw):
        cookies = {}
        if kw.get('with_sid', True):
            cookies['sessionid'] = self._get_sid()

        if kw.get('with_csid'):
            cookies['csid'] = self._get_csid()


        cookies.update(getattr(self, '_cookies', {}))

        if method == 'get':
            func = get
        else:
            func = post

        headers = getattr(self, '_headers', {})

        return func(
            self.host + self._url,
            getattr(self, '_data', {}),
            cookies = cookies,
            headers = headers
        )

    def post(self, **kw):
        self.request('post', **kw)

    def get(self, **kw):
        self.request('get', **kw)
