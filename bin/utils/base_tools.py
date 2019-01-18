# coding:utf-8

'''
基础工具类
'''

import os
import config
import logging
import traceback
import decimal

from constants import ApplyDef
from excepts import ParamError, UserError
from valid import is_valid_int
from client import finance_client, org_client, ap_client, account2_client
from tools import unicode_to_utf8

from qfcommon.web import cache
from qfcommon.qfpay import defines
from qfcommon.server.client import HttpClient, ThriftClient
from qfcommon.base.dbpool import get_connection_exception, get_connection
from qfcommon.thriftclient.fund2 import Fund2
from qfcommon.thriftclient.fund2.ttypes import UserRuleArgs
from qfcommon.thriftclient.account2.ttypes import CostFeeQueryArgs, FeeQueryArgs
from qfcommon.thriftclient.org import ttypes


log = logging.getLogger()

base_url = getattr(
    config, 'BASE_URL', 'http://pic.qfpay.com'
)
BASE_URL = os.path.join(base_url, 'userprofile')


class QudaoTools(object):
    '''渠道基础'''

    def get_qudao_infos(self, qd_uids, **kw):
        '''获取渠道信息'''
        if not qd_uids:
            return []

        where = {'qd_uid' : ('in', qd_uids)}

        fields = kw.get('fields', '*')

        with get_connection_exception('qf_org') as db:
            qds = db.select('qd_profile', where=where, fields=fields)

        return qds

    def get_hierarchy_qd_uids(self, org_uid, max_hierarchy=2, status=ttypes.QudaoStatus.ALL):
        return org_client('qd_get_hierarchy', [int(org_uid), ], max_hierarchy, status).get(int(org_uid))

    def check_belong(self, qd_uid, org_uid=None):
        '''验证渠道id归属关系'''

        if org_uid == qd_uid:
            return True
        if qd_uid in self.get_hierarchy_qd_uids(org_uid):
            return True

        raise UserError("Don't belong to the current organization")

    def get_qd_ratio(self, qd_uid):
        '''取出代理商费率(新的费率存储结构)'''
        data = {'groupid': [int(qd_uid), ], }
        query = CostFeeQueryArgs(**data)
        # 取出代理商的费率
        qd_accounts = account2_client(
            'cost_feeratio_query', query
        )
        ret = []
        if not qd_accounts:
            return ret
        for i in qd_accounts:
            ratio = float(decimal.Decimal(i.ratio * 100 or 0.00))
            ratio = ('%.2f') % ratio
            account = {'ratio': ratio, 'chnl_id': i.chnl_id, 'trade_type': i.trade_type,
                       'trade_type_name': defines.busicd[i.trade_type]}
            with get_connection('qf_core') as db:
                channel_name = db.select_one(
                    'channel',
                    where={'code': i.chnl_id},
                ) or {}
            account['chnl_name'] = channel_name.get('name')
            ret.append(account)
        return ret


class MchntTools(QudaoTools):
    '''商户基础'''

    def query_fee_ratios(self, userids, step=100):
        ret = {}
        for idx in range(0, len(userids), step):
            ret_data = finance_client('get_trade_fee_list', userids[idx:idx + step])
            for i in ret_data:
                ret[i.userid] = {
                    'userid' : i.userid,
                    'debit_ratio' : i.debit_ratio,
                    'credit_ratio' : i.credit_ratio,
                    'tenpay_ratio' : ('%.2f') % (i.tenpay_ratio * 100),
                    'alipay_ratio' : i.alipay_ratio,
                    'jdpay_ratio' : i.jdpay_ratio,
                    'qqpay_ratio' : i.qqpay_ratio
                }

        return ret

    def get_mchnt_ratios(self, userids=None, qd_uid=None):
        qd_ratio = self.get_qd_ratio(qd_uid)
        trade_types = [str(i['trade_type']) for i in qd_ratio]
        query = FeeQueryArgs(userid=userids, trade_type=trade_types, card_type=config.CARD_TYPE, refresh_cache=1)
        # query = FeeQueryArgs(userid=userids)
        ret_data = account2_client('fee_ratio_query', query)
        ret = []
        data = {}
        for i in ret_data:
            for k in qd_ratio:
                if int(i.trade_type) == int(k['trade_type']):
                    account = {
                        'chnl_name': k['chnl_name'],
                        'chnl_id': k['chnl_id'],
                        'trade_type': k['trade_type'],
                        'ratio': ('%.2f') % (i.ratio * 100),
                        'trade_type_name': k['trade_type_name'],
                    }
                    data.setdefault(account['chnl_id'], []).append(account)
        for i in data:
            data_ = {'busicd': data[i], 'name': data[i][0]['chnl_name']}
            ret.append(data_)
        return ret

    def get_vouchers(self, userid):
        with get_connection_exception('qf_mis') as db:
            vouchers = db.select(
                'mis_upgrade_voucher',
                where={'user_id':int(userid)}, fields='name, imgname'
            ) or []

        userdir =  '%s/%s' % (int(userid)/10000, userid)

        ret = []
        for i in vouchers:
            ret.append({
                'name' : i['name'],
                'imgname' : i['imgname'],
                'url' : os.path.join(BASE_URL, userdir, i['imgname'])
            })

        return ret

    def get_auditlogs(self, userid):
        with get_connection_exception('qf_mis') as db:
            auditlogs = db.select(
                'mis_auditlog',
                where={'user_id':int(userid), 'is_delete':0},
                fields='memo, create_user, create_date, result',
                other='order by create_date desc'
            ) or []

        for i in auditlogs:
            i['result_str'] = ApplyDef.AUDIT_RESULT_MAP.get(i['result'], '未知状态')

        return auditlogs

    def get_mchnt_user(self, userid):
        '''获取商户信息'''
        if not is_valid_int(userid):
            raise ParamError('No merchant')
        userid = int(userid)

        with get_connection_exception('qf_org') as db:
            mchnt_user = db.select_one(
                'mchnt_user', where={'mchnt_uid' : userid}
            )
        if not mchnt_user:
            raise ParamError('No merchant')

        return mchnt_user

    def get_mchnt_shoptype_path(self, userid=None, shoptype_id=None):
        '''获取店铺类型'''
        def find(shoptype):
            while 1:
                if shoptype in all_types:
                    yield all_types[shoptype]['name']
                    shoptype = all_types[shoptype]['parent_id']
                else:
                    return

        def get_shoptype_id():
            if shoptype_id:
                return shoptype_id

            user_ext = ap_client('getUserExt', int(userid))
            if not user_ext:
                return None
            return user_ext.shoptype_id

        all_types = cache.get('kuma_shop_cates')
        cid = get_shoptype_id()
        if not cid:
            return []

        return list(find(cid))[::-1]

    def get_enuserid(self, userid):
        syssn = int(userid) + 20141314654321L
        char_lib = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_list = list(char_lib)
        lenth =  len(char_lib)
        index = 0
        result = []
        rs = syssn

        while(rs > lenth):
            result.append(rs % lenth)
            rs = rs / lenth
            index = index + 1

        result.append(rs)
        ret = ''
        for t in result:
            ret = ret + char_list[t]
        return ret

    def up_vouchers(self, userid, enuserid, vouchers):
        '''上传凭证照片'''
        if not vouchers:
            return

        # 特定上传enuserid, 需要移动到指定目录
        if enuserid == 'EPeRaNEt':
            imgnames = [i['imgname'] for i in vouchers]
            HttpClient(config.OPENAPI2_SERVERS).post(
                '/util/v1/mvfile', {'imgname': ','.join(imgnames), 'userid':userid}
            )

        insert_data = []
        for i in vouchers:
            insert_data.append({
                'user_id': userid, 'upgrade_id': 0, 'apply_level': 0,
                'cert_type': i['cert_type'], 'name': i['name'],
                'submit_time': 'now()',
                'state': ApplyDef.VOUCHER_STATE_PASS, 'input_state': 1,
                'typist_user' : 0,
                'typist_time': 'now()',
                'imgname': i['imgname']
            })
        with get_connection('qf_mis') as db:
            db.insert_list(
                'mis_upgrade_voucher', insert_data,
                other = (
                    'on duplicate key update state=values(state),'
                    'imgname=values(imgname)'
                )
            )

    def get_user_rule(self, query=None):
        '''商户规则查询'''
        try:
            client = ThriftClient(config.FUND2_SERVERS, Fund2)
            fields = ('group_id', 'user_id', 'user_name')
            data = {i: query[i] for i in fields if query.get(i)}
            args = UserRuleArgs(**data)
            result = client.user_rule_query(args)
            if result:
                return result
        except:
            log.warn(traceback.format_exc())

    def get_remit_amt(self, query=None):
        '''查询结算资金起点'''
        if 'bankaccount' not in query:
            return ''
        where = {'cardno': unicode_to_utf8(query.get('bankaccount'))}
        with get_connection('qf_fund2') as db:
            remit_amt = db.select_one(
                'remit_rule',
                where=where,
            ) or {}
        if not remit_amt:
            return ''
        else:
            return remit_amt['amt']