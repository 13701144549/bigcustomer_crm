# coding: utf-8
import os, sys

# 正常
QF_OK                               = "0000"
# 系统维护
QF_ERR_MAINTEN                      = "1100"
# 需要主动冲正
QF_ERR_REVERSAL                     = "1101"
# 重复请求
QF_ERR_REPEAT                       = "1102"
# 报文格式错误
QF_ERR_JSON                         = "1103"
# 报文参数错误
QF_ERR_JSON_PARAM                   = "1104"
# 终端未激活
QF_ERR_TERM_NOTACTIVE               = "1105"
# 终端不匹配
QF_ERR_TERM_NOTMATCH                = "1106"
# 终端被封禁
QF_ERR_TERM_DENY                    = "1107"
# MAC校验失败
QF_ERR_MAC                          = "1108"
# 加解密错误
QF_ERR_CRYPT                        = "1109"
# 客户端重置，流水号错
QF_ERR_CLIENT_RESET                 = "1110"
# 外部服务不可用
QF_ERR_SERVICE_OUT                  = "1111"
# 内部服务不可用
QF_ERR_SERVICE_IN                   = "1112"
# 用户不存在
QF_ERR_USER_NOTEXIST                = "1113"
# 用户被封禁
QF_ERR_USER_DENY                    = "1114"
# 用户受限
QF_ERR_USER_LIMIT                   = "1115"
# 用户密码错误
QF_ERR_USER_PASS                    = "1116"
# 用户不在线
QF_ERR_USER_OFFLINE                 = "1117"
# 风控禁止交易
QF_ERR_RISK                         = "1118"
# 交易类型受限
QF_ERR_TRADE_TYPE                   = "1119"
# 交易时间受限
QF_ERR_TRADE_TIME                   = "1120"
# 交易卡类型受限
QF_ERR_TRADE_CARD                   = "1121"
# 交易币种受限
QF_ERR_TRADE_CURRENCY               = "1122"
# 交易额度受限
QF_ERR_TRADE_AMOUNT                 = "1123"
# 无效交易
QF_ERR_TRADE                        = "1124"
# 已退货
QF_ERR_REFUNDED                     = "1125"
# 原交易信息不匹配
QF_ERR_ORIG_TRADE                   = "1126"
# 数据库错误
QF_ERR_DB                           = "1127"
# 文件系统错误
QF_ERR_FS                           = "1128"
# 已上传凭证
QF_ERR_UPLOADED                     = "1129"
# 交易不在允许日期
QF_ERR_OUT_OF_DATE                  = "1130"
# 渠道错误
QF_ERR_CHANNEL_TIMEOUT              = "1131"
# 客户端版本信息错误
QF_ERR_CLIENT_VERSION               = "1132"
# 用户渠道信息错误
QF_ERR_CHANNEL_INFO                 = "1133"
# 撤销交易刷卡与消费时不是同一张卡
QF_ERR_DIFF_CARD                    = "1134"
# 用户配置错误
QF_ERR_USER_SETTING                 = "1135"
# 交易不存在
QF_ERR_TRADE_NOT_EXIST              = "1136"
# 联系方式不存在
QF_ERR_TRADE_NO                     = "1137"
# 用户更新密钥错
QF_ERR_UPDATE_KEYS                  = "1138"
# 卡号或者卡磁错误
QF_ERR_CARD                         = "1139"
# 账户未审核通过
QF_ERR_USER_NOT_VARIFIED            = "1140"
# 计算通道MAC错误
QF_ERR_CHANNEL_MAC                  = "1141"

# 订单已关闭
QF_ERR_ORDER_CLOSE                  = "1142"
# 交易不存在
QF_ERR_ORDER_NOT_EXIST              = "1143"
# 请求处理失败(协议)
QF_ERR_ORDER_FAIL                   = "1144"
# 订单状态等待支付
QF_ERR_ORDER_WAIT_PAY               = "1145"
## 订单业务处理结果未知
#QF_ERR_ORDER_UNKOWN                 = "1146"
# 订单处理业务错误
QF_ERR_ORDER_TRADE_FAIL             = "1146"
# 通道加密磁道错误
QF_ERR_CHANNEL_TRACK                = "1141"
# 微信刷卡失败
QF_ERR_WEIXIN_PAY_ERROR             = "1147"

# 钱方账户系统错误
QF_ERR_QFACCOUNT                    = "1148"
# 开放接口受限
QF_ERR_OPENAPI_LIMIT                = "1149"

#机构不存在
QF_ERR_ORG_NOTEXIST                 = "2001"
#商户绑定失败
QF_ERR_ORG_MCHNT_BIND_ERROR         = "2002"
#签到失败
QF_ERR_ORG_SIGNIN_ERROR             = "2003"

### 海外版支付系统增加 ####
# 消费者余额不足
QF_ERR_CUSTOMER_NOT_ENOUGH          = "2004"
# 消费者二维码过期
QF_ERR_CUSTOMER_QR_EXPIRE           = "2005"
# 消费者二维码非法
QF_ERR_CUSTOMER_QR_INVALID          = "2006"
# 消费者关闭了这次交易
QF_ERR_CUSTOMER_CANCEL              = "2007"
# 传递给通道的参数错误
QF_ERR_TO_CHNL_PARAM                = "2008"
# 连接通道失败
QF_ERR_TO_CHNL_CONNECT              = "2009"
# 和通道交互的未知错误
QF_ERR_TO_CHNL_UNKOWN               = "2010"
# 交易流水号重复
QF_ERR_SYSSN_USED                   = "2011"
# 用户的通道证书配置错误
QF_ERR_USER_CERT                    = "2012"

# 原预授权信息不匹配
QF_ERR_ORIG_PAUTH                   = "1151"
# 预授权完成不在允许日期
QF_ERR_PAUTHCP_OUT_OF_DATE          = "1152"
# 预授权完成金额错误
QF_ERR_PAUTHCP_AMOUNT               = "1153"
# 内部错误
QF_ERR_INTERNAL                     = "1154"
# 不允许撤销的交易
QF_ERR_REFUND_DENY                  = "1155"
# 交易结果未知，须查询
QF_ERR_CHANNEL_QUERY                = "1161"
# channeld不能提供服务
QF_ERR_CHANNELD_SHUTDOWN            = "1170"
# 路由重置，需重新路由
QF_ERR_ROUTE_AGAIN                  = "1180"

# 订单过期
QF_ERR_ORDER_EXPIRED                = "1181"


#####  无卡部分错误码 没有NOCARD的以后避免使用
# 120* 121* 通道的错误转换
# 124* 用户相关错误
# 125* 内部错误
# 126* 订单错误
# 129* 通道故障错误

# 余额不足
QF_ERR_NOCARD_NOT_ENOUGH            = "1201"
QF_ERR_NOT_ENOUGH                   = "1201"
# 付款码错误
QF_ERR_NOCARD_AUTH_CODE             = "1202"
QF_ERR_AUTH_CODE                    = "1202"
# 账户错误
QF_ERR_NOCARD_ACCOUNT               = "1203"
QF_ERR_ACCOUNT                      = "1203"
# 银行错误
QF_ERR_NOCARD_BANK                  = "1204"
QF_ERR_BANK                         = "1204"
# 银联付款码类型错误
QF_ERR_UNIONPAY_AUTH_CODE_TYPE      = "1212"
# 用户不存在
QF_ERR_NOCARD_USER_NOT_EXIST        = "1241"
# 用户通道配置错误
QF_ERR_NOCARD_USER_NO_CHANNEL       = "1242"
# 用户禁用
QF_ERR_NOCARD_USER_DENY             = "1243"
# 交易不允许
QF_ERR_NOCARD_LIMIT_BUSICD          = "1250"
# 参数错误
QF_ERR_NOCARD_PARAMS                = "1251"
# 创建订单错误
QF_ERR_NOCARD_SYSSN                 = "1252"
# 内部系统错误
QF_ERR_NOCARD_SYSTEM_ERROR          = "1254"
# 订单已支付
QF_ERR_NOCARD_ORDER_PAIED           = "1260"
# 订单未支付
QF_ERR_NOCARD_ORDER_NOTPAY          = "1261"
# 订单已经退款
QF_ERR_NOCARD_ORDER_REFUNDED        = "1262"
# 订单已经关闭
QF_ERR_NOCARD_ORDER_CLOSED          = "1263"
# 订单已经撤销
QF_ERR_NOCARD_ORDER_CANCELED        = "1264"
# 订单禁止退款
QF_ERR_NOCARD_ORDER_LIMIT_REFUND    = "1265"
# 订单金额错误
QF_ERR_NOCARD_ORDER_AMT             = "1266"
# 订单不匹配
QF_ERR_NOCARD_ORDER_NOT_MATCH       = "1267"
# 订单不存在
QF_ERR_NOCARD_ORDER_NOT_EXIST       = "1268"
# 未结算金额不足
QF_ERR_NOCARD_UNSETTLED_AMOUNT_NOT_ENOUGH       = "1269"
# 该币种不支持部分退款
QF_ERR_NOCARD_CURRENCY_LIMIT_PART_REFUND        = "1270"
# 该通道不支持部分退款
QF_ERR_NOCARD_CHANNEL_LIMIT_PART_REFUND         = '1271'
# 通道风控
QF_ERR_NOCARD_CHANNEL_RISK          = "1294"
# 通道签名校验错误
QF_ERR_NOCARD_CHANNEL_MAC           = "1295"
# 通道系统错误
QF_ERR_NOCARD_CHANNEL_SYSTEMERROR   = "1296"
# 通道未知错误
QF_ERR_NOCARD_CHANNEL_UNKNOW        = "1297"
# 通道超时
QF_ERR_NOCARD_CHANNEL_TIMEOUT       = "1298"

err_state = {
    QF_OK                             : u'正常',
    QF_ERR_MAINTEN                    : u'系统维护',
    QF_ERR_REVERSAL                   : u'需要主动冲正',
    QF_ERR_REPEAT                     : u'重复请求',
    QF_ERR_JSON                       : u'报文格式错误',
    QF_ERR_JSON_PARAM                 : u'报文参数错误',
    QF_ERR_TERM_NOTACTIVE             : u'终端未激活',
    QF_ERR_TERM_NOTMATCH              : u'终端不匹配',
    QF_ERR_TERM_DENY                  : u'终端被封禁',
    QF_ERR_MAC                        : u'MAC校验失败',
    QF_ERR_CRYPT                      : u'加解密错误',
    QF_ERR_CLIENT_RESET               : u'客户端重置，流水号错',
    QF_ERR_SERVICE_OUT                : u'外部服务不可用',
    QF_ERR_SERVICE_IN                 : u'内部服务不可用',
    QF_ERR_USER_NOTEXIST              : u'用户不存在',
    QF_ERR_USER_DENY                  : u'用户被封禁',
    QF_ERR_USER_LIMIT                 : u'用户受限',
    QF_ERR_USER_PASS                  : u'用户密码错误',
    QF_ERR_USER_OFFLINE               : u'用户不在线',
    QF_ERR_OPENAPI_LIMIT              : u'接口受限',
    QF_ERR_RISK                       : u'风控禁止交易',
    QF_ERR_TRADE_TYPE                 : u'交易类型受限',
    QF_ERR_TRADE_TIME                 : u'交易时间受限',
    QF_ERR_TRADE_CARD                 : u'交易卡类型受限',
    QF_ERR_TRADE_CURRENCY             : u'交易币种受限',
    QF_ERR_TRADE_AMOUNT               : u'交易额度受限',
    QF_ERR_TRADE                      : u'无效交易',
    QF_ERR_REFUNDED                   : u'已退货',
    QF_ERR_ORIG_TRADE                 : u'原交易信息不匹配',
    QF_ERR_DB                         : u'数据库错误',
    QF_ERR_FS                         : u'文件系统错误',
    QF_ERR_UPLOADED                   : u'已上传凭证',
    QF_ERR_OUT_OF_DATE                : u'交易不在允许日期',
    QF_ERR_CHANNEL_TIMEOUT            : u'渠道错误',
    QF_ERR_CLIENT_VERSION             : u'客户端版本信息错误',
    QF_ERR_CHANNEL_INFO               : u'用户渠道信息错误',
    QF_ERR_DIFF_CARD                  : u'撤销交易刷卡与消费时不是同一张卡',
    QF_ERR_USER_SETTING               : u'用户配置错误',
    QF_ERR_TRADE_NOT_EXIST            : u'交易不存在',
    QF_ERR_TRADE_NO                   : u'联系方式不存在',
    QF_ERR_UPDATE_KEYS                : u'用户更新密钥错',
    QF_ERR_CARD                       : u'卡号或者卡磁错误',
    QF_ERR_USER_NOT_VARIFIED          : u'账户未审核通过',
    QF_ERR_CHANNEL_MAC                : u'计算通道MAC错误'  ,
    QF_ERR_ORDER_CLOSE                : u'订单已关闭',
    QF_ERR_ORDER_NOT_EXIST            : u'订单不存在',
    QF_ERR_ORDER_FAIL                 : u'协议处理失败',
    QF_ERR_ORDER_WAIT_PAY             : u'订单已创建等待支付完成',
    QF_ERR_ORDER_TRADE_FAIL           : u'订单业务处理失败',
    QF_ERR_ORIG_PAUTH                 : u'原预授权信息不匹配',
    QF_ERR_PAUTHCP_OUT_OF_DATE        : u'预授权完成不在允许日期',
    QF_ERR_PAUTHCP_AMOUNT             : u'预授权完成金额错误',
    QF_ERR_INTERNAL                   : u'内部错误',
    QF_ERR_REFUND_DENY                : u'交易不能撤销',
    QF_ERR_CHANNEL_QUERY              : u'交易结果未知，须查询',
    QF_ERR_CHANNELD_SHUTDOWN          : u'channeld不能提供服务',
    QF_ERR_ROUTE_AGAIN                : u'路由重置，需重新路由',
    QF_ERR_ORDER_EXPIRED              : u'订单过期',
    QF_ERR_WEIXIN_PAY_ERROR           : u"微信刷卡失败，需要重新刷卡",
    QF_ERR_ORG_NOTEXIST               : u"机构不存在",
    QF_ERR_ORG_MCHNT_BIND_ERROR       : u"商户绑定失败",
    QF_ERR_ORG_SIGNIN_ERROR           : u"签到失败",
    QF_ERR_NOCARD_NOT_ENOUGH          : u'余额不足',
    QF_ERR_NOCARD_AUTH_CODE           : u'付款码错误',
    QF_ERR_NOCARD_ACCOUNT             : u'账户错误',
    QF_ERR_NOCARD_BANK                : u'银行错误',
    QF_ERR_NOCARD_USER_NOT_EXIST      : u'用户不存在',
    QF_ERR_NOCARD_USER_NO_CHANNEL     : u'商户没有配置通道',
    QF_ERR_NOCARD_USER_DENY           : u'用户被禁用',
    QF_ERR_NOCARD_LIMIT_BUSICD        : u'交易类型受限',
    QF_ERR_NOCARD_PARAMS              : u'参数错误',
    QF_ERR_NOCARD_SYSSN               : u'创建流水号错误',
    QF_ERR_NOCARD_SYSTEM_ERROR        : u'内部系统错误',
    QF_ERR_NOCARD_ORDER_PAIED         : u'订单已支付',
    QF_ERR_NOCARD_ORDER_NOTPAY        : u'订单未支付',
    QF_ERR_NOCARD_ORDER_REFUNDED      : u'订单已退款',
    QF_ERR_NOCARD_ORDER_CLOSED        : u'订单已关闭',
    QF_ERR_NOCARD_ORDER_CANCELED      : u'订单已撤销',
    QF_ERR_NOCARD_ORDER_LIMIT_REFUND  : u'订单被限制撤销',
    QF_ERR_NOCARD_ORDER_AMT           : u'订单金额不正确',
    QF_ERR_NOCARD_ORDER_NOT_MATCH     : u'订单信息不匹配',
    QF_ERR_NOCARD_ORDER_NOT_EXIST     : u'订单不存在',
    QF_ERR_NOCARD_CHANNEL_MAC         : u'通道校验签名错误',
    QF_ERR_NOCARD_CHANNEL_SYSTEMERROR : u'通道系统错误',
    QF_ERR_NOCARD_CHANNEL_UNKNOW      : u'通道未知错误',
    QF_ERR_NOCARD_CHANNEL_TIMEOUT     : u'通道超时',
    QF_ERR_NOCARD_CHANNEL_RISK        : u'通道风控',
    QF_ERR_NOCARD_UNSETTLED_AMOUNT_NOT_ENOUGH: u'当日未结算金额不足',
    QF_ERR_NOCARD_CURRENCY_LIMIT_PART_REFUND: u'该币种不支持部分退款',
    QF_ERR_NOCARD_CHANNEL_LIMIT_PART_REFUND: u'该通道不支持部分退款',
    QF_ERR_UNIONPAY_AUTH_CODE_TYPE    : u'银联付款码类型错误',
}

# ---- 内部错误代码 ----
QF_PAY_OK                           = 0
QF_PAY_ERR                          = -1
QF_PAY_ERR_JSON                     = -2
QF_PAY_ERR_CONNECT                  = -11
QF_PAY_ERR_READ                     = -12
QF_PAY_ERR_WRITE                    = -13
QF_PAY_ERR_TIMEOUT                  = -14
QF_PAY_ERR_NETWORK                  = -15
QF_PAY_ERR_RISK                     = -16
QF_PAY_ERR_THRIFT                   = -17
QF_PAY_ERR_NOSERVER                 = -18
QF_PAY_ERR_TRADENOOUT               = -19
QF_PAY_ERR_PARA                     = -20
QF_PAY_ERR_MEMORY                   = -21


# ----  用户状态 ----
# 新建
QF_USTATE_NEW                       = 1
# 通过审核, 未设备激活
QF_USTATE_VARIFIED                  = 2
# 已设备激活，未业务激活
QF_USTATE_ACTIVE                    = 3
# 已业务激活，正常
QF_USTATE_OK                        = 4
# 呆户
QF_USTATE_DULL                      = 5
# 临时封禁，黑名单
QF_USTATE_FORBID                    = 6
# 永久封禁
QF_USTATE_DESTROY                   = 7
# 用户主动注销
QF_USTATE_CLOSE                     = 8
# 临时停用(主要渠道用)
QF_USTATE_CANCEL                    = 9

# ---- 订单状态 ----
# 订单创建
QF_ORDER_CREATED                    = 1
# 订单支付中
QF_ORDER_PAYING                     = 2
# 订单支付成功
QF_ORDER_PAY_SUCCESS                = 3
# 订单支付失败
QF_ORDER_PAY_FAIL                   = 4
# 订单关闭
QF_ORDER_CLOSE                      = 5
# 订单过期
QF_ORDER_EXPIRED                    = 6
# 定单撤销
QF_ORDER_CANCEL                     = 7

order_state = {
    QF_ORDER_CREATED: u'订单创建',
    QF_ORDER_PAYING: u'支付中',
    QF_ORDER_PAY_SUCCESS: u'支付成功',
    QF_ORDER_PAY_FAIL: u'支付失败',
    QF_ORDER_CLOSE: u'订单关闭',
    QF_ORDER_EXPIRED: u'订单过期',
}

# ------订单支付方式----
#刷卡支付
QF_ORDER_PAY_METHOD_CARD            = 1
#支付宝
QF_ORDER_PAY_METHOD_ALIPAY          = 2
#微信
QF_ORDER_PAY_METHOD_WEIXIN          = 3
#百付宝
QF_ORDER_PAY_METHOD_BAIFUBAO        = 4

# ---- 设备绑定状态 ----
# 未激活
QF_DSTATE_NOACTIVE                  = 1
# 正常
QF_DSTATE_OK                        = 2
# 激活失败
QF_DSTATE_ACT_ERR                   = 3
# 失效
QF_DSTATE_NOTVALID                  = 4

term_state = {
    QF_DSTATE_NOACTIVE: u'未激活',
    QF_DSTATE_OK: u'已激活',
    QF_DSTATE_ACT_ERR: u'激活失败',
    QF_DSTATE_NOTVALID: u'已失效',
}

# ---- 交易类型 ----
# POSP消费收款(消费，撤销，退货，余额查询)
QF_TRADE_TYPE_POSP                  = 0x01
# 支付宝
QF_TRADE_TYPE_ALIPAY                = 0x02
# 支付宝(海外 需要钱方转汇率)
QF_TRADE_TYPE_ALIPAY_OVERSEAS       = 0x03
# 支付宝(海外 通道支持使用外币交易)
QF_TRADE_TYPE_ALIPAY_OVERSEAS_ATUO_EXCHANGE     = 0x05
# 支付宝海外线上
QF_TRADE_TYPE_ALIPAY_ONLINE         = 0x06
# 便民(转帐, 还款，缴费，充值)
QF_TRADE_TYPE_TRANSFER              = 0x04
# 香港微信
QF_TRADE_TYPE_WEIXIN_HK             = 0x07
# 微信
QF_TRADE_TYPE_WEIXIN                = 0x08
# 微信(海外 需要钱方转汇率)
QF_TRADE_TYPE_WEIXIN_OVERSEAS       = 0x09
# 微信(海外 通道支持使用外币交易)
QF_TRADE_TYPE_WEIXIN_OVERSEAS_ATUO_EXCHANGE     = 0x0A
# 百付宝
QF_TRADE_TYPE_BAIFUBAO              = 0x10
# 百付宝(海外 需要钱方转汇率)
QF_TRADE_TYPE_BAIFUBAO_OVERSEAS     = 0x11
# 百付宝(海外 通道支持使用外币交易)
QF_TRADE_TYPE_BAIFUBAO_OVERSEAS_ATUO_EXCHANGE   = 0x12
# 京东钱包 只能硬着头皮塞了
QF_TRADE_TYPE_JDPAY                 = 0x0B
# 微信APP
QF_TRADE_TYPE_WEIXIN_APP            = 0x0C
# QQ钱包
QF_TRADE_TYPE_QQPAY                 = 0x0D
# 银联二维码
QF_TRADE_TYPE_UNIONPAY_QRCODE       = 0x0E
# 会员储值
QF_TRADE_TYPE_PREPAID               = 0x1F
# 预授权
QF_TRADE_TYPE_PAUTH                 = 0x20
# 快捷支付
QF_TRADE_TYPE_QUICK                 = 0x21
# 网关支付
QF_TRADE_TYPE_GATEWAYPAY            = 0x22
# 翼支付
QF_TRADE_TYPE_BESTPAY               = 0x23
# 现金
QF_TRADE_TYPE_CASH                  = 0x40
# 管理
QF_TRADE_TYPE_MANAGE                = 0x80
# 代付
QF_TRADE_TYPE_CASHDRAW              = 0x90
# LINE PAY
QF_TRADE_TYPE_LINEPAY               = 0x24
# LINE PAY ONLINE
QF_TRADE_TYPE_LINEPAY_ONLINE        = 0x25
# UPI PAY
QF_TRADE_TYPE_UPI                   = 0x26
# AIR PAY
QF_TRADE_TYPE_AIRPAY                = 0x27
# 微信小程序交易类型
QF_TRADE_TYPE_WEIXIN_MAPP           = 0x28
# 支付宝香港线上
QF_TRADE_TYPE_ALIPAY_HK             = 0x29


trade_type = {
    QF_TRADE_TYPE_POSP: u'POSP消费',
    QF_TRADE_TYPE_ALIPAY: u'支付宝',
    QF_TRADE_TYPE_ALIPAY_ONLINE: u'支付宝线上',
    QF_TRADE_TYPE_TRANSFER: u'便民',
    QF_TRADE_TYPE_WEIXIN: u'微信',
    QF_TRADE_TYPE_WEIXIN_APP: u'微信APP',
    QF_TRADE_TYPE_JDPAY: u'京东钱包',
    QF_TRADE_TYPE_QQPAY: u'QQ钱包',
    QF_TRADE_TYPE_UNIONPAY_QRCODE: u'银联二维码',
    QF_TRADE_TYPE_PAUTH: u'预授权',
    QF_TRADE_TYPE_CASH: u'现金',
    QF_TRADE_TYPE_MANAGE: u'管理',
    QF_TRADE_TYPE_BAIFUBAO: u'百付宝',
    QF_TRADE_TYPE_WEIXIN_OVERSEAS: u'微信海外支付c方案',
    QF_TRADE_TYPE_WEIXIN_OVERSEAS_ATUO_EXCHANGE: u'微信海外支付ab方案',
    QF_TRADE_TYPE_PREPAID: '会员储值',
    QF_TRADE_TYPE_QUICK: u'快捷支付',
    QF_TRADE_TYPE_CASHDRAW: u'代付',
    QF_TRADE_TYPE_WEIXIN_HK: u"微信香港",
    QF_TRADE_TYPE_LINEPAY: u'LINE PAY',
    QF_TRADE_TYPE_LINEPAY_ONLINE: u'LINE PAY ONLINE',
    QF_TRADE_TYPE_UPI: u'UPI PAY',
    QF_TRADE_TYPE_AIRPAY: u'AIR PAY',
    QF_TRADE_TYPE_WEIXIN_MAPP: u'微信小程序',
    QF_TRADE_TYPE_ALIPAY_HK: u'ALIPAY HK',
}

# ---- 交易分类 ----
# 交易类
QF_TRADE_CLASS_PAYMENT              = 0x01
# 冲正类
QF_TRADE_CLASS_REVERSAL             = 0x02
# 撤销类
QF_TRADE_CLASS_CANCEL               = 0x04
# 查询类
QF_TRADE_CLASS_BALANCE              = 0x08
# 其他
QF_TRADE_CLASS_OTHER                = 0x10

# ---- 交易时间 ----
# 8 - 20点
QF_TRADE_TIME_8TO20                 = 0x01
# 20 - 0点
QF_TRADE_TIME_20TO0                 = 0x02
# 0 - 8点
QF_TRADE_TIME_0TO80                 = 0x04

# ---- 业务代码 ----
# 转账
QF_BUSICD_TOCARD                        =   "420000"
# 还款
QF_BUSICD_TOCREDIT                      =   "401000"
# 充值
QF_BUSICD_RECHARGE                      =   "500000"
# 消费
QF_BUSICD_PAYMENT                       =   "000000"
# 消费冲正
QF_BUSICD_REVERSAL                      =   "040000"
# 退货
QF_BUSICD_REFUND                        =   "200000"
# 余额查询
QF_BUSICD_BALANCE                       =   "300000"
# 上传凭证
QF_BUSICD_UPLOAD                        =   "180100"
# 交易列表
QF_BUSICD_TRADELIST                     =   "180200"
# 交易详情
QF_BUSICD_TRADEINFO                     =   "180300"
# 发送收据
QF_BUSICD_RECEIPT                       =   "180400"
# 交易查询
QF_BUSICD_TRADEQUERY                    =   "180600"
# 初始化
QF_BUSICD_INIT                          =   "170100"
# 激活
QF_BUSICD_ACTIVE                        =   "170200"
# 登录
QF_BUSICD_LOGIN                         =   "170300"
# 统计
QF_BUSICD_STAT                          =   "170500"
# 反馈
QF_BUSICD_FEED                          =   "170600"
# 修改密码
QF_BUICD_CHPASS                         =   "170700"
# 更新密钥
QF_BUICD_UPDATEKEYS                     =   "170800"
# 消费撤销
QF_BUSICD_CANCEL                        =   "201000"
# 消费撤销冲正
QF_BUSICD_CANCEL_REVERSAL               =   "041000"
# 现金记账
QF_BUSICD_CASH                          =   "180500"
# 订单支付
QF_BUSICD_ORDER_PAY                     =   "181000"
QF_BUSICD_ORDER_CREATE                  =   "181001"
QF_BUSICD_ORDER_QUERY                   =   "181002"
QF_BUSICD_ORDER_CLOSE                   =   "181003"
QF_BUSICD_ORDER_CANCEL                  =   "181004"
# IC卡脚本通知
QF_BUSICD_ICNOTICE                      =   "210000"
# 预授权
QF_BUSICD_PAUTH                         =   "032000"
# 预授权冲正
QF_BUSICD_PAUTH_REVERSAL                =   "042000"
# 预授权撤销
QF_BUSICD_PAUTH_CANCEL                  =   "202000"
# 预授权撤销冲正
QF_BUSICD_PAUTH_CANCEL_REVERSAL         =   "044000"
# 预授权完成
QF_BUSICD_PAUTHCP                       =   "033000"
# 预授权完成冲正
QF_BUSICD_PAUTHCP_REVERSAL              =   "043000"
# 预授权完成撤销
QF_BUSICD_PAUTHCP_CANCEL                =   "203000"
# 预授权完成撤销冲正
QF_BUSICD_PAUTHCP_CANCEL_REVERSAL       =   "045000"
# 管理类报文
QF_BUSICD_MANAGE                        =   "800000"
# 密码更新报文
QF_BUSICD_SECRET                        =   "820000"
# 烟草订购
QF_BUSICD_BACOO_ORDER                   =   "182000"
# 烟草消费
#QF_BUSICD_BACCO_PAYMENT                 =   "000000"

# 7开头内部系统业务
# 储值消费
QF_BUSICD_PREPAID_CONSUME               = "700000"
# 储值查询
QF_BUSICD_PREPAID_QUERY                 = "700001"
# 储值退款
QF_BUSICD_PREPAID_REFUND                = "700002"
# 储值付款码支付
QF_BUSICD_PREPAID_SWIPE                 = "700003"


#### 快捷支付 ####
# 快捷支付-普通支付
QF_BUSICD_QUICK_PAY                     = "700101"
# 快捷支付-发送短信验证码
QF_BUSICD_QUICK_SENDSMS                 = "700102"
# 快捷支付-确认支付
QF_BUSICD_QUICK_CONFIRM                 = "700103"
# 快捷支付-撤销
QF_BUSICD_QUICK_CANCEL                  = "700104"
# 快捷支付-退款
QF_BUSICD_QUICK_REFUND                  = "700105"
# 快捷支付-查询
QF_BUSICD_QUICK_QUERY                   = "700106"
# 快捷支付-签约支付  @IMPORTANT 废弃
QF_BUSICD_QUICK_SIGN_PAY                = "700107"
# 快捷支付-协议号支付  @IMPORTANT 废弃
QF_BUSICD_QUICK_PROTOCOL_PAY            = "700108"
# 快捷支付-开卡
QF_BUSICD_QUICK_OPENCARD                = "700109"
# 快捷支付-开卡查询
QF_BUSICD_QUICK_OPENCARD_QUERY          = "700110"


# 提现 目前富友使用
# 查询
QF_BUSICD_WITHDRAW_QUERY                = "700201"
# 计算手续费
QF_BUSICD_WITHDRAW_CAL_FEE              = "700202"
# 发起提现
QF_BUSICD_WITHDRAW_CREATE               = "700203"
# 提现预算
QF_BUSICD_WITHDRAW_BUDGET               = "700204"
# 收益查询
QF_BUSICD_WITHDRAW_PROFIT_QUERY         = "700205"

#### 代付 ####
# 代付-单笔代付
QF_BUSICD_CASHDRAW_SINGLE_PAY           = "700301"
# 代付-单笔代付查询
QF_BUSICD_CASHDRAW_SINGLE_QUERY         = "700302"
# 代付-批量代付
QF_BUSICD_CASHDRAW_BATCH_PAY            = "700303"
# 代付-批量代付查询
QF_BUSICD_CASHDRAW_BATCH_QUERY          = "700304"

# 无卡反扫合一
QF_BUSICD_NOCARD_SWIPE                  = "800008"

# 支付宝预下单
QF_BUSICD_ALIPAY_PRECREATE              =   "800101"
# 支付宝退款查询
QF_BUSICD_ALIPAY_REFUND_QUERY           =   "800102"
# 支付宝退款
QF_BUSICD_ALIPAY_REFUND                 =   "800103"
# 支付宝查询
QF_BUSICD_ALIPAY_QUERY                  =   "800104"
# 支付宝撤销
QF_BUSICD_ALIPAY_CANCEL                 =   "800105"
# 支付宝H5
QF_BUSICD_ALIPAY_H5                     =   "800107"
# 支付宝刷卡
QF_BUSICD_ALIPAY_SWIPE                  =   "800108"
# 支付宝冲正 @ATTENTION 目前只有海外版使用
QF_BUSICD_ALIPAY_REVERSE                =   "800109"
# 支付宝WAP
QF_BUSICD_ALIPAY_WAP                    =   "800112"

# 微信统一预下单
QF_BUSICD_WEIXIN_PRECREATE              =   "800201"
# 微信退款查询
QF_BUSICD_WEIXIN_REFUND_QUERY           =   "800202"
# 微信退货
QF_BUSICD_WEIXIN_REFUND                 =   "800203"
# 微信订单查询
QF_BUSICD_WEIXIN_QUERY                  =   "800204"
# 微信关闭订单
QF_BUSICD_WEIXIN_CLOSE_ORDER            =   "800205"
# 微信账单查询
QF_BUSICD_WEIXIN_DOWNLOADBILL           =   "800206"
# 微信H5统一预下单
QF_BUSICD_WEIXIN_PRECREATE_H5           =   "800207"
# 微信小额支付
QF_BUSICD_WEIXIN_SWIPE                  =   "800208"
# 微信小额支付冲正
QF_BUSICD_WEIXIN_REVERSAL               =   "800209"
# 微信APP
QF_BUSICD_WEIXIN_APP                    =   "800210"
# 微信授权码获取openid
QF_BUSICD_WEIXIN_AUTHCODE_TO_OPENID     =   "800211"
# 微信WAP
QF_BUSICD_WEIXIN_WAP                    =   "800212"
# 微信小程序
QF_BUSICD_WEIXIN_MAPP                   =   "800213"


#银联代收交易
QF_BUSICD_UNIONPAY_WITHHOLDING_TRADE    =   "800301"
QF_BUSICD_UNIONPAY_WITHHOLDING_VERIFY   =   "800302"
QF_BUSICD_UNIONPAY_WITHHOLDING_QUERY    =   "800303"
QF_BUSICD_UNIONPAY_WITHHOLDING_REFUND   =   "800304"
QF_BUSICD_UNIONPAY_WITHHOLDING_BIND     =   "800305"
QF_BUSICD_UNIONPAY_WITHHOLDING_UNBIND   =   "800306"

# 百度的百付宝预下单
QF_BUSICD_BAIFUBAO_PRECREATE            =   "800401"
# 百度的百付宝退款查询
QF_BUSICD_BAIFUBAO_REFUND_QUERY         =   "800402"
# 百度的百付宝退货
QF_BUSICD_BAIFUBAO_REFUND               =   "800403"
# 百度的百付宝订单查询
QF_BUSICD_BAIFUBAO_QUERY                =   "800404"
# 百度的百付宝关闭订单
QF_BUSICD_BAIFUBAO_CLOSE_ORDER          =   "800405"
# 百度的百付宝条码支付
QF_BUSICD_BAIFUBAO_PAY                  =   "800408"
# 百度的百付宝支付冲正
QF_BUSICD_BAIFUBAO_REVERSAL             =   "800409"

# 京东钱包扫码下单
QF_BUSICD_JDPAY_PRECREATE               =   "800501"
# 京东退款查询
QF_BUSICD_JDPAY_REFUND_QUERY            =   "800502"
# 京东钱包退款
QF_BUSICD_JDPAY_REFUND                  =   "800503"
# 京东钱包查询
QF_BUSICD_JDPAY_QUERY                   =   "800504"
# 京东钱包H5支付
QF_BUSICD_JDPAY_H5                      =   "800507"
# 京东钱包付款码
QF_BUSICD_JDPAY_SWIPE                   =   "800508"

# QQ钱包扫码下单
QF_BUSICD_QQPAY_QRCODE                  =   "800601"
# QQ钱包退款查询
QF_BUSICD_QQPAY_REFUND_QUERY            =   "800602"
# QQ钱包退款
QF_BUSICD_QQPAY_REFUND                  =   "800603"
# QQ钱包查询
QF_BUSICD_QQPAY_QUERY                   =   "800604"
# QQ钱包H5预下单
QF_BUSICD_QQPAY_H5                      =   "800607"
# QQ钱包付款码
QF_BUSICD_QQPAY_SWIPE                   =   "800608"

# 银联二维码下单
QF_BUSICD_UNIONPAY_QRCODE_PRECREATE     =   "800701"
QF_BUSICD_UNIONPAY_QRCODE_REFUND_QUERY  =   "800702"
# 银联二维码退款
QF_BUSICD_UNIONPAY_QRCODE_REFUND        =   "800703"
# 银联二维码查询
QF_BUSICD_UNIONPAY_QRCODE_QUERY         =   "800704"
# 银联付款码
QF_BUSICD_UNIONPAY_QRCODE_SWIPE         =   "800708"
# 银联二维码冲正
QF_BUSICD_UNIONPAY_QRCODE_REVERSAL      =   "800709"
# 银联二维码冲正
QF_BUSICD_UNIONPAY_QRCODE_REFUND_QUERY  =   "800702"

# 网关支付
QF_BUSICD_GATEWAYPAY                    =   "800801"
# 网关支付查询
QF_BUSICD_GATEWAYPAY_QUERY              =   "800802"

# 翼支付二维码下单
QF_BUSICD_BESTPAY_QRCODE_PRECREATE      =   "800901"
# 翼支付查询
QF_BUSICD_BESTPAY_QUERY                 =   "800902"

#微信香港反扫
QF_BUSICD_WEIXIN_HK_SWIPE               =   "801008"
#微信香港查询
QF_BUSICD_WEIXIN_HK_QUERY               =   "801004"
#微信香港退款
QF_BUSICD_WEIXIN_HK_REFUND              =   "801003"
#微信香港冲正
QF_BUSICD_WEIXIN_HK_REVERSAL            =   "801009"
#微信香港退款查询
QF_BUSICD_WEIXIN_HK_REFUND_QUERY        =   "801002"

# 支付宝海外在线PC支付
QF_BUSICD_ALIPAY_ONLINE_PC              =   "801101"
# 支付宝海外在线退款查询
QF_BUSICD_ALIPAY_ONLINE_REFUND_QUERY    =   "801102"
# 支付宝海外在线WAP支付
QF_BUSICD_ALIPAY_ONLINE_WAP             =   "801107"
# 支付宝海外在线查询
QF_BUSICD_ALIPAY_ONLINE_QUERY           =   "801104"
# 支付宝海外在线退款
QF_BUSICD_ALIPAY_ONLINE_REFUND          =   "801103"

# LINE PAY 线下支付反扫
QF_BUSICD_LINEPAY_SWIPE                 =   "801208"
# LINE PAY 线下支付查询
QF_BUSICD_LINEPAY_QUERY                 =   "801204"
# LINE PAY 线下退款
QF_BUSICD_LINEPAY_REFUND                =   "801203"

# LINE PAY 线上预支付
QF_BUSICD_LINEPAY_ONLINE_RESERVE        =   "801301"
# LINE PAY 线上确认支付
QF_BUSICD_LINEPAY_ONLINE_CONFIRM        =   "801307"
# LINE PAY 线上支付查询
QF_BUSICD_LINEPAY_ONLINE_QUERY          =   "801304"
# LINE PAY 线下退款
QF_BUSICD_LINEPAY_ONLINE_REFUND         =   "801303"

#AIR PAY 线上扫码查询
QF_BUSICD_AIRPAY_QUERY                  =   "801404"
#AIR PAY 线上反扫支付
QF_BUSICD_AIRPAY_SWIPE                  =   "801408"
#AIR PAY 线上退款
QF_BUSICD_AIRPAY_REFUND                 =   "801403"
#AIR PAY 线上退款查询
QF_BUSICD_AIRPAY_REFUND_QUERY           =   "801402"

#支付宝香港 WAP支付 
QF_BUSICD_ALIPAY_HK_WAP                 =   '801512'
#支付宝香港 PC支付 
QF_BUSICD_ALIPAY_HK_PC                  =   '801501'
#支付宝香港查询
QF_BUSICD_ALIPAY_HK_QUERY               =   "801504"
#支付宝香港退款
QF_BUSICD_ALIPAY_HK_REFUND              =   "801503"
#支付宝香港退款查询
QF_BUSICD_ALIPAY_HK_REFUND_QUERY        =   "801502"

#机构签到 buscid
QF_BUSICD_ORG_SIGNIN                    =   "600001"
#机构绑定商户 buscid
QF_BUSICD_ORG_MCHNT_BIND                =   "600002"

busicd = {
    QF_BUSICD_TOCARD: u'转账',
    QF_BUSICD_TOCREDIT: u'还款',
    QF_BUSICD_RECHARGE: u'充值',
    QF_BUSICD_PAYMENT: u'刷卡消费',
    QF_BUSICD_REVERSAL: u'消费冲正',
    QF_BUSICD_REFUND: u'退货',
    QF_BUSICD_BALANCE: u'余额查询',
    QF_BUSICD_UPLOAD: u'上传凭证',
    QF_BUSICD_TRADEQUERY:u'交易查询',
    QF_BUSICD_TRADELIST: u'交易查询',
    QF_BUSICD_TRADEINFO: u'交易详情',
    QF_BUSICD_RECEIPT: u'发送收据',
    QF_BUSICD_INIT: u'初始化',
    QF_BUSICD_ACTIVE: u'激活',
    QF_BUSICD_LOGIN: u'登录',
    QF_BUSICD_STAT: u'统计',
    QF_BUSICD_FEED: u'反馈',
    QF_BUICD_CHPASS: u'修改密码',
    QF_BUICD_UPDATEKEYS: u'更新秘钥',
    QF_BUSICD_CANCEL: u'消费撤销',
    QF_BUSICD_CANCEL_REVERSAL: u'消费撤销冲正',
    QF_BUSICD_CASH: u'现金记账',
    QF_BUSICD_ORDER_PAY: u'订单支付',
    QF_BUSICD_ORDER_CREATE: u'创建订单',
    QF_BUSICD_ORDER_QUERY: u'订单查询',
    QF_BUSICD_ORDER_CANCEL: u'定单撤销',
    QF_BUSICD_ICNOTICE: u'脚本通知',
    QF_BUSICD_PAUTH: u'预授权',
    QF_BUSICD_PAUTH_REVERSAL: u'预授权冲正',
    QF_BUSICD_PAUTH_CANCEL: u'预授权撤销',
    QF_BUSICD_PAUTH_CANCEL_REVERSAL: u'预授权撤销冲正',
    QF_BUSICD_PAUTHCP: u'预授权完成',
    QF_BUSICD_PAUTHCP_REVERSAL: u'预授权完成冲正',
    QF_BUSICD_PAUTHCP_CANCEL: u'预授权完成撤销',
    QF_BUSICD_PAUTHCP_CANCEL_REVERSAL: u'预授权完成撤销冲正',
    QF_BUSICD_MANAGE: u'管理报文',
    QF_BUSICD_SECRET: u'秘钥更新',
    QF_BUSICD_BACOO_ORDER: u'烟草订购',
    #QF_BUSICD_BACCO_PAYMENT: u'烟草消费',
    QF_BUSICD_ALIPAY_PRECREATE: u'支付宝扫码',
    QF_BUSICD_ALIPAY_REFUND: u'支付宝退款',
    QF_BUSICD_ALIPAY_QUERY: u'支付宝查询',
    QF_BUSICD_ALIPAY_WAP: u'支付宝WAP',
    QF_BUSICD_ALIPAY_ONLINE_PC: u'支付宝海外在线PC支付',
    QF_BUSICD_ALIPAY_ONLINE_WAP: u'支付宝海外在线WAP支付',
    QF_BUSICD_ALIPAY_ONLINE_QUERY: u'支付宝海外在线支付查询',
    QF_BUSICD_ALIPAY_ONLINE_REFUND: u'支付宝海外在线支付退款',
    QF_BUSICD_ALIPAY_ONLINE_REFUND_QUERY: u'支付宝海外在线支付退款查询',
    QF_BUSICD_ALIPAY_CANCEL: u'支付宝撤销(冲正)',
    QF_BUSICD_ALIPAY_H5: u'支付宝H5',
    QF_BUSICD_WEIXIN_PRECREATE: u'微信扫码',
    QF_BUSICD_WEIXIN_PRECREATE_H5: u'微信H5',
    QF_BUSICD_WEIXIN_QUERY: u'微信订单查询',
    QF_BUSICD_WEIXIN_CLOSE_ORDER: u'微信关闭订单',
    QF_BUSICD_WEIXIN_REFUND_QUERY: u'微信退款查询',
    QF_BUSICD_WEIXIN_REFUND: u'微信退款',
    QF_BUSICD_WEIXIN_SWIPE: u'微信刷卡支付',
    QF_BUSICD_WEIXIN_APP: u'微信APP',
    QF_BUSICD_WEIXIN_WAP: u'微信WAP',
    QF_BUSICD_WEIXIN_MAPP: u'微信小程序支付',
    QF_BUSICD_ALIPAY_SWIPE: u'支付宝刷卡',
    QF_BUSICD_ALIPAY_REFUND_QUERY: u'支付宝退款查询',
    QF_BUSICD_WEIXIN_REVERSAL:u"微信刷卡撤销(冲正)",
    QF_BUSICD_BAIFUBAO_PRECREATE: u'百度的百付宝预下单',
    QF_BUSICD_BAIFUBAO_REFUND_QUERY: u'百度的百付宝退款查询',
    QF_BUSICD_BAIFUBAO_REFUND: u'百度的百付宝退货',
    QF_BUSICD_BAIFUBAO_QUERY: u'百度的百付宝订单查询',
    QF_BUSICD_BAIFUBAO_CLOSE_ORDER: u'百度的百付宝关闭订单',
    QF_BUSICD_BAIFUBAO_PAY: u'百度的百付宝条码支付',
    QF_BUSICD_BAIFUBAO_REVERSAL: u'百度的百付宝支付冲正',
    QF_BUSICD_JDPAY_PRECREATE: u'京东扫码',
    QF_BUSICD_JDPAY_REFUND: u'京东退款',
    QF_BUSICD_JDPAY_QUERY: u'京东查询',
    QF_BUSICD_JDPAY_REFUND_QUERY: u'京东退款查询',
    QF_BUSICD_JDPAY_H5: u'京东H5',
    QF_BUSICD_JDPAY_SWIPE: u'京东付款码',
    QF_BUSICD_QQPAY_QRCODE:u'QQ钱包扫码',
    QF_BUSICD_QQPAY_REFUND_QUERY: u'QQ钱包退款查询',
    QF_BUSICD_QQPAY_REFUND:u'QQ钱包退款',
    QF_BUSICD_QQPAY_QUERY:u'QQ钱包查询',
    QF_BUSICD_QQPAY_H5:u'QQ钱包H5',
    QF_BUSICD_QQPAY_SWIPE:u'QQ钱包刷卡',
    QF_BUSICD_UNIONPAY_QRCODE_PRECREATE: u'银联二维码下单',
    QF_BUSICD_UNIONPAY_QRCODE_REFUND: u'银联二维码退款',
    QF_BUSICD_UNIONPAY_QRCODE_REFUND_QUERY: u'银联二维码退款查询',
    QF_BUSICD_UNIONPAY_QRCODE_QUERY: u'银联二维码查询',
    QF_BUSICD_UNIONPAY_QRCODE_SWIPE: u'银联二维码付款码',
    QF_BUSICD_PREPAID_CONSUME: u'储值消费',
    QF_BUSICD_PREPAID_QUERY: u'储值查询',
    QF_BUSICD_PREPAID_REFUND: u'储值退款',
    QF_BUSICD_PREPAID_SWIPE: u'储值反扫',
    QF_BUSICD_QUICK_PAY: u'快捷支付-普通支付',
    QF_BUSICD_QUICK_PROTOCOL_PAY: u'快捷支付-协议支付',
    QF_BUSICD_QUICK_SIGN_PAY: u'快捷支付-签约支付',
    QF_BUSICD_QUICK_SENDSMS: u'快捷支付-发送短信验证码',
    QF_BUSICD_QUICK_CONFIRM: u'快捷支付-确认',
    QF_BUSICD_QUICK_QUERY: u'快捷支付-查询',
    QF_BUSICD_QUICK_CANCEL: u'快捷支付-撤销',
    QF_BUSICD_QUICK_REFUND: u'快捷支付-退款',
    QF_BUSICD_QUICK_OPENCARD: u'快捷支付-开卡',
    QF_BUSICD_QUICK_OPENCARD_QUERY: u'快捷支付-开卡查询',
    QF_BUSICD_WITHDRAW_QUERY: u'提现金额查询',
    QF_BUSICD_WITHDRAW_CAL_FEE: u'提现手续费计算',
    QF_BUSICD_WITHDRAW_CREATE: u'提现发起',
    QF_BUSICD_CASHDRAW_BATCH_PAY: u'批量代付',
    QF_BUSICD_CASHDRAW_BATCH_QUERY: u'批量代付查询',
    QF_BUSICD_CASHDRAW_SINGLE_PAY: u'单笔代付',
    QF_BUSICD_CASHDRAW_SINGLE_QUERY: u'单笔代付查询',
    QF_BUSICD_NOCARD_SWIPE: u'无卡反扫',
    QF_BUSICD_GATEWAYPAY: u"网关支付",
    QF_BUSICD_GATEWAYPAY_QUERY: u"网关支付查询",
    QF_BUSICD_BESTPAY_QRCODE_PRECREATE: u"翼支付二维码下单",
    QF_BUSICD_BESTPAY_QUERY: u"翼支付查询",
    QF_BUSICD_WEIXIN_HK_SWIPE: u"微信香港反扫",
    QF_BUSICD_WEIXIN_HK_QUERY: u"微信香港查询",
    QF_BUSICD_WEIXIN_HK_REFUND: u"微信香港退款",
    QF_BUSICD_WEIXIN_HK_REVERSAL: u"微信香港冲正",
    QF_BUSICD_WEIXIN_HK_REFUND_QUERY: u"微信香港退款查询",
    QF_BUSICD_LINEPAY_SWIPE: u'LINE PAY 反扫',
    QF_BUSICD_LINEPAY_QUERY: u'LINE PAY 查询',
    QF_BUSICD_LINEPAY_REFUND: u'LINE PAY 退款',
    QF_BUSICD_LINEPAY_ONLINE_RESERVE: u'LINE PAY 线上预支付',
    QF_BUSICD_LINEPAY_ONLINE_CONFIRM: u'LINE PAY 线上确认支付',
    QF_BUSICD_LINEPAY_ONLINE_QUERY: u'LINE PAY 线上支付查询',
    QF_BUSICD_LINEPAY_ONLINE_REFUND: u'LINE PAY 线下退款',
    QF_BUSICD_AIRPAY_QUERY: u'AIR PAY 查询',
    QF_BUSICD_AIRPAY_SWIPE: u'AIR PAY 反扫',
    QF_BUSICD_AIRPAY_REFUND: u'AIR PAY 退款',
    QF_BUSICD_AIRPAY_REFUND_QUERY: u"退款查询",
    QF_BUSICD_ALIPAY_HK_WAP: u'支付宝香港 wap 支付',
    QF_BUSICD_ALIPAY_HK_QUERY: u'支付宝香港 查询',
    QF_BUSICD_ALIPAY_HK_REFUND: u'支付宝香港 退款',
    QF_BUSICD_ALIPAY_HK_REFUND_QUERY: u'支付宝香港 退款查询',
}


# 交易动作
QF_ACTION_QUERY                         = 1
QF_ACTION_REVERSAL                      = 2

# ---- 交易状态 ----
# 交易中
QF_TRADE_NOW                        = 0
# 交易成功
QF_TRADE_SUCC                       = 1
# 交易失败
QF_TRADE_FAILED                     = 2
# 交易超时
QF_TRADE_TIMEOUT                    = 3

trade_state = {
    QF_TRADE_NOW: u'交易中',
    QF_TRADE_SUCC: u'交易成功',
    QF_TRADE_FAILED: u'交易失败',
    QF_TRADE_TIMEOUT: u'交易超时',
}

QF_TRADE_NOW_STR                    = "0"
QF_TRADE_SUCC_STR                   = "1"
QF_TRADE_FAILED_STR                 = "2"
QF_TRADE_TIMEOUT_STR                = "3"

# ---- 取消状态 ----
QF_CANCEL_NO                        = 0
# 已冲正
QF_CANCEL_REVERSAL                  = 1
# 已撤销
QF_CANCEL_CANCELED                  = 2
# 已退货
QF_CANCEL_REFUND                    = 3
# 已完成预授权
QF_CANCEL_PAUTHCP                   = 4
# 已部分退款
QF_CANCEL_PART_REFUND               = 5

cancel_state = {
    QF_CANCEL_NO: u'无',
    QF_CANCEL_REVERSAL: u'已冲正',
    QF_CANCEL_CANCELED: u'已撤销',
    QF_CANCEL_REFUND: u'已退货',
    QF_CANCEL_PAUTHCP: u'已预授权完成',
    QF_CANCEL_PART_REFUND: u'已部分退款',
}

# ---- 卡类型 ----
# 未识别卡
QF_CARD_UNKNOWN                     = 0
# 借记卡
QF_CARD_DEBIT                       = 1
# 信用卡(贷记卡)
QF_CARD_CREDIT                      = 2
# 准贷记卡
QF_CARD_SEMICREDIT                  = 3
# 储值卡
QF_CARD_VALUE                       = 4
# zhanghao
QF_CARD_ACCOUNT                     = 5

# ---- 卡种 ----
# 磁条卡
QF_CARD_CLASS_MAGNETIC              = 1
# IC卡
QF_CARD_CLASS_IC                    = 2
# 无卡交易
QF_CARD_CLASS_NOCARD                = 3
# 复合卡
QF_CARD_CLASS_IC_MAGNETIC           = 4

card_type = {
    QF_CARD_UNKNOWN: u'未识别卡',
    QF_CARD_DEBIT: u'借记卡',
    QF_CARD_CREDIT: u'信用卡',
    QF_CARD_SEMICREDIT: u'准贷记卡',
    QF_CARD_VALUE: u'储值卡',
    QF_CARD_ACCOUNT: u'第三方账号',
}


# ---- 卡类型限制 ----
# 国内借记卡
QF_CARDALLOW_DEBIT_CN               = 1
# 国外借记卡
QF_CARDALLOW_DEBIT_FOREIGN          = 2
# 国内信用卡
QF_CARDALLOW_CREDIT_CN              = 4
# 国外信用卡
QF_CARDALLOW_CREDIT_FOREIGN         = 8

# ---- 渠道接入模式 ----
# 我们的渠道路由方(讯联)
QF_CHNLMODE_CHNL                    = 0
# 终端接入
QF_CHNLMODE_TERM                    = 1
# 机构接入
QF_CHNLMODE_ORG                     = 2

# 已上传凭证
QF_SIGN_NO                          = 0
# 未上传凭证
QF_SIGN_OK                          = 1

# --- 撤销控制查询类型 ---
# userid
QF_SETTLE_CONFIG_TYPE_USERID        = 0
# groupid
QF_SETTLE_CONFIG_TYPE_GROUPID       = 1
# 通道商户号
QF_SETTLE_CONFIG_TYPE_CHNLUSERID    = 2
