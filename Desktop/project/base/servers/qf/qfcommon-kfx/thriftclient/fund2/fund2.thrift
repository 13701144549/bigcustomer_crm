namespace py fund2

exception ServerError
{
    1: string code,
    2: string msg,
}

struct FundQueryParams
{
    1: string  start_date,
    2: string  end_date,
    3: i64     userid,
    4: list<i64> userids = [],
    5: i64  limit,
    6: i64  offset,
}

// 帐户划款记录
struct RemitRecord
{
    1:  i64     userid,            // 商户id
    2:  i64     amt,               // 划款金额
    3:  string  biz_time,          // 划款时间
    4:  i64     account_type_id,   // 帐户的类型
    5:  string  name,              // 姓名
    6:  string  cardno,            // 银行卡号
    7:  string  bank_name,         // 总行
    8:  string  bank_brch,         // 支行
    9:  string  bank_area,         // 开户省
    10: string  bank_city,         // 开户市
    11: string  bank_code,         // 联行号
    12: i64     bank_type,         // 账户类型
    13: i64     remitback_id,      // 退票id
    14: i64     id                 // 划款id
    15: string  remitback_memo     // 退票原因
}

// 帐户收益记录
struct SettleRecord
{
    1: i64 userid,       //商户id
    2: i64 amt,          //总金额
    3: i64 num,          //总笔数
    4: i64 fee,          //总手续费
    5: string biz_time,   //结算时间
    6: i64 chnl_id,       //通道id
    7: i64 account_type_id,  //账户类型
    8: string trade_date,  //交易时间
    9: i64 id,
}

// 商户交易记录
struct TradeRecord
{
    1: i64 userid,       //商户id
    2: i64 amt,          //交易金额
    3: i64 fee,          //手续费
    4: string biz_sn,     //钱方流水号
    5: string orig_biz_sn,  //原钱方流水号
    6: i64 chnl_id,       //通道id
    7: string  trade_time,  //交易时间
    8: string  trade_type,  //交易类型
}

struct RemitRuleArg
{
    1: string cardno   //银行卡号
    2: string name     //姓名 
    3: i64  amt        //金额
    4: i32  account_type_id  //账户ID 
    5: i32  enable     //是否启用
}

service Fund2
{
    // 商户划款记录
    list<RemitRecord> remit_query(1: FundQueryParams query_args) throws(1: ServerError e);

    // 商户结算记录
    list<SettleRecord> settle_query(1: FundQueryParams query_args) throws(1: ServerError e);

    // 商户交易记录
    list<TradeRecord> trade_query(1: FundQueryParams query_args) throws(1: ServerError e);

    // 统计划款记录总数
    i32 remit_query_count(1: FundQueryParams  query_args) throws(1: ServerError e);

    //增加清算规则
    i32 add_remit_rule(1:list<RemitRuleArg>  rule_args) throws(1:ServerError e),

    //修改清算规则
    i32 change_remit_rule(1:list<RemitRuleArg>  rule_args) throws(1:ServerError e),
}
