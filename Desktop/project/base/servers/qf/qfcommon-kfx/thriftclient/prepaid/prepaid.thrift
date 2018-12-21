namespace py prepaid

enum BIZ_TYPE
{
    RECHARGE=1,     // 储值-充值
    CONSUME=2,      // 储值-消费
    REFUND=3,       // 储值-消费退款
    MANUAL_RECHARGE=4, // 手动充值(内部增加金额)
    MANUAL_CONSUME=5,  // 手动消费
}

// 储值业务交易状态
//
// 状态迁移图:
//
// 储值-充值:  充值成功(TRADING -> SUCCESS), 充值失败(TRADING -> FAILED)
// 储值-消费:  消费成功(TRADING -> SUCCESS), 消费失败(TRADING -> FAILED), 退款成功(SUCCESS -> REFUNDED)
// 储值-消费退款: 退款成功(TRADING -> SUCCESS),  退款失败(TRADING -> FAILED)
//
enum PREPAID_STATUS
{
    TRADING=0,      // 交易中
    SUCCESS=1,      // 交易成功
    FAILED=2,       // 交易失败
    TIMEOUT=3,      // 交易超时, 暂不使用
    REFUNDED=4,       // 消费已退款, 仅针对`储值-消费`类型的交易
}

enum ERRCODE
{
    // 系统错误
    INNER_SERVICE_ERR=5000,         // 内部错误
    OUT_SERVICE_ERR,                // 外部调用错误
    SYSTEM_ERROR,                   // 系统错误

    // 逻辑错误
    PARAM_ERROR=6000,               // 参数错误

    // 业务错误
    INSUFFICIENT_BALANCE=6100,  // 余额不足
    INVALID_BIZ_SN,             // 非法的biz_sn
    INVALID_SYSSN,              // 非法的syssn
    INVALID_STATUS,             // 非法的交易状态, 交易记录的状态不支持当前的操作. 如: 重复退款, 对失败的消费交易退款
    INVALID_BIZ_TYPE,           // 非法的业务代码
    PREPAID_UNUSED,             // 消费者还未在商户下使用过储值功能
}


// 储值服务异常
exception PrepaidError
{
    1: i32      respcd,     // 返回码
    2: string   resperr,    // 错误信息
}


////////////
// API定义 //
////////////


// 储值(充值/消费) 结果
struct PrepaidRecord
{
    1: required i32 cid,                // 消费者ID
    2: required i64 userid,             // 产生该交易的商户ID， 该交易在哪个商户下发生的。
    3: required string biz_sn,          // 储值流水号
    4: required string syssn,           // 支付系统流水号
    5: required PREPAID_STATUS status,  // 储值状态
    6: required BIZ_TYPE biz_type,      // 业务类型: 选填: 1(充值), 2(消费), 3(消费退款), 4(手动充值)
    7: required i32 txamt,              // 交易金额
    8: optional i32 pay_amt,            // 支付金额, 业务类型为RECHARGE时有效, 代表消费者真正支付的金额
    9: optional i32 present_amt,        // 赠送金额, 业务类型为RECHARGE时有效, 代表储值时赠送的金额
    10: optional string orig_biz_sn,    // 原始交易储值业务流水号, 业务类型为REFUND时有效, 代表退款的原始交易储值业务流水号
    11: optional i64 activity_id,       // 活动ID, 业务类型为RECHARGE时有效, 代表该充值所属的活动
    12: required string sysdtm,         // 交易时间
    13: optional i64 fund_uid,          // 影响资金的商户ID， 该交易最终影响到消费者在哪个商户下的资金
}

// 余额信息
struct BalanceInfo
{
    1: required i32 cid,                // 消费者ID
    2: required i64 userid,             // 商户ID
    3: required i32 balance,            // 余额
    4: required string first_use_dtm,   // 第一次在该商户下,使用储值业务的时间
    5: required string last_recharge_dtm,   // 第一次在该商户下,进行充值的时间
    6: required string last_consume_dtm,   // 最后移除在该商户下,进行消费的时间
    7: required string id,                 // 条目ID
    8: required string update_time,     // 数据最后更新时间
}

// 储值-充值
struct RechargeArg
{
    1: required i32 cid,            // 消费者ID
    2: required i64 userid,         // 商户ID
    3: required i64 activity_id,    // 活动ID, 自定义类型无活动ID填0
    4: required i32 grid_index,     // 充值规则格位, 自定义类型无格位填0
    5: required i32 pay_amt,        // 消费者支付金额
    6: required i32 present_amt,    // 商户赠送金额, 自定义类型无赠送填0
    7: optional string memo='',     // 备注
    8: optional string openid,      // 消费者在微信公众号下的openid
}

// 储值-消费
struct ConsumeArg
{
    1: required i32 cid,                // 消费者ID
    2: required i64 userid,             // 商户ID
    3: required i32 txamt,              // 消费金额
    4: required string syssn,           // 支付系统流水号
    5: optional string memo='',         // 备注
}

// 储值-查询
struct QueryArg
{
    1: required string syssn,          // 支付系统流水号
    2: optional i32 cid,                // 消费者ID
    3: required i64 userid,             // 商户ID
}

// 储值-消费退款
struct RefundArg
{
    1: required string syssn,           // 支付系统流水号
    2: required string refund_sn,       // 退款唯一流水号, 支付系统生成
    3: optional i32 cid,                // 消费者ID
    4: required i64 userid,             // 商户ID
    5: required i32 txamt,              // 退款金额
    6: optional string memo='',         // 本次退款操作的原因
}

// 储值余额操作
struct OPPrepaidBalanceArg
{
    1: required i32 cid,                // 消费者ID
    2: required i64 userid,             // 产生该交易的商户ID， 该交易在哪个商户下发生的。
    3: required i32 txamt,              // 交易金额
    4: required BIZ_TYPE biz_type,      // 业务类型: 选填: 1(充值) 或 2(消费)
    5: required string memo,            // 本次余额操作的原因, 为了余额安全,本字段必填
    6: optional i64 fund_uid,           // 影响资金的商户ID， 该交易最终影响到消费者在哪个商户下的资金（针对连锁店模式）
}

// 储值回调
struct PrepaidNotifyArg
{
    1: required string biz_sn,          // 储值业务流水号
    2: required string syssn,           // 支付系统流水号
    3: required string respcd,          // 结果码
    4: required string respmsg,      // 结果描述字符串
}


service prepaid
{
    // 充值, 返回该充值交易产生的记录
    PrepaidRecord recharge(1:RechargeArg arg) throws(1:PrepaidError e);
    // 手动充值, 返回该充值交易产生的记录
    PrepaidRecord manual_recharge(1:RechargeArg arg) throws(1:PrepaidError e);
    // 消费, 返回该消费交易产生的记录
    PrepaidRecord consume(1:ConsumeArg arg) throws(1:PrepaidError e);
    // 手动消费, 返回该消费交易产生的记录
    PrepaidRecord manual_consume(1:ConsumeArg arg) throws(1:PrepaidError e);
    // 充值或消费 查询, 返回该交易的记录
    PrepaidRecord query(1:QueryArg arg) throws(1:PrepaidError e);
    // 消费退款, 返回该退款交易产生的记录
    PrepaidRecord refund(1:RefundArg arg) throws(1:PrepaidError e);
    // 直接增/减消费者的余额, 用于业务上的差错处理. 一般情况不要调用本接口!
    PrepaidRecord op_balance(1:OPPrepaidBalanceArg arg) throws(1:PrepaidError e);
    // 储值回调
    PrepaidRecord prepaid_notify(1:PrepaidNotifyArg arg) throws(1:PrepaidError e);

    // 获取消费者在指定商户下的余额信息, 如果消费者和商户储值关系不存在,则不返回该商户的记录
    list<BalanceInfo> balance(1:i32 cid, 2:list<i64> userid_list) throws(1:PrepaidError e);
    // 获取消费者的所有储值余额信息
    list<BalanceInfo> all_balance(1:i32 cid) throws(1:PrepaidError e);
    // 获取商户下的指定消费者的余额信息, 如果消费者和商户储值关系不存在,则不返回该消费者的记录
    list<BalanceInfo> m_balance(1:i64 userid, 2:list<i32> cid_list) throws(1:PrepaidError e);
    // 获取商户下的所有消费者的储值余额信息
    list<BalanceInfo> m_all_balance(1:i64 userid) throws(1:PrepaidError e);



    ////////////
    // 其他业务 //
    ////////////
    string ping();
}
