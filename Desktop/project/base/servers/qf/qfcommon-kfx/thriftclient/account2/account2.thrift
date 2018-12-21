namespace py account2

// 发生错误时的返回码及其对应的描述信息
exception ServerError
{
    1: string code, // 返回码
    2: string msg,  // 描述信息
}

struct Photo
{
    1: string type,
    2: string filename,
}

enum CardChangeType
{
    MIS = 1,            // mis提交
    WEB = 2,            // 网页提交
    CHANNEL = 3,        // 渠道
    MIAOMIAO = 4,       // 喵喵微店
    PHONE = 5,          // 手机
}

enum CardChangeStatus
{
    WAITING = 1,        // 等待审核
    AUDITING = 2,       // 审核中
    PASS = 3,           // 审核通过
    CLOSE = 4,          // 审核关闭
}

// 帐户信息
struct Account
{
    1:  i64     id,           // 帐户id
    2:  i64     userid,       // 商户id
    3:  i64     amt,          // 帐户中的金额
    4:  i64     frozen_amt,   // 冻结金额
    6:  i64     account_type_id, // 帐户的类型
}

struct AccountQueryArgs
{
    1:  i64    amt,                 // 以帐户金额为条件查询, 默认不限制金额, 大于amt的数据
    2:  i32    pos = 0,             // 查询的起始位置
    3:  i32    count = 20,          // 查询的个数
    4:  list<i64> userids = [],     // 以商户id为条件批量查询
    5:  list<i64> account_type_ids = [],  // 查多个类型的账户
}

// 查询商户帐户记录流水
struct RecordArgs
{
    1:  i64    userid,       // 以商户id为条件查询
    2:  list<i32> action_types = [],     // 账户操作类型1:交易2:结算3:出款4:退票5:手续费6:扣款7:冻结
    3:  string start_time,   // 查询交易的起始时间，如果为空，则根据month字段查询
    4:  string end_time,     // 查询交易的结束时间，如果为空，则根据month字段查询
    5:  i32    pos = 0,      // 查询的起始位置
    6:  i32    count = 20,   // 查询的个数
    7:  string biz_sn,       // 账户操作流水号
    8:  string orig_biz_sn = '',  // 原交易流水号, 默认为不限制
    9: i64    account_id,   // 以帐户id为条件查询
    10: string month = '',   // 账户记录按照月份查询,格式'2018-01'
    11: list<i64> account_type_ids = [],  // 查多个类型的账户记录
}

struct Record
{
    1:  i64     id,                 // 帐户记录id
    2:  i64     userid,             // 以商户id为条件查询
    3:  i64     account_id,         // 以帐户id为条件查询
    4:  i64     account_type_id,    // 以帐户类型为条件查询
    5:  i32     action_type,        // 账户操作类型1:交易2:结算3:出款4:退票5:手续费6:扣款7:冻结
    6:  string  biz_sn,             // 业务流水号
    7:  string  orig_biz_sn,        // 原业务流水号
    8:  i64     amt,                // 业务操作金额，以分为单位
    9:  i64     refund_amt,         // 业务操作金额，以分为单位
    10:  i64    before_acct_amt,    // 业务操作金额，以分为单位
    11: string  biz_time,           // 业务时间
    12: string  title,              // 业务标题
    13: string  detail,             // 帐户操作详情
    14: string  memo,               // 业务时间
}

// 交易信息
struct Trade
{
    1:  i64    userid,              // 交易的商户id
    2:  string biz_sn,              // 交易流水号
    3:  string orig_biz_sn,         // 交易原流水号
    4:  i64    amt,                 // 交易的金额，以分为单位
    5:  string currency = '156',    // 交易的币种
    6:  string trade_time,          // 交易时间
    7:  string  pay_time,           // 支付时间
    8:  string  trade_type,         // 交易类型 busicd
    9:  i16     card_type,          // 卡类型   1.借记卡 2.信用卡 3.准贷记卡 4.储值卡 5.无卡
    10: string memo,                // 描述
    11: i32     chnl_id,            // 通道id
}

// 转账
struct Transfer
{
    1:  i64     userid,                 // 商户id
    2:  string  biz_sn,                 // 转账流水号
    3:  string  orig_biz_sn = '',       // 原转账流水号
    4:  string  orig_biz_time = '',     // 原转账操作时间
    5:  i64     from_account_type_id,   // 转出账户类型
    6:  i64     to_account_type_id,     // 转入账户类型
    7:  i64     amt,                    // 交易的金额，以分为单位
    8:  string  memo,                   // 描述
    9:  i32     orig_action_type,       // 原账户操作类型1:交易2:结算3:出款4:退票5:手续费6:扣款7:冻结
    10: string  biz_time,               // 业务操作时间
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
    11: string  bank_mobile, // 绑定卡预留手机号
    12: string  memo,       // 备注
}

struct CardChangeArgs
{
    1: i64 userid,
    2: Card card,
    3: list<Photo> photos,
    4: CardChangeType apply_type,   // 卡变更申请类型
    5: i64 apply_user,              // 卡变更申请人
}

struct CardChangeResp
{
    1: i64 userid,
    2: Card card,
    3: CardChangeStatus status,
    4: string memo,
}

// 银行卡查询参数
struct CardQueryArgs
{
    1: list<i64> userids,    // 以多个商户id为查询条件
}

// 费率信息
struct FeeRatio
{
    1:  i64     userid,         // 商户id
    2:  string  trade_type,     // 交易类型 busicd
    3:  i16     card_type,      // 卡类型   1.借记卡 2.信用卡 3.准贷记卡 4.储值卡 5.无卡
    4:  double  ratio,          // 费率
    5:  i32     max_fee,        // 费率封顶
}

// 手续费计算结果
struct Fee
{
    1: i32    fee,      // 手续费
    2: double ratio,    // 费率
    3: i32    max_fee,  // 费率封顶
}

// 费率查询参数
struct FeeQueryArgs
{
    1: list<i64>  userid,      // 以商户id列表为条件查询
    2: list<string> trade_type,  // 以交易类型列表为条件查询
    3: i16    card_type,   // 以卡类型为条件查询
}

// 计算手续费
struct CalculateFeeArgs
{
    1: i64    userid,           // 以商户id为条件查询
    2: string trade_type,       // 以交易类型为条件查询
    3: i16    card_type,        // 以卡类型为条件查询
    4: i64    amt,              // 交易金额
    5: i32    chnl_id,          // 通道id
}

//海外通道费率
struct OverseasFeeRatio
{
    1: i64      userid,
    2: double   airpay_ratio,    // airpay 费率
    3: double   unionpay_ratio,  // 银联费率
    4: double   alipayhk_ratio,  // 支付宝港币钱包费率
}

service Account2
{
    i16 ping();

    // 查询账户
    list<Account> account_query(1: AccountQueryArgs query_args) throws(1:ServerError e);
    // 查询账户记录
    list<Record> account_record(1: RecordArgs record_args) throws(1:ServerError e);
    // 撤销账户操作
    // 返回值: 1 成功
    i16 account_cancel(1:Transfer param) throws(1:ServerError e);

    // 交易，操作交易帐户
    // 返回值: 交易的费率信息
    Fee trade_payment(1:Trade trade) throws(1:ServerError e);

    // 撤销交易，交易金额从交易帐户中扣除
    // 返回值: 交易的费率信息
    Fee trade_cancel(1:Trade trade) throws(1:ServerError e);

    // 退货交易，交易金额从交易帐户中扣除
    // 返回值: 交易的费率信息
    Fee trade_refund(1:Trade trade) throws(1:ServerError e);

    // 结算(从钱方出款的交易帐户结算)
    // 返回值: 1 成功
    i16 settle(1:Transfer param) throws(1:ServerError e);

    // 出款
    // 返回值: 1 成功
    i16 remit(1:Transfer param) throws(1:ServerError e);

    // 出款退票
    // 返回值: 1 成功
    i16 remitback(1:Transfer param) throws(1:ServerError e);

    // 扣款
    // 返回值: 1 成功
    i16 withhold(1:Transfer param) throws(1:ServerError e);

    // 冻结
    // 返回值: 1 成功
    i16 frozen(1:Transfer param) throws(1:ServerError e);

    // 解冻
    // 返回值: 1 成功
    i16 unfrozen(1:Transfer param) throws(1:ServerError e);

    // 代付出款
    // 必传参数[userid, biz_sn, amt], 选传参数[memo, biz_time]
    // 返回值: 1 成功 -1 失败
    i16 cashdraw(1:Transfer param) throws(1:ServerError e);

    // 代付退票
    // 必传参数[userid, biz_sn, orig_biz_sn, orig_biz_time, amt], 选传参数[memo, biz_time]
    // 返回值: 1 成功 -1 失败
    i16 cashdrawback(1:Transfer param) throws(1:ServerError e);

    // 提现
    // 返回值: 1 成功
    i16 withdraw(1:Transfer param) throws(1:ServerError e);

    // 提现退回
    // 返回值: 1 成功
    i16 withdrawback(1:Transfer param) throws(1:ServerError e);

    // 收益
    // 返回值: 1 成功
    i16 profit(1:Transfer param) throws(1:ServerError e);

    // 银行卡管理
    // 申请变更
    // 返回值: 1 成功
    i64 card_change(1:CardChangeArgs change_args) throws(1:ServerError e);

    // 直接变更银行卡信息,目前暂只支持变更银行卡绑定的手机号
    // 返回值: 1 成功
    i64 card_modify(1:Card card_args) throws(1:ServerError e);

    // 申请变更查询
    CardChangeResp card_change_query(1:i64 userid) throws(1:ServerError e);
    // 查询银行卡信息
    list<Card> card_query(1:CardQueryArgs query_args) throws(1:ServerError e);

    // 费率管理
    // 保存费率信息 userid存在，则修改，不存在，则添加
    // 返回值: 1 成功
    i64 fee_ratio_save(1:FeeRatio fee_ratio) throws(1:ServerError e);
    // 查询费率信息
    list<FeeRatio> fee_ratio_query(1:FeeQueryArgs query_args) throws(1:ServerError e);
    // 查询费率数量, 与fee_ratio_query一起进行分页查询
    // 计算手续费
    Fee calculate_fee(1:CalculateFeeArgs cal_args) throws(1:ServerError e);

    //海外手续费设置
    i64 overseas_fee_ratio_save(1:OverseasFeeRatio overseas_fee_ratio) throws(1:ServerError e);
}
