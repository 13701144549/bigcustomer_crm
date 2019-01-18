# coding:utf-8

import json
import logging
import config
import xlrd
import traceback
import decimal
import uuid
import os
import datetime
import config

from valid import is_valid_int
from runtime import apcli
from excepts import ParamError
from utils.constants import PRIMARY_MCC

from qfcommon.base.dbpool import get_connection, get_connection_exception
from qfcommon.web.core import Handler
from qfcommon.qfpay.apollouser import ApolloUser
from qfcommon.web.http import ChunkedResponse
from qfcommon.thriftclient.apollo.ttypes import UserExt

from utils.constants import PermDef, UserDef, BatchCreateDef
from utils.valid import is_valid_num

import re

re_email = re.compile(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z0-9]{3}$')

log = logging.getLogger()

web_cate = getattr(config, 'WEB_CATE', UserDef.ORG_USER_CATE)


class BaseHandler(Handler):

    def initial(self):
        self.set_headers({
            'Content-Type': 'application/json; charset=UTF-8'
        })
        log.debug("lang : %s", self.req.environ.get('HTTP_LANG'))

    def get_name(self, userid=None):
        try:
            if not userid:
                return self.user.ses['username']
        except:
            pass

        user = {}
        if getattr(self, '_user', None):
            user = self._user
        else:
            try:
                userid = userid or self.user.userid
                if userid:
                    user = apcli.findUserBriefById(int(userid))
                    self._user = user = user.__dict__
            except:
                user = {}

        return user.get('name') or ''

    def get_cates(self, userid=None, reload=False):
        self._new_get_cates = False
        try:
            if not reload and not self._new_get_cates:
                return self.user.ses.data['user_cates']
        except:
            pass

        try:
            self._new_get_cates = True
            userid = int(userid or self.user.userid)
            cates = apcli.get_user_cate(userid)
            cates = [cate['code'] for cate in cates or []]
        except:
            cates = []

        try:
            self.user.ses.data['user_cates'] = cates
        except:
            pass

        return cates

    def get_cate(self, userid=None, cates=None):
        ''' 商户角色

        Returns:
            bigmerchant: 大商户
            submerchant: 子商户
            merchant: 商户
        '''
        cate = ''
        cate_dict = cates
        if not userid:
            return cate
        if not cates:
            try:
                userid = userid
                cates = apcli.get_user_cate(userid)
            except:
                cates = []
            cate_dict = {cate['code'] for cate in cates or []}
        if 'bigmerchant' in cate_dict:
            cate = 'bigmerchant'

        elif 'mchnt' in cate_dict and 'submchnt' not in cate_dict:
            cate = 'merchant'
        elif 'submchnt' in cate_dict and 'mchnt' not in cate_dict:
            cate = 'submerchant'
        elif 'mchnt' in cate_dict and 'submchnt' in cate_dict:
            big_uid = apcli.reverse_userids(userid, 'merchant')
            if big_uid:
                self._big_uid = big_uid[0].userid
                cate = 'submerchant'
            else:
                cate = 'merchant'

        return cate

    def check_cate(self, cate=web_cate, userid=None):
        if not cate: return True

        for flag in (False, True):
            user_cates = self.get_cates(userid, flag)
            if cate in user_cates:
                return True

        return False

    def get_perms(self, userid=None, reload=False):
        self._new_get_perms = False
        try:
            if not reload and not self._new_get_perms:
                return self.user.ses.data['perms']
        except:
            pass

        try:
            self._new_get_perms = True
            userid = int(userid or self.user.userid)
            perms = apcli('get_user_permissions', userid)
            perms = [p.code for p in perms or []
                     if p.group.startswith(PermDef.PERM_ROLE_GROUP)]
        except:
            perms = []

        try:
            self.user.ses.data['perms'] = perms
        except:
            pass

        return perms

    def check_perms(self, perm_codes, userid=None):
        if not perm_codes:
            return True

        for flag in (False, True):
            user_perms = self.get_perms(userid, flag)
            if set(perm_codes) & set(user_perms):
                return True

        return False

    def check_login(self):
        '''
        method: 验证商户是否登录
        return: 是否登录并会将session值写入self
        '''
        try:
            sessionid = self.get_cookie('sessionid')
            self.user = ApolloUser(sessionid=sessionid)
            if not self.user.is_login():
                return False
        except:
            log.warn('check_login error: %s' % traceback.format_exc())
            return False
        return True

    def get_pageinfo(self, params=None):
        params = params or self.req.input()

        page = params.get('page', 1)
        pagesize = params.get('pagesize', 10)

        if not is_valid_int(page) or not is_valid_int(pagesize):
            raise ParamError('分页信息错误')

        limit = int(pagesize)

        offset = limit * int(page)

        return limit, offset

    def get_where(self, fields=None, intfields=None, likefields=None, params=None):
        params = params or self.req.input()

        fields = fields or []
        intfields = intfields or []
        likefields = likefields or []
        # where
        where = {}
        search = list(fields) + list(intfields) + list(likefields)
        for i in search:
            if not params.get(i):
                continue
            elif i in intfields:
                where[i] = int(params[i])
            elif i in likefields:
                where[i] = 'like', '%%%s%%' % params[i]
            elif i in fields:
                where[i] = params[i]
        return where

    def get_other(
            self, fields=None, default_field='ctime',
            default_type='desc', params=None
    ):
        '''
        获取sql查询other

        params:
            fields: 可排序字段
            default_field: 默认排序字段
            default_type: 默认排序方法
            params: 所有参数, 不传默认使用input

        return:
            order by XX limit XX offset XX
        '''
        if params is None:
            params = self.req.input()

        order_field = params.get('order_field') or default_field
        order_type = params.get('order_type') or default_type
        if (
                (fields is not None and order_field not in fields) or
                order_type not in ('desc', 'asc')
        ):
            raise ParamError('排列信息错误')
        orderby = 'order by {order_field} {order_type}'.format(
            order_field=order_field, order_type=order_type)

        limit, offset = self.get_pageinfo(params)

        return '{orderby} limit {limit} offset {offset}'.format(
            orderby=orderby, limit=limit, offset=offset
        )

    def get_org_uid(self, userid=None):
        '''获取商户机构uid'''
        if not userid:
            try:
                return self.user.ses.data['groupid']
            except:
                pass

        admin = None
        with get_connection('qf_org') as db:
            userid = userid or self.user.userid
            admin = db.select_one(
                'org_admin', where={'userid': userid},
                fields='qd_uid'
            )

        if not admin:
            raise ParamError('org不存在')

        try:
            self.user.ses['org_uid'] = admin['qd_uid']
        except:
            pass

        return admin['qd_uid']


def get_area_cities(country_code):
    with get_connection('qf_org') as db:

        records_area = db.select(
            'tools_area',
            where={'country': country_code, 'area_display': 1},
            fields=('id areaid, area_name areaname, area_no'),
        )
        if records_area:
            records_areacity = db.select(
                'tools_areacity',
                where={'area_id': ('in', [i['areaid'] for i in records_area]), 'city_display': 1},
                fields=('id cityid, city_name cityname, city_no, area_id'),
            )
    rtn_val = {}
    for area in records_area or []:
        if area.get('areaid') not in rtn_val:
            rtn_val[area.get('areaid')] = {
                'areaid': area.get('areaid'),
                'areaname': area.get('areaname'),
                'area_no': area.get('area_no'),
                'cities': []
            }
        for areacity in records_areacity or []:
            if area.get('areaid') == areacity.get('area_id'):
                rtn_val[area.get('areaid')]['cities'].append({
                    'cityid': areacity.get('cityid'),
                    'cityname': areacity.get('cityname'),
                    'city_no': areacity.get('city_no')
                })

    return rtn_val


def get_qd_of_org(org_uid):
    ret = []

    if not org_uid:
        return ret

    with get_connection_exception('qf_org') as db:
        one = []
        one = db.select(
            table='qd_user',
            fields='qd_uid',
            where={'level': 2, 'parent': org_uid, 'status': 0},
        )
        one_uids = [i['qd_uid'] for i in one]
        if not one_uids:
            return ret

        two = []
        two = db.select(
            table='qd_user',
            fields='qd_uid',
            where={'level': 3, 'parent': ('in', one_uids), 'status': 0},
        )
        two_uids = [i['qd_uid'] for i in two]
        one_uids.extend(two_uids)
        ret = one_uids
    return ret


class BaseChunkedHandler(BaseHandler):

    def __init__(self, *args, **kwargs):
        super(BaseChunkedHandler, self).__init__(*args, **kwargs)
        self.resp = ChunkedResponse()

    def set_callback(self, func):
        self.resp.set_callback(func)


def add_user_ext(userid, data):
    contact = data['ext_contact'] if 'ext_contact' in data else data.get('landline', '') or data.get('telephone')
    user_ext = UserExt(
        uid=int(userid),
        shoptype_id=data.get('shoptype_id'),
        contact=contact,
        head_img=data.get('head_img'),
        logo_url=data.get('logo_url'),
        ext=json.dumps(data.get('user_ext') or {})
    )
    if is_valid_int(data.get('regionid')):
        user_ext.regionid = int(data['regionid'])
    apcli('bindUserExt', user_ext)


class UploadFileMixin(object):
    '''上传文件工具类'''

    def read_excel(self, content, head_fields, format_fields, prompt=None):
        adapt_fields = ('MDR(%)', )
        num_fislds = ('mobile', 'telephone', 'storetelephone', 'mcc', 'is_contract')
        excel_num_fislds = ('Contact Number', 'Store Contact Number')
        items = []
        excel = ReadExcel(content)
        sheets = excel.sheet_names()
        num = 1
        for row in excel.readlines(sheet_name=sheets[0], min_row=config.MIN_ROW):
            item = {}
            for idx, field in enumerate(head_fields):
                value = row[idx].encode('utf8') if isinstance(row[idx], unicode) else row[idx]
                if value not in ('0', 0) and not value:
                    raise ParamError(getattr(prompt, 'RESPMSG').WRITE_PARAMETER.format(num, field))

                for i in BatchCreateDef.BATCH_EXCEL_FIELDS:
                    if field in adapt_fields:
                        if row[idx] or row[idx] == 0:
                            value = row[idx].encode('utf8') if isinstance(row[idx], unicode) else row[idx]
                            if not is_valid_num(value):
                                raise ParamError(getattr(prompt, 'RESPMSG').ONLY_BE_NUM.format(num, 'MDR(%)', value))
                            ratio = str(value).split('.')[1] if value != '0' else '0'
                            if len(ratio) > 2:
                                raise ParamError(getattr(prompt, 'RESPMSG').FEE_DIGITS.format(num))
                            if field in i:
                                field = i[field]
                                item[field] = float(decimal.Decimal(float(value)) / decimal.Decimal(100.0))
                    elif row[idx] or row[idx] == 0:
                        if field in i:
                            value = row[idx].encode('utf8') if isinstance(row[idx], unicode) else row[idx]
                            if field in excel_num_fislds and not is_valid_num(value):
                                raise ParamError(getattr(prompt, 'RESPMSG').ONLY_BE_NUM.format(num, field, value))
                            field = i[field]
                            if field == 'cate':
                                if value not in BatchCreateDef.CATE:
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'Merchant Category'))
                                value = BatchCreateDef.CATE[value]
                            if field == 'is_contract':
                                if value not in BatchCreateDef.IS_CONTRACT:
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'Agreement Signed (Yes/No)'))
                                value = BatchCreateDef.IS_CONTRACT[value]
                            if field == 'location' or field == 'storelocation':
                                if value not in BatchCreateDef.LOCATION:
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'Area'))
                                value = BatchCreateDef.LOCATION[value]
                            if field == 'settlement_time':
                                if value not in BatchCreateDef.SETTLEMENT_TIME:
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'Settlement Period'))
                                value = BatchCreateDef.SETTLEMENT_TIME[value]
                            if field == 'mcc':
                                mccs = []
                                if getattr(prompt, 'ALL') == 'All':
                                    mccs = getattr(prompt, 'PRIMARY_MCC')
                                elif getattr(prompt, 'ALL') == '全部':
                                    mccs = PRIMARY_MCC
                                for mcc in mccs:
                                    if value == mcc['name'] and mcc['display'] == 1:
                                        value = mcc['id']
                                        break
                                else:
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'Industry'))
                            if field == 'email':
                                if not re_email.match(value):
                                    raise ParamError(
                                        getattr(prompt, 'RESPMSG').EXCEL_BASE.format(num, 'E-mail Address'))
                            if field in num_fislds and is_valid_num(value):
                                value = int(value)
                            else:
                                value = str(value).strip()
                            item[field] = value

            items.append(item)
            num += 1

        return items

    def dump_file(self, items, memo):
        ret = {}
        try:
            mfs_path = os.path.join(config.EXCEL_BASE_URL, datetime.date.today().strftime('%Y%m%d'))
            if not os.path.exists(mfs_path):
                os.mkdir(mfs_path)
        except Exception:
            log.warn(traceback.format_exc())
            return ret

        fileid = str(uuid.uuid1())
        try:
            with open(os.path.join(mfs_path, fileid), 'w') as f:
                data = {'mchnts': items, 'file_name': memo}
                json.dump(data, f)
        except Exception:
            log.warn('save data error: %s', traceback.format_exc())
            return ret

        ret['fileid'] = fileid
        return ret


class _BaseReadExcel(object):
    def sheet_names(self):
        """

        :return:
        :rtype:  list[str]
        """
        pass

    def readlines(self, sheet_name, min_row, **kw):
        """

        :param sheet_name:
        :type sheet_name:
        :param min_row:
        :type min_row:
        :param kw:
        :type kw:
        :return:
        :rtype: list[object] | generator
        """
        pass


class ReadExcelXlrd(_BaseReadExcel):
    """
    xlrd方式的excel读取，具有更好的兼容性
    openpyxl方式的读取，可能会遇到mac numbers编辑之后，出现无用的空白行和列。
    """

    def __init__(self, path, **kw):
        is_file_like = hasattr(path, 'read')
        if is_file_like:
            path.seek(0)
            wb = xlrd.open_workbook(file_contents=path.read())
        else:
            wb = xlrd.open_workbook(path)

        self.wb = wb

    def sheet_names(self):
        return [sheet.name for sheet in self.wb.sheets()]

    def readlines(self, sheet_name, min_row=1, **kw):
        min_row -= 1  # xlrd的行，从0开始

        sheet = self.wb.sheet_by_name(sheet_name)
        for rowx in range(min_row, sheet.nrows):
            row = sheet.row(rowx)
            yield [cell.value for cell in row]

    def sheet(self, sheet_name):
        return self.wb.sheet_by_name(sheet_name)

# 默认使用xlrd方式的excel读取
ReadExcel = ReadExcelXlrd
