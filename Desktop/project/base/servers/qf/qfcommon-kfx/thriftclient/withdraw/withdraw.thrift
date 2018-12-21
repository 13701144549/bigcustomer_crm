namespace py withdraw

// 发生错误时的返回码及其对应的描述信息
exception ServerError
{
    1: string code, // 返回码
    2: string msg,  // 描述信息
}

// 银行卡信息
struct Card
{
    1:  i64     userid,     // 商户id
    2:  string  name,       // 持卡人姓名
    3:  string  cardno,     // 卡号
    4:  i16     card_type,  // 卡类型 1: 借记卡 2: 信用卡
    5:  string  bank_name,  // 银行
    6:  string  bank_brch,  // 支行
    7:  string  bank_area,  // 开户省
    8:  string  bank_city,  // 开户市
    9:  string  bank_code,  // 银联标准的联行号
    10: i16     bank_type,  // 银行类型 1: 对私 2: 对公
    11: string  bank_mobile,// 持卡人手机号
    12: string  memo,       // 备注
}

// 查询商户提现明细查询
struct WithdrawDetailArgs
{
    1:  i64    userid,       // 以商户id为条件查询
    2:  string start_time,   // 查询交易的起始时间，如果为空，则根据month字段查询
    3:  string end_time,     // 查询交易的结束时间，如果为空，则根据month字段查询
    4:  i32    pos = 0,      // 查询的起始位置
    5:  i32    count = 20,   // 查询的个数
    6:  i32    status        // 状态
    7: list<string> ids,     // 提现操作id
    8:  string month = '',   // 账户记录按照月份查询,格式'2018-01'
}

// 查询商户收益记录流水
struct ProfitRecordArgs
{
    1:  i64    userid,       // 以商户id为条件查询
    2:  string start_date,   // 查询收益的起始时间，如果为空，则根据month字段查询
    3:  string end_date,     // 查询收益的结束时间，如果为空，则根据month字段查询
    4:  i32    pos = 0,      // 查询的起始位置
    5:  i32    count = 20,   // 查询的个数
    6:  i32    status        // 状态
}

struct WithdrawDetail
{
    1:  i64     id,                 // 提现记录id
    2:  i64     userid,             // 商户id
    3:  string  biz_sn,             // 业务流水号
    4:  i64     amt,                // 提现金额，以分为单位
    5:  i32     fee,                // 手续费
    6:  double  ratio,              // 费率
    7:  Card    card                // 商户卡信息
    8:  string  currency = '156',   // 交易的币种
    9:  string  withdraw_time,      // 提现时间
    10: string  success_time,       // 提现成功时间
    11: i32     status,             // 提现状态
    12: string  memo,               // 备注
}

struct ProfitRecord
{
    1:  i64     id,                 // 提现记录id
    2:  i64     userid,             // 商户id
    3:  string  mchid,              // 商户号
    4:  i64     available_amt,      // 可用账户金额，以分为单位
    5:  i64     freeze_amt,         // 冻结账户金额，以分为单位
    6:  i64     sysfreeze_amt,      // 系统冻结账户金额，以分为单位
    7:  i64     day_profit,         // 当日收益，以分为单位
    8:  i64     week_profit,        // 本周收益，以分为单位
    9:  i64     month_profit,       // 本月收益，以分为单位
    10: i64     total_profit,       // 累计收益，以分为单位
    11: string  profit_date,        // 收益日期
    12: i32     status,             // 收益状态
    13: string  memo,               // 备注
}

struct WithdrawArgs
{
    1: i64 userid,          // 商户id
    2: i64 chnl_id,         // 通道id
    3: Card card,           // 商户卡信息
    4: string cert_name,    // 证件名称
    5: string cert_type,    // 证件类型, 仅支持身份证传01
    6: string cert_no,      // 证件号
    7: string auth_code,    // 短信验证码
}

struct Budget
{
    1:  i64     userid,             // 商户id
    2:  i64     amt,                // 当前可提现金额，以分为单位
    3:  string  currency = '156',   // 提现币种
    4:  i16     status,             // 提现功能是否开启,0未开启,1开启
}

service Withdraw
{
    i16 ping();

    // 查询提现记录
    list<WithdrawDetail> withdraw_detail(1:WithdrawDetailArgs detail_args) throws(1:ServerError e);

    // 查询收益记录
    list<ProfitRecord> profit_query(1:ProfitRecordArgs query_args) throws(1:ServerError e);

    // 开通提现
    // 返回值: 1 成功
    i16 open_withdraw(1:WithdrawArgs withdraw_args) throws(1:ServerError e);

    // 提现申请操作[userid 提现商户id amt 提现金额]
    // 返回值: 1 成功
    WithdrawDetail withdraw_apply(1:i64 userid, 2:i64 amt) throws(1:ServerError e);

    // 提现预算接口[userid 提现商户id amt 预提现金额]
    // 返回值: 1 成功
    Budget withdraw_budget(1:i64 userid, 2:i64 amt) throws(1:ServerError e);
}
