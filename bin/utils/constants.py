# coding:utf8

'''
常量定义模块
每个业务模块的常量定义用类分开
基础常量请写在BaseDef中
'''

import types
from qfcommon.thriftclient.qudao import ttypes
from qfcommon.qfpay.defines import (
    QF_USTATE_NEW, QF_USTATE_VARIFIED, QF_USTATE_ACTIVE, QF_USTATE_FORBID, QF_USTATE_CANCEL,
    QF_USTATE_OK, QF_USTATE_DULL, QF_BUSICD_PREPAID_REFUND, QF_BUSICD_CANCEL, QF_USTATE_CLOSE,
    QF_BUSICD_WEIXIN_HK_REFUND, QF_BUSICD_ALIPAY_ONLINE_REFUND, QF_BUSICD_ALIPAY_REFUND, QF_BUSICD_WEIXIN_REFUND,
    QF_BUSICD_AIRPAY_REFUND, QF_BUSICD_UNIONPAY_QRCODE_REFUND, QF_USTATE_DESTROY
)

from qfcommon.qfpay import defines


class BaseDef(object):

    # ListType, TupleType
    MulType = (types.ListType, types.TupleType)

    # 时间格式
    DTM_FMT = DATETIME_FMT = '%Y-%m-%d %H:%M:%S'
    DT_FMT = DATE_FMT = '%Y-%m-%d'
    DTM_PATTERN = r"^\d{4}(-\d\d){2} \d\d(:\d\d){2}"

    # 手机号码正则
    MOBILE_PATTERN = '^1(0|1|2|3|4|5|6|7|8|9)\d{9}$'

class AgentDef(object):

    STATUS = (INVALID, VALID) = (1, 0)

class SlsmDef(object):

    STATUS = (INVALID, VALID) = (1, 0)

class ClearingDef(object):

    # 结算周期形式
    SETTLEMENT_CYCLE = (DAY, WEEK, MONTH) = (1, 2, 3)
    # 清分模板类型
    TYPE = (COMMON, LADDER_PER, LADDER_NUM) = (1, 2, 3)
    # 启用条件（单笔金额）
    CONDITION_TYPE = ('gt', 'ge', 'lt', 'le')
    # 通道成本类型
    CHNLCOST_TYPE = (PER, NUM) = (1, 2)
    # 结算类型
    SETTLE_TYPE = (INCOME, PAY) = (1, 2)
    SETTLE_TYPE_DICT = {
        INCOME: '收入',
        PAY: '支出',
    }
    # 结算用户
    SETTLE_ROLE = (ORG, ONE, TWO) = (1, 2, 3)
    SETTLE_ROLE_DICT = {
        ORG: '机构',
        ONE: '一级代理',
        TWO: '二级代理',
    }

class UserDef(object):

    ORG_USER_CATE = 'org_user'
    ORG_SUPER_CATE = 'org_super'

    # import from qfcommon defines
    ALLOW_LOGIN_STATES = (
        QF_USTATE_NEW, QF_USTATE_VARIFIED, QF_USTATE_ACTIVE,
        QF_USTATE_OK
    )

    # user state
    USER_STATE = OPEN, CLOSE = (1, 9)


class PermDef(object):
    PERM_ROLE_GROUP = 'org_protal_group'
    ROOT_ROLE_CODE = 'org_portal_root_role'

    STATUS = VALID, INVALID = 1, 0

    # 主模块
    PERM_MAIN_STRUCT = [
        ('home', '首页'),
        ('mchnt_manage', '商户管理'), ('trade_manage', '交易管理'),
        ('salesman_manage', '业务员管理'),
        ('agent_manage', '代理商管理'), ('settlement_manage', '结算管理'),
        ('perm_manage', '权限管理')
    ]

    # 子模块
    # list结尾代表 -- 模块和api
    # 其他结尾的api
    PERM_STRUCT = {
        'mchnt_manage': [
            'mchnt_manage_list', 'mchnt_manage_create', 'shop_manage_list',
            'shop_manage_export', 'mchnt_manage_batch_create',
            'mchnt_audit_list'
        ],
        'trade_manage': [
            'trade_detail_list', 'trade_summary_list', 'trade_detail_export'
        ],
        'salesman_manage': [
            'salesman_manage_list', 'salesman_manage_create', 'salesman_manage_detail',
        ],
        'agent_manage': [
            'agent_manage_create', 'agent_manage_list',
            'agent_manage_edit'
        ],
        'settlement_manage': [
            'clearing_detail_list', 'clearing_detail_export',
            'clearing_summary_list', 'clearing_summary_total',
            'clearing_summary_export',
            # 'income_report_total',
            # 'income_report_export', 'payment_report_total',
            # 'payment_report_export',
            # 'income_report_list', 'payment_report_list',
            'clearing_template_create', 'clearing_template_config',
            'clearing_template_detail', 'clearing_template_edit',
            'clearing_template_list',
        ],
        'perm_manage': [
            'perm_user_list', 'perm_role_list', 'perm_role_create',
            'perm_role_edit', 'perm_user_create', 'perm_user_edit',
        ]
    }

    # 前端需要
    PERM_INDEX_MAP = {
        'mchnt_manage_list': ['2', '2-1'],
        'shop_manage_list': ['2', '2-2'],
        'mchnt_audit_list': ['2', '2-3'],
        'trade_detail_list': ['3', '3-1'],
        'trade_summary_list': ['3', '3-2'],
        'agent_manage_list': ['4', '4-1'],
        'clearing_detail_list': ['5', '5-1'],
        'clearing_summary_list': ['5', '5-2'],
        # 'income_report_list': ['5', '5-3'],
        # 'payment_report_list': ['5', '5-4'],
        'clearing_template_list': ['5', '5-5'],
        'perm_user_list': ['6', '6-1'],
        'perm_role_list': ['6', '6-2'],
        'salesman_manage_list': ['7', '7-1'],
    }

    # 名称映射 - 现在主要使用langconf
    # 在每次检测权限的时候会使用
    PERM_NAME_MAP = {

        # 商户管理权限
        'mchnt_manage_list': '商户管理',
        'mchnt_manage_create':  '创建商户',
        'mchnt_manage_batch_create':  '批量创建商户',

        # 业务员权限
        'salesman_manage_list': '业务员管理',
        'salesman_manage_create': '业务员创建',
        'salesman_manage_detail': '业务员详情',

        # 门店管理
        'shop_manage_list': '门店管理',
        'shop_manage_export': '门店信息导出',

        # 商户审核
        # 'mchnt_audit_list': '商户审核',

        # 交易
        'trade_detail_list': '交易明细',
        'trade_detail_export': '交易明细导出',
        'trade_summary_list': '交易汇总',

        # 代理商管理
        'agent_manage_list': '代理商列表',
        'agent_manage_create': '代理商创建',
        'agent_manage_edit': '代理商修改',

        # 清分
        'clearing_detail_list': '清分明细',
        'clearing_detail_export': '清分明细导出',
        'clearing_summary_list': '清分汇总',
        'clearing_summary_total': '清分汇总总计',
        'clearing_summary_export': '清分汇总导出',

        # 报表
        # 'income_report_list': '应收报表',
        # 'income_report_total': '应收报表总计',
        # 'income_report_export': '应收报表导出',
        # 'payment_report_list': '应付报表',
        # 'payment_report_total': '应付报表总计',
        # 'payment_report_export': '应付报表导出',

        # 清分模板
        'clearing_template_list': '清分模板',
        'clearing_template_create': '清分模板创建',
        'clearing_template_config': '清分模板配置',
        'clearing_template_detail': '清分模板明细',
        'clearing_template_edit': '清分模板修改',

        # 权限管理
        'perm_role_list': '角色管理',
        'perm_role_create': '权限角色创建',
        'perm_role_edit': '权限角色修改',
        'perm_user_list': '用户管理',
        'perm_user_create': '权限用户创建',
        'perm_user_edit': '权限有用户修改',
    }


BASE_UPDATE_FIELDS = ('slsm_uid',)
REGION_UPDATE_FIELDS = ('name', 'province', 'city', 'type', 'openness')
TRAINING_FILE_UPDATE_FIELDS = ('name', 'link', 'memo')

# profile 表可以修改的字段.
PROFILE_UPDATE_FIELDS = (
    'name', 'short_name', 'legal_name', 'legal_idnumber',
    'province', 'city', 'address',
    'business_name', 'business_mobile', 'business_email',
    'finance_name', 'finance_mobile', 'finance_email',
    'logo_url', 'icon_url', 'business_license_url', 'bank_account_url',
    'auth_province', 'auth_city',
    'manager_name', 'manager_mobile', 'service_manager_name', 'service_manager_mobile',
)

ACCOUNT_UPDATE_FIELDS = ('default_mchnt_fee', 'royalty_rule_id')

# apollo 中用户状态对应渠道状态的关系, 修改状态时使用
QUDAO_APOLLO_STATE_MAP = {
    ttypes.QudaoStatus.ENABLE: QF_USTATE_CANCEL,
    ttypes.QudaoStatus.DISABLE: QF_USTATE_CLOSE,
    ttypes.QudaoStatus.DELETED: QF_USTATE_DESTROY
}
# apollo 中用户状态对应渠道状态的关系, 展示时使用
APOLLO_QUDAO_STATE_MAP = {
    QF_USTATE_NEW: ttypes.QudaoStatus.ENABLE,
    QF_USTATE_VARIFIED: ttypes.QudaoStatus.ENABLE,
    QF_USTATE_ACTIVE: ttypes.QudaoStatus.ENABLE,
    QF_USTATE_OK: ttypes.QudaoStatus.ENABLE,
    QF_USTATE_CANCEL: ttypes.QudaoStatus.ENABLE,

    QF_USTATE_DULL: ttypes.QudaoStatus.DISABLE,
    QF_USTATE_FORBID: ttypes.QudaoStatus.DISABLE,
    QF_USTATE_DESTROY: ttypes.QudaoStatus.DELETED,
    QF_USTATE_CLOSE: ttypes.QudaoStatus.DISABLE,
}

# apollo 中用户状态对应商户状态的关系, 修改状态时使用
MCHNT_APOLLO_STATE_MAP = {
    ttypes.MchntStatus.ENABLE: QF_USTATE_OK,
    ttypes.MchntStatus.DISABLE: QF_USTATE_CLOSE,
}

# apollo 中用户状态对应业务员状态的关系, 修改状态时使用
SLSM_APOLLO_STATE_MAP = {
    ttypes.SlsmStatus.ENABLE: QF_USTATE_OK,
    ttypes.SlsmStatus.DISABLE: QF_USTATE_CLOSE,
}


# 商户状态, 0=正常, 1=注销
MCHNT_STATUS = {
    QF_USTATE_NEW: 0,
    QF_USTATE_VARIFIED: 0,
    QF_USTATE_ACTIVE: 0,
    QF_USTATE_OK: 0,
    QF_USTATE_DULL: 1,
    QF_USTATE_FORBID: 1,
    QF_USTATE_DESTROY: 1,
    QF_USTATE_CLOSE: 1,
}


# 下载渠道列表包含的字段
QUDAO_DOWNLOAD_FIELDS = (
    ('渠道编号', 'base.qd_uid'),
    ('渠道类型', 'base.type_desc'),
    ('渠道名称', 'base.name'),
    ('状态', 'base.status_desc'),
    ('法人姓名', 'base.legal_name'),
    ('法人身份证号', 'base.legal_idnumber'),
    ('手机号', 'base.mobile'),
    ('国家', 'base.country'),
    ('时区', 'base.timezone'),
    ('币种', 'base.currency'),
    ('省份', 'base.province'),
    ('市', 'base.city'),
    ('注册邮箱', 'base.email'),
    ('业务员手机号', 'base.slsm_mobile'),
    ('授权省份', 'base.auth_province'),
    ('授权城市', 'base.auth_city'),
    ('业务联系人', 'base.business_name'),
    ('业务手机号', 'base.business_mobile'),
    ('业务邮箱', 'base.business_email'),
    ('财务联系人', 'base.finace_name'),
    ('财务手机号', 'base.finace_mobile'),
    ('财务邮箱', 'base.finace_email'),
    ('商户地址', 'base.address'),
    ('收款人姓名', 'account.bankuser'),
    ('收款账号', 'account.bankaccount'),
    ('总行名称', 'account.headbankname'),
    ('支行名称', 'account.bankname'),
    ('结算类型', 'account.banktype_desc'),
    ('结算方式', 'account.settle_cycle_desc'),
    ('起结金额', 'account.settle_base_amt'),
    ('微信手续费', 'account.wechat_fee'),
    ('支付宝手续费', 'account.alipay_fee'),
    ('QQ钱包手续费', 'account.qqwallet_fee'),
    ('京东钱包手续费', 'account.jd_fee'),
    ('刷卡手续费', 'account.swipecard_fee'),
    ('商户默认手续费', 'account.default_mchnt_fee'),
)


# 下载业务员列表包含的字段
SLSM_DOWNLOAD_FIELDS = (
    ('业务员编号', 'slsm_uid'),
    ('业务员名称', 'name'),
    ('手机号', 'mobile'),
    ('状态', 'status_desc'),
    ('注册时间', 'jointime'),
)


class RESP_CODE(object):
    SUCCESS = '0000'  # 成功
    SYSTEM_ERROR = '1000'  # 系统错误
    USER_NOT_LOGIN = '1001'  # 用户未登录
    PARAM_ERROR = '1002'
    INNER_SERVICE_ERR = '1003'  # 内部系统错误
    DB_ERR = '1004'  # 数据库错误
    DATA_EXIST = '1005'  # 数据已存在
    DATA_NOT_EXIST = '1006'  # 数据不存在


# 退款相关busicd
REFUND_BUSICD_LIST = ('800103', '800203', '800304', '800403', '800503', '800603', '800703', '801003',
                      '801103', '801203', '801303', '801403', '801503', '801603', '801808', '801903')
ABROAD_REFUND_BUSICD_LIST = [QF_BUSICD_WEIXIN_HK_REFUND, QF_BUSICD_ALIPAY_ONLINE_REFUND, QF_BUSICD_ALIPAY_REFUND,
                             QF_BUSICD_WEIXIN_REFUND, QF_BUSICD_UNIONPAY_QRCODE_REFUND, QF_BUSICD_AIRPAY_REFUND]

# 所有关于冲正和取消操作和推出操作的BUSICD
NOT_NEED_BUSICD_LIST = (defines.QF_BUSICD_QUICK_CANCEL, defines.QF_BUSICD_ALIPAY_CANCEL,
                        defines.QF_BUSICD_ALIPAY_REVERSE, defines.QF_BUSICD_WEIXIN_CLOSE_ORDER,
                        defines.QF_BUSICD_WEIXIN_REVERSAL, defines.QF_BUSICD_BAIFUBAO_CLOSE_ORDER,
                        defines.QF_BUSICD_BAIFUBAO_REVERSAL, defines.QF_BUSICD_UNIONPAY_QRCODE_REVERSAL,
                        defines.QF_BUSICD_WEIXIN_HK_CLOSE_ORDER, defines.QF_BUSICD_WEIXIN_HK_REVERSAL,
                        defines.QF_BUSICD_ALIPAY_OVERSEAS_PREAUTH_CANCEL,
                        defines.QF_BUSICD_ALIPAY_OVERSEAS_PREAUTH_UNFREEZE,
                        defines.QF_BUSICD_ALIPAY_OVERSEAS_PREAUTH_QUERY)


class MchntDef(object):
    '''商户常量定义'''

    # 审核状态
    AUDIT_STATUS_ING = -1
    AUDIT_STATUS_REFUSE = 0
    AUDIT_STATUS_SUCC = 1
    AUDIT_STATUS_FAIL = 2
    AUDIT_STATUS_MAP = {
        AUDIT_STATUS_ING : '审核中',
        AUDIT_STATUS_REFUSE : '审核拒绝',
        AUDIT_STATUS_SUCC : '审核成功',
        AUDIT_STATUS_FAIL : '审核失败'
    }
    # 商户列表和商户详情商户状态
    MCHNT_STATUS_OPEN = 3       # 启用
    MCHNT_STATUS_CLOSE = 4      # 禁用

    # mchnt_user商户状态
    MCHNT_USER_STATUS_OPEN = 0  # 启用
    MCHNT_USER_STATUS_CLOSE = 1  # 禁用


class ApplyDef(object):
    '''审核定义'''

    STATE_PASS = 5 # 审核通过
    STATE_FAIL = 8 # 审核失败

    # 凭证状态
    VOUCHER_STATE_WAIT = 0 # 待审
    VOUCHER_STATE_PASS = 1 # 通过
    VOUCHER_STATE_FAIL = 2 # 未通过

    # auditlog result
    AUDIT_RESULT_REJECT = 0 # 审核拒绝
    AUDIT_RESULT_PASS = 1 # 审核成功
    AUDIT_RESULT_FAIL = 2 # 审核失败
    AUDIT_RESULT_MAP = {
        AUDIT_RESULT_REJECT  : '审核拒绝',
        AUDIT_RESULT_PASS : '审核成功',
        AUDIT_RESULT_FAIL : '审核失败'
    }


class BatchCreateDef(object):
    """商户批量入网相关参数(新加坡版本)"""

    # 商户批量入网表头和参数的对应关系
    BATCH_EXCEL_FIELDS = [
        {'Salesperson Contact Number': 'mobile'},
        {'Merchant Category': 'cate'},
        {'Merchant Name': 'shopname'},
        {'Industry': 'mcc'},
        {'Description': 'memo'},
        {'Agreement Signed (Yes/No)': 'is_contract'},
        {'Settlement Period': 'settlement_time'},
        {'MDR(%)': 'ratio'},
        {'Company Name': 'name'},
        {'Business Registration Number': 'licensenumber'},
        {'Area': 'location'},
        {'Address': 'address'},
        {'Post Code': 'post'},
        {'Contact Name': 'legalperson'},
        {'Contact Number': 'telephone'},
        {'E-mail Address': 'email'},
        {'Bank Name': 'headbankname'},
        {'Swift Code': 'bankcode'},
        {'Bank Account Name': 'bankuser'},
        {'Bank Account Number': 'bankaccount'},
        {'Branch Name': 'bankname'},
        {'Store Name': 'storename'},
        {'Store Contact Number': 'storetelephone'},
        {'Store Area': 'storelocation'},
        {'Store Address': 'storeaddress'},
        {'Store Post Code': 'storepost'},
        {'Business Hours': 'storeoperating'},
        {'Website': 'website'},
        {'Additional Services': 'storeadditional'},
    ]

    # 商户批量入网 cate 字段对应
    CATE = {'Chain Merchant': 'bigmerchant', 'Merchant': 'merchant'}

    # 商户批量入网 is_contract 字段对应
    IS_CONTRACT = {'Yes': 1, 'No': 0}

    # 商户批量入网 settlement_time 字段对应
    SETTLEMENT_TIME = {'Daily': 'date', 'Weekly': 'week', 'Monthly': 'month'}

    # 商户批量入网 location 字段对应
    LOCATION = {'Singapore': 'SG', 'Malaysia': 'MY'}


# 一级mcc参数名称
PRIMARY_MCC = [
    {'id': 1, 'name': 'Clothing', 'display': 1},
    {'id': 2, 'name': '3C home appliances', 'display': 1},
    {'id': 3, 'name': 'Beauty & make up、Fitness & Health', 'display': 1},
    {'id': 4, 'name': 'Direct sellin', 'display': 1},
    {'id': 5, 'name': 'Office supplies & printing', 'display': 1},
    {'id': 6, 'name': 'Furniture for home building materials', 'display': 1},
    {'id': 7, 'name': 'Business services、Adult education', 'display': 1},
    {'id': 8, 'name': 'Life service', 'display': 1},
    {'id': 9, 'name': 'Luggage and leather accessories', 'display': 1},
    {'id': 10, 'name': 'Food、beverage、tobacco and alcohol retail', 'display': 1},
    {'id': 11, 'name': 'Leisure sports culture', 'display': 1},
    {'id': 12, 'name': 'Grocery supermarket', 'display': 1},
    {'id': 13, 'name': 'Entertainment、leisure and vacation', 'display': 1},
    {'id': 14, 'name': 'Cars and bicycles', 'display': 1},
    {'id': 15, 'name': 'Jewelry craft、antique flower and bird', 'display': 1},
    {'id': 16, 'name': 'Lottery ticket recharging ticketing Tour', 'display': 1},
    {'id': 17, 'name': 'Pharmacy and medical services', 'display': 1},
    {'id': 18, 'name': 'Logistics and leasing', 'display': 1},
    {'id': 19, 'name': 'Public welfare', 'display': 1},
    {'id': 20, 'name': 'Merchants in non fixed places', 'display': 1},
    {'id': 21, 'name': 'Qfpay & partner', 'display': 1},
    {'id': 22, 'name': 'Quanjian', 'display': 1},
]


class BatchCreateHKDef(object):
    """商户批量入网相关参数(香港版本)"""

    # 商户批量入网表头和参数的对应关系
    BATCH_EXCEL_FIELDS = [
        {'业务员账号': 'mobile'},
        {'商户类型': 'cate'},
        {'商户名称': 'shopname'},
        {'邮箱': 'email'},
        {'联系人姓名': 'legalperson'},
        {'联系电话': 'telephone'},
        {'证件类型': 'document_type'},
        {'证件编号': 'document_code'},
        {'行业类别': 'mcc'},
        {'商户地址': 'address'},
        {'BR编号': 'br'},
        {'BR有效期': 'br_expire_time'},
        {'CI编号': 'ci'},
        {'CI有效期': 'ci_expire_time'},
        {'通道费率(%)': 'ratio'},
        {'开户名称': 'bankuser'},
        {'开户行': 'headbankname'},
        {'银行账号': 'bankaccount'},
        {'银行地址': 'bankProvince'},
        {'结算资金起点': 'remit_amt'},
        {'门店名称': 'storename'},
        {'门店地址': 'storeaddress'},
        {'门店联系电话': 'storetelephone'},
        {'门店营业时间': 'operating'},
    ]

    # 商户批量入网 cate 字段对应
    CATE = {'连锁店': 'bigmerchant', '单店': 'merchant'}

    # 商户批量入网 证件类型 字段对应
    DOCUMENT_TYPE = {'护照': 'passport', '港澳通行证': 'eep', '香港居民证': 'idnumber'}
