# coding: utf-8
import os, sys
import re, time, types, mimetypes
from qfcommon.web import template, reloader
from qfcommon.base import dbpool
from qfcommon.base.tools import smart_utf8
from qfcommon.web.http import Request, Response, NotFound
import traceback, logging
from http import MethodNotAllowed

log = logging.getLogger()

# 读取500 页面
error_page_content = 'some error'
error_page_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','500.html')
if os.path.exists(error_page_path):
    with open(error_page_path) as f:
        error_page_content = f.read()

class HandlerFinish(Exception):
    pass

class Handler(object):
    def __init__(self, app, req):
        self.webapp = app
        self.req = req
        #self.ses = session.Session(app.settings.SESSION, req.cookie)
        self.ses = {}
        self.resp = Response()
        self.write = self.resp.write
        req.allowed_methods = []

    def initial(self):
        pass

    def finish(self):
        #self.ses.end()
        pass

    def get_cookie(self, cookie_name):
        return self.req.cookie.get(cookie_name, '')

    def set_cookie(self, *args, **kwargs):
        self.resp.set_cookie(*args, **kwargs)

    def set_headers(self, headers={}):
        if headers:
            for k,v in headers.iteritems():
                self.resp.headers[k] = smart_utf8(v)

    def redirect(self, *args, **kwargs):
        return self.resp.redirect(*args, **kwargs)

    def GET(self):
        self.resp = MethodNotAllowed()

    POST = HEAD = DELETE = PUT = GET

    def OPTIONS(self):
        '''
            OPTIONS请求方法的主要用途有两个：
            1、获取服务器支持的HTTP请求方法；也是黑客经常使用的方法。
            2、用来检查服务器的性能。例如：
                AJAX进行跨域请求时的预检，需要向另外一个域名的资源发送一个HTTP OPTIONS请求头，用以判断实际发送的请求是否安全。
        '''
        origin = self.req.environ.get('HTTP_ORIGIN','')
        self.resp.headers['Access-Control-Allow-Origin'] = origin
        self.resp.headers['Access-Control-Allow-Credentials'] = 'true'
        self.resp.headers['Access-Control-Allow-Methods'] = ','.join(self.allowed_methods)
        # request headers
        req_headers = self.req.environ.get('HTTP_ACCESS_CONTROL_REQUEST_HEADERS', '')
        self.resp.headers['Access-Control-Allow-Headers'] = req_headers
        self.resp.headers['Access-Control-Max-Age'] = '86400'  # ,允许这个预请求的参数缓存的秒数,在此期间,不用发出另一条预检请求
        self.resp.status=200
        return

    def render(self, *args, **kwargs):
        if template.render:
            kwargs.update({
                '_handler':self
            })
            self.write(template.render(*args, **kwargs))


class WebApplication(object):
    def __init__(self, settings):
        '''
        settings:
            DOCUMENT_ROOT: web root path
            DEBUG: True/False
            CHARSET: utf-8
            LOGGER: log file
            HOME: project home path
            TEMPLATE: {'path':xx,'tmp':xx,'cache':True}
            DATABASE: database config
            APPS: app
            URLS: (('/', index.Index), )
            STATICS
            SESSION
            MIDDLEWARE
        '''
        # 切换到字典static,兼容列表型
        if isinstance(settings.STATICS, list) or isinstance(settings.STATICS, tuple):
            settings.STATICS = dict(zip(settings.STATICS,settings.STATICS))

        self.allowed_methods = set(('GET', 'HEAD', 'POST', 'DELETE', 'PUT', 'OPTIONS'))
        self.charset = 'utf-8'

        self.settings = settings
        self.debug = settings.DEBUG
        self.reloader = None
        if self.debug:
            self.reloader = reloader.Reloader()
            self.reloader()
        self.install()

        if not self.settings.DOCUMENT_ROOT:
            self.document_root = os.getcwd()
        else:
            self.document_root = self.settings.DOCUMENT_ROOT

        self.charset = settings.CHARSET



    def add_urls(self, urls, appname=''):
        tmpurls = []
        for item in urls:
            if len(item) == 2:
                if type(item[1]) == types.StringType:
                    mod, cls = item[1].rsplit('.', 1)
                    mod = __import__(mod, None, None, [''])
                    #仅仅针对于调试用, 热更新
                    if self.reloader:
                        reload(mod)
                    obj = getattr(mod, cls)
                else:
                    obj = item[1]

                if appname:
                    tmpurls.append((re.compile('/'+appname+item[0]), obj, {}))
                else:
                    tmpurls.append((re.compile(item[0]), obj, {}))
            else:
                if appname:
                    tmpurls.append((re.compile('/'+appname+item[0]), obj, item[2]))
                else:
                    tmpurls.append((re.compile(item[0]), obj, item[2]))
        #self.urls = tmpurls + self.urls
        self.urls += tmpurls

    def install(self):
        if self.settings.HOME not in sys.path:
            sys.path.insert(0, self.settings.HOME)

        tplcf = self.settings.TEMPLATE
        if tplcf['tmp'] and not os.path.isdir(tplcf['tmp']):
            os.mkdir(tplcf['tmp'])
        if tplcf['path']:
            template.install(tplcf['path'], tplcf['tmp'], tplcf['cache'],
                             self.settings.CHARSET)

        if self.settings.DATABASE:
            dbpool.install(self.settings.DATABASE)

        self.urls = []
        for appname in self.settings.APPS:
            self.add_app(appname)
        self.add_urls(self.settings.URLS)

    def run(self, host='0.0.0.0', port=8000):
        from gevent.wsgi import WSGIServer

        server = WSGIServer((host, port), self)
        server.backlog = 512
        try:
            log.info("Server running on %s:%d" % (host, port))
            server.serve_forever()
        except KeyboardInterrupt:
            server.stop()


    def add_app(self, appname):
        log.debug('add app:%s', appname)
        m = __import__(appname)
        self.add_urls(m.URLS, appname)

    def __call__(self, environ, start_response):
        times = [time.time()]
        req  = None
        resp = None
        viewobj = None
        try:
            if self.reloader:
                if self.reloader():
                    self.install()
            req = Request(environ)
            times.append(time.time())
            if req.path.startswith(tuple(self.settings.STATICS.keys())):
                fpath = self.document_root +  req.path
                resp = NotFound('Not Found: ' + fpath)
                for k,v in self.settings.STATICS.iteritems():
                    if req.path.startswith(k):
                        fpath = fpath.replace(k,v)
                        if os.path.isfile(fpath):
                            resp = self.static_file(req, fpath)
            else:
                for regex, view, kwargs in self.urls:
                    match = regex.match(req.path)
                    if match is not None:
                        if req.method not in self.allowed_methods:
                            raise NotImplemented
                        args    = ()
                        mkwargs = match.groupdict()
                        if mkwargs:
                            kwargs.update(mkwargs)
                        else:
                            args = match.groups()

                        times.append(time.time())

                        viewobj = view(self, req)

                        middleware = []
                        try:
                            viewobj.initial()
                            viewobj.allowed_methods = self.allowed_methods

                            for x in self.settings.MIDDLEWARE:
                                obj = x()
                                resp = obj.before(viewobj, *args, **kwargs)
                                if resp:
                                    log.debug('middleware return:%s', resp)
                                    break
                                middleware.append(obj)

                            ret = getattr(viewobj, req.method)(*args, **kwargs)
                            if ret:
                                viewobj.resp.write(ret)
                            viewobj.finish()

                        except HandlerFinish:
                            pass

                        resp = viewobj.resp

                        for obj in middleware:
                            resp = obj.after(viewobj)
                        break
                else:
                    resp = NotFound('Not Found')
        except Exception, e:
            times.append(time.time())
            log.warn('web call error: %s', traceback.format_exc())
            if self.debug:
                resp = Response('<pre>%s</pre>' % traceback.format_exc(), 500)
            else:
                global error_page_content
                resp = Response(error_page_content, 500)

        times.append(time.time())
        #s = '%s %s %s ' % (req.method, req.path, str(viewobj.__class__)[8:-2])
        s = [str(resp.status), req.method, req.path]
        s.append('%d' % ((times[-1]-times[0])*1000000))
        s.append('%d' % ((times[1]-times[0])*1000000))
        s.append('%d' % ((times[-1]-times[-2])*1000000))
        try:
            if req.query_string:
                s.append(req.query_string[:2048])
            if req.method == 'POST':
                s.append(str(req.input())[:2048])
            if not req.input() and req.data:
                s.append(str(req.data)[:2048])
            # if resp.content and resp.headers['Content-Type'].startswith('application/json'):
            if resp.content and resp.content.startswith('{') and resp.content.endswith('}'):
                s.append(str(resp.content)[:4096])
        except:
            log.warn(traceback.format_exc())
        if not req.path.startswith(tuple(self.settings.STATICS.keys())):
            log.info('|'.join(s))

        return resp(environ, start_response)

    def static_file(self, req, fpath):
        mtype, encoding = mimetypes.guess_type(fpath)
        if not mtype:
            mtype = 'application/octet-stream'

        try:
            reqtm = 0
            reqgmt = req.environ.get('HTTP_IF_MODIFIED_SINCE')
            if reqgmt:
                reqgmt = reqgmt[:reqgmt.find('GMT') + 3]
                reqtm  = time.strptime(reqgmt, '%a, %d %b %Y %H:%M:%S GMT')
                if type(reqtm) != types.FloatType:
                    reqtm = time.mktime(reqtm) + (time.mktime(time.localtime()) - time.mktime(time.gmtime()))
        except:
            log.warn(traceback.format_exc())
            reqtm  = 0

        mtime = os.path.getmtime(fpath)
        gmt   = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(mtime))
        if mtime > reqtm or mtype == 'application/octet-stream':
            with open(fpath, 'rb') as f:
                s = f.read()
            resp = Response(s, mimetype=mtype)
        else:
            resp = Response('', status=304, mimetype=mtype)
        resp.headers['Last-Modified'] = gmt

        return resp




