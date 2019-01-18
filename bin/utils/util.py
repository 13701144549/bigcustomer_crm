#coding: utf-8

''' api tools

functions:
    1: build pagination
    2: export excel
    3: args type operation(check translate business_control)

'''

import datetime
import traceback
import xlwt
import config
import json
import StringIO
import logging
import globalization
log = logging.getLogger()


from qfcommon.base.dbpool import get_connection, get_connection_exception
from qfcommon.base.tools import thrift_callex
from qfcommon.library.excel import Cell
from qfcommon.thriftclient.spring import Spring

from utils.base import BaseHandler
from utils.excepts import ParamError
from utils.constants import BaseDef, PermDef, UserDef
from utils.runtime import apcli
from utils.misc import minus_seconds, str2datetime
from utils.valid import is_valid_datetime, is_date_type

__version__ = '2.7.1'

langs = globalization.LANGS

class ValidArgs(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        pass

    def _default(self, value):
        return value

    def _none_check(self, value):
        if value is None:
            return False
        return value

    def _is_valid(self, v, f):
        if not v:
            return False
        try:
            v = f(v)
            return v
        except:
            log.warn(traceback.format_exc())
            return False

    def v_int(self, value):
        return self._is_valid(value, int)

    def v_float(self, value):
        return self._is_valid(value, float)

    def v_str(self, value):
        if not value:
            return False
        return str(value)

    def v_datetime(self, value):
        value = str(value)
        dtck = lambda s: datetime.datetime.strptime(value, BaseDef.DATETIME_FMT)
        return self._is_valid(value, dtck)

    def v_json(self, value):
        value = self._is_valid(value, json.loads)
        if not value:
            return False
        return value

    def v_manual(self, value):
        return self._default(value)

    def v_split(self, value, processer=None):
        value = str(value)
        value_list = value.split(',')
        value_list = [i.strip() for i in value_list if i.strip()]
        if not processer:
            return value_list
        value_list = map(processer, value_list)
        return value_list if False not in value_list else False

    def v_split_int(self, value):
        return self.v_split(value, self.v_int)

    def v_split_str(self, value):
        return self.v_split(value, self.v_str)


class ArgsBuilder(object):

    def __init__(self, args_idft=None, valid_args=None, source=None):
        '''初始化'''

        # args identification config
        self.args_idft = args_idft or {}
        # soruce args
        self.source = source or {}
        # checked args
        self.values = {}
        # other args
        self.others = {}
        # FIXME
        self.valid_args = valid_args or ValidArgs()

    def _verify(self):

        # return if none
        if not self.args_idft:
            return

        # type check
        for suffix, arg_key_list in self.args_idft.items():
            for arg_key in arg_key_list:
                value = self._arg_trans(suffix, arg_key)
                self.values[arg_key] = value
        # logic check
        for k,v in self.values.items():
            bl_verify_func = getattr(self, k, self._default)
            self.values[k] = bl_verify_func(v)

    def _arg_trans(self, suffix, arg_key):
        ''' 类型校验

        params:
            suffix: 校验函数名称部分
            arg_key: 用来取值
        return:
            valid_ret: 经过校验函数处理以后的值

        '''

        arg_value = self.source.get(arg_key)

        # load err info
        args_lang_map = getattr(self, 'args_lang_map', {})
        err_info = '请输入{}'.format(arg_key)
        zh_err_info = args_lang_map.get(arg_key)
        if zh_err_info:
            err_info = zh_err_info

        # valid func check
        valid_func = getattr(self.valid_args, 'v_'+suffix, None)
        if not valid_func:
            log.warn('MH> no mapping type checker for {}'.format(arg_key))
            raise ParamError('系统内部错误')

        # value check by valid func
        valid_ret = valid_func(arg_value)
        if valid_ret is False:
            log.warn('MH> args type error:{}:{}'.format(arg_key, arg_value))
            raise ParamError(err_info)
        return valid_ret

    def _default(self, value):
        return value

class MisHandler(BaseHandler):


    def initial(self):
        self.args_builder = getattr(self, 'args_builder', ArgsBuilder)
        self.args_idft= {}
        self.args_lang_map = {}
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        self.use_dt = False

        log.debug("lang : %s", self.req.environ.get('HTTP_LANG'))
        self.lang = self.req.environ.get('HTTP_LANG', 'en-us').split('-')[0]  # zh-cn 中文，默认是英文
        self.langconf = langs[self.lang]
        if hasattr(self, 'before_api_call'):
            self.before_api_call()

    def build_args(self):
        '''验证参数'''
        if hasattr(self, 'values') and self.values:
            return self.values
        log.info('args_builder is {}'.format(self.args_builder.__name__))
        self.args_builder_inst = self.args_builder(
                self.args_idft, None, self.req.input())
        self.args_builder_inst._verify()
        self.values = self.args_builder_inst.values
        self.others = self.args_builder_inst.others
        log.info('built_args is {}'.format(self.values))
        log.info('built_others is {}'.format(self.others))
        return self.values

    def get_others(self):
        if not hasattr(self, 'args_builder_inst'):
            raise ParamError('未初始化')
        if hasattr(self, 'others') and self.others:
            return self.others
        log.info('others = {}'.format(self.args_builder_inst.others))
        return self.args_builder_inst.others

    def build_lists(self, data=None):

        d = data or self.req.input()
        d['offset'] = int(self.req.input().get('offset', 0))
        d['pageSize'] = int(self.req.input().get('pageSize', 10))
        offset = d['offset']
        limit = d['pageSize']

        # 如果使用了datatable,则兼容
        use_dt = getattr(self, 'use_dt', False)
        if not use_dt:
            offset = offset * limit

        if 'table' not in self.list_args:
            raise ParamError('未知表')
        if 'db' not in self.list_args:
            raise ParamError('未知库')

        where = {}
        fuzzy_search = self.list_args.get('fuzzy', [])
        split_search = self.list_args.get('split', [])
        split_seq = self.list_args.get('split_seq', ',')
        if 'limit' in self.list_args:
            for item in self.list_args['limit']:
                where.update(item)
        if 'where' in self.list_args:
            for item in self.list_args['where']:
                item_value = d.get(item)
                # 处理value
                if item in split_search and item_value:
                    item_value = item_value.split(split_seq)
                if item_value:
                    # 特殊搜索
                    if item in fuzzy_search:
                        where[item] = ('like', '%{}%'.format(item_value))
                    elif item in split_search:
                        where[item] = ('in', item_value)
                    elif isinstance(item_value, list):
                        where[item] = ('in', item_value)
                    else:
                        where[item] = item_value
                if item.endswith('date') or item.endswith('time'):
                    start_time = d.get('start_time')
                    end_time = d.get('end_time')
                    if start_time and end_time:
                        where[item] = ('between', (start_time, end_time))
        log.debug('where={}'.format(where))
        self.build_where = where

        total = 0
        lists = []
        ret = {'total': total, 'list': lists}
        order_by = self.list_args.get('order_by') or ''
        group_by = self.list_args.get('group_by') or ''
        sort = self.list_args.get('sort') or 'desc'

        other = ''
        other_total = ''
        if group_by:
            other += 'group by {} '.format(group_by)
        if order_by:
            other += 'order by {} '.format(order_by)
        other_total = other
        other += sort
        if not (d.get('mode') == 'expo_excel'):
            other += ' limit {limit} offset {offset} '.format(
                limit = limit, offset = offset)
        log.debug('other_total={}|other={}'.format(other_total, other))

        # 返回值
        table = self.list_args['table']
        database = self.list_args['db']
        fields = self.list_args.get('fields', '*')
        with get_connection(database) as db:
            lists = db.select(table,where=where,other=other,fields=fields)
            total = db.select(
                    table,fields='count(1) total',other=other_total,
                    where = where)
        # group by
        total = len(total) if group_by else total[0]['total']
        for li in lists:
            for k in li:
                if li[k] is None:
                    li[k] = ''
        ret['total'] = total
        ret['list'] = lists
        log.debug('source_list={}'.format(lists))

        return ret

    def build_excel(self, lists, excel_name='expo.xls'):
        if not self.head_list:
            raise ParamError('缺少excel列表头部')

        self.set_headers({'Content-Type': 'application/octet-stream'})
        self.set_headers(
            {'Content-disposition': 'attachment; filename={}'.format(excel_name)})
        return excel_data(self.head_list, lists)

    def is_expo_excel(self):
        if self.req.input().get('mode') == 'expo_excel':
            return True
        return False

def excel_data(head, data):
    if not head:
        raise ParamError('缺少excel列表头部')

    rows = []
    heads = []
    for head_data in head:
        arg_name = head_data[0]
        arg_str = head_data[1]
        heads.append(Cell(arg_str))
    rows.append(heads)

    max_item = getattr(config, 'MAX_EXCEL_ROWS', 5000)
    if len(data) > max_item:
        raise ParamError('导出数量太多,限制为{}条'.format(max_item))

    for item in data:
        row = []
        for head_data in head:
            arg_name = head_data[0]
            arg_str = head_data[1]
            tmp = Cell(str(item.get(arg_name, '')))
            row.append(tmp)
        rows.append(row)
    sio = StringIO.StringIO()
    create_xl(sio, rows)
    return sio.getvalue()


def create_xl(sio, rows = None):
    '''
    根据rows[[], [], []]完成表格
    多个sheet存储，每个sheet数目可配置
    '''
    # 创建excel文件
    table = xlwt.Workbook()
    head_list = rows.pop(0)
    if rows:
        n = 1
        for sheet_num in xrange(1, len(rows) + 1, config.SHEET_NUM):
            sheet_s = str((n - 1) * config.SHEET_NUM + 1)
            sheet_e = str(n * config.SHEET_NUM if n * config.SHEET_NUM < len(rows) else len(rows))
            sheet = table.add_sheet(sheet_s + '-' + sheet_e)
            for colnum in xrange(0, len(head_list)):
                cell = head_list[colnum]
                sheet.write(0, colnum, cell.value)
            m = 1
            for rownum in xrange((n - 1) * config.SHEET_NUM, n * config.SHEET_NUM):
                if rownum < len(rows):
                    for colnum in xrange(0, len(rows[rownum])):
                        cell = rows[rownum][colnum]
                        sheet.write(m, colnum, cell.value)
                m += 1
            n += 1
    table.save(sio)


def get_str_len(name, cn=1, en=1):
    len_of_name = 0
    try:
        if not isinstance(name, unicode):
            name = str(name).decode('utf8')
        for i in name:
            if u'\u4e00' <= i <= u'\u9fff':
                len_of_name += cn
            else:
                len_of_name += en
    except:
        log.warn(traceback.format_exc())
        return 0 # 字符串长度设置为0
    return len_of_name

def gen_id():
    '''生成唯一号'''
    try:
        ret =thrift_callex(config.SPRING_SERVERS,Spring,"getid")
        return int(ret)
    except:
        log.error("call Spring error. reason .{0}".format(traceback.format_exc()))
        raise

def trans_to(args, func):
    try:
        if isinstance(args, (list, set)):
            return map(func, args)
        if isinstance(args, (dict)):
            for k,v in args.items():
                args[k] = func(v)
            return args
        return func(args)
    except:
        log.warn(traceback.format_exc())
        raise ParamError('包含非法字符，请使用英文逗号分割')

def is_future(dt):
    # 首先校验是否是时间
    if not is_date_type(dt):
        if isinstance(dt, str) and not is_valid_datetime(dt):
            raise ParamError('工具:格式错误')
        else:
            dt = str2datetime(dt)

    # 然后结算时间差
    now = datetime.datetime.now()
    seconds = minus_seconds(dt, now)
    return True if seconds > 0 else False


def info_by_syssn(syssn):
    '''根据syssn 获取交易的上下文信息'''

    if not syssn:
        raise ParamError('没有syssn')

    table = 'record_{}'.format(syssn[0:6])
    where = {'syssn': syssn}
    fields = ['userid']

    # 如果没有表 直接抛出错误
    record_info = {}
    with get_connection_exception('qf_trade') as db:
        record_info = db.select_one(
            table = table,
            fields = fields,
            where = where
        ) or {}

    return record_info

def rebuild(items, key, value=None):
    '''重新组装为dict'''

    ret = {}
    if isinstance(items, list):
        for i in items:
            ret_key = i.get(key)
            if not ret_key:
                continue
            ret_value = i.get(value) if value else i
            # if ret_key in ret:
                # tmp = []
                # tmp.append(ret_value)
                # tmp.append()
            ret[ret_key] = ret_value
    if len(ret) < 50:
        log.info('rebuilt dict={}'.format(ret))
    return ret

def fetch_all(func, arg, offset=100):
    '''分页情况下获取所有的数据

    只支持arg 包含QueryMeta结构的thrift call

    '''

    if not callable(func):
        raise ParamError('需要是func')
    if not hasattr(arg, 'query_meta'):
        raise ParamError('工具:不支持的模式')

    ret = []
    part = func(arg)

    while part:
        ret.extend(part)
        arg.query_meta.offset += offset
        part = func(arg)
    return ret

