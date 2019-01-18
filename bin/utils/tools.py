# coding:utf-8

import json
import datetime
import types
import xlwt
import csv
import codecs
import config
import decimal
import urlparse
import traceback
from StringIO import StringIO
import logging
from contextlib import contextmanager
from openpyxl import Workbook
from utils.runtime import qfcache, redis_pool
from utils.excepts import ParamError
from utils.constants import PRIMARY_MCC

from qfcommon.base.dbpool import get_connection_exception
from qfcommon.server.selector import Selector
from qfcommon.base.http_client import RequestsClient
from qfcommon.base.date_tools import getyearandmonth
from qfcommon.base.tools import thrift_callex
from qfcommon.thriftclient.finance import Finance, ttypes as finance_ttypes
from qfcommon.server.client import ThriftClient, HttpClient
from qfcommon.thriftclient.spring import Spring
from qfcommon.thriftclient.org import OrgServer, ttypes
from qfcommon.thriftclient.payadmin import PayAdmin, ttypes as payadmin_ttypes

from utils.valid import is_valid_int

log = logging.getLogger()

decode_from_utf8 = lambda v: v if isinstance(v, unicode) else v.decode('utf-8')

unicode_to_utf8 = lambda v: v.encode('utf-8') if isinstance(v, unicode) else str(v)

merchant_server = Selector(config.MERCHANT_SERVER, 'round_robin')


def create_xls(sio, data):
    table = xlwt.Workbook()
    sheet = table.add_sheet('Sheet1')
    for row, rows in enumerate(data):
        for col, item in enumerate(rows):
            if isinstance(item, (types.StringType)):
                item = decode_from_utf8(item)
            sheet.write(row, col, item)
    table.save(sio)


def create_xlsx(sio, data):
    wb = Workbook()
    ws = wb.active
    for i in data:
        ws.append(i)
    wb.save(sio)


def getid():
    '''通过spring生成id'''
    return ThriftClient(config.SPRING_SERVERS, Spring).getid()


def get_page_params(params):
    '''
    请求时获取页码相关参数
    :param params: 请求参数
    :return: 返回一个元组，（page，page_size）
    '''
    if params.get('page'):
        page = int(params['page'])
    else:
        page = 0
    if params.get('page_size'):
        page_size = int(params['page_size'])
    else:
        page_size = config.PAGE_SIZE
    return page, page_size


def thrift_callex_framed(server_config, mod, func, *args, **kwargs):
    client = ThriftClient(server_config, mod, framed=True)
    client.raise_except = True
    return client.call(func, *args, **kwargs)


def call_org(func, *args, **kwargs):
    log.debug('req org_api: %s %s %s', func, args, kwargs)
    try:
        ret = thrift_callex_framed(config.ORG_API_SERVER, OrgServer, func, *args, **kwargs)
        log.debug('org_api ret: %s', ret)
        return ret
    except ttypes.QudaoException as e:
        log.warn('org_api error: %s', str(e))
        raise


def call_payadmin(func, *args, **kwargs):
    log.debug('req payadmin: %s %s %s', func, args, kwargs)
    try:
        ret = thrift_callex_framed(config.PAYADMIN_SERVER, PayAdmin, func, *args, **kwargs)
        log.debug('payadmin ret: %s', ret)
        return ret
    except payadmin_ttypes.ServerError as e:
        log.warn('payadmin error: %s', str(e))
        raise


@contextmanager
def high_prec(prec):
    old_prec = decimal.getcontext().prec
    decimal.getcontext().prec = prec
    try:
        yield
    finally:
        decimal.getcontext().prec = old_prec


def call_finance(func, *args, **kwargs):
    log.debug('req finance: %s %s %s', func, args, kwargs)
    try:
        ret = thrift_callex(config.FINANCE_SERVER, Finance, func, *args, **kwargs)
        log.debug('finance ret: %s', ret)
        return ret
    except finance_ttypes.ServerException as e:
        log.warn('finance error: %s', str(e))
        raise


def call_merchant(method, url, headers={}, *args, **kwargs):
    log.debug('req merchant: %s %s', args, kwargs)
    server = merchant_server.next()
    url = urlparse.urljoin(server['server']['addr'], url)
    client = RequestsClient(timeout=server['server']['timeout'] / 1000)
    content, status_code, headers = client.request(method, url, headers, *args, **kwargs)
    log.debug('merchant ret: %s %s', status_code, content)
    return status_code, content


def build_csv(fields, rows, write_header=True):
    buffer_ = StringIO()
    writer = csv.DictWriter(buffer_, fields)

    if write_header:
        # NOTE: 需要加上 BOM 头, 否则 office 会乱码.
        buffer_.write(codecs.BOM_UTF8)
        writer.writeheader()

    writer.writerows(rows)
    buffer_.seek(0)
    return buffer_.read()


def monthly_table_name(table_name, dtm=None):
    if dtm:
        dtm = datetime.datetime.strptime(dtm, '%Y-%m-%d')
    else:
        dtm = datetime.datetime.now()
    return '{0}_{1}'.format(table_name, dtm.strftime('%Y%m'))


def get_first_day_month(n=0):
    """获取当前时间往前或往后n个月的第一天的起始时间"""
    today = datetime.date.today()
    year, month, days = getyearandmonth(year=today.year, mon=today.month, n=n)
    return '{year}-{month}-01 00:00:00'.format(year=year, month=month)


def get_differ_days(time1, time2):
    '''获取时间差（天数），两个时间的格式是 "%Y-%m-%d %H:%M:%S" 这样的字符串'''
    date1 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
    differ_days = (date1 - date2).days
    return differ_days


def get_lang_by_code(code=None):
    ''' 返回常量
    如果code为空, 返回所有的常量,
    否则返回指定的常量
    '''
    cons = qfcache.get_data('language_constant')
    if not code:
        return cons

    try:
        return json.loads(cons[code])
    except:
        return cons[code]


def get_agent_user(dl_uid, raise_exception=False):
    log.debug('get dl_uid: %s', dl_uid)
    if not dl_uid:
        return None
    try:
        return call_org('qd_get', [int(dl_uid)])[0]
    except ttypes.QudaoException as e:
        if raise_exception:
            log.warn('org_api error: %s', str(e))
            raise
        else:
            return None
    except Exception:
        if raise_exception:
            raise
        else:
            log.warn(traceback.format_exc())
            return None

def fen_to_yuan(amt):
    '''
    将分转化为元
    '''
    if not is_valid_int(amt):
        raise ParamError('amt必须为整数')

    yuan = amt / 100.0

    return str(int(yuan)) if int(yuan) == yuan else str(yuan)


def get_mchnt_mccstr(mcc=None, lang=None, langconf=None):
    """根据mcc获取对应的中文mcc"""
    mcc_str = ''
    if not mcc:
        return mcc_str
    if not is_valid_int(mcc):
        return mcc_str
    mcc = int(mcc)
    with get_connection_exception('qf_mis') as db:
        ret = db.select_one(
            'tools_mcc',
            where={'id': mcc, 'mcc_display': 1}
        )
    if not ret:
        with get_connection_exception('qf_mis') as db:
            ret = db.select_one(
                'tools_mcca',
                where={'id': mcc, 'mcca_display': 1}
            )
        if ret:
            mcc_str = ret['mcca_name']
    else:
        mcc_str = ret['mcc_name']
    if lang == 'en':
        for i in PRIMARY_MCC:
            if mcc_str == i['name']:
                mcc = i['id']
        for i in getattr(langconf, 'PRIMARY_MCC'):
            if mcc == i['id']:
                mcc_str = i['name']

    return mcc_str


def check_str_long(str=None, num=None):
    if not str or not num:
        return False
    if len(unicode(str, encoding='utf8')) > num:
        return False
    return True


def check_expire_time(expire_time=None, format=None):
    # 校验时间格式
    try:
        expire_time = datetime.datetime.strptime(expire_time, format)
    except Exception:
        log.warn('time format error: %s', expire_time)
        raise ParamError('time format error')
    return expire_time


def get_redis_mcca():
    '''从redis里获取mcca列表信息，如果没有，查数据库设置'''
    if redis_pool.exists("mcca_infos_key"):
        return json.loads(redis_pool.get('mcca_infos_key'))
    else:
        with get_connection_exception('qf_mis') as db:
            ret = db.select(
                'tools_mcca',
                where={'mcca_display': 1}
            )
        if ret:
            # 设置redis
            redis_pool.set('mcca_infos_key', json.dumps(ret))
            return ret