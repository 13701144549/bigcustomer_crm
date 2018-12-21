namespace py cashdraw

// 交易状态码
enum TradeStatus
{
    PROCESSING=0, // 交易中
    SUCCESS=1,  // 成功
    FAILED=2,     // 失败
    REFUNDED=3,   // 已退款(已退汇）
}

// 批次状态码
enum BatchStatus
{
    PROCESSING=0, // 交易中
    SUCCESS=1,  // 成功
    FAILED=2,     // 失败
}

// 账户类型
enum AccountType
{
    DEBIT=0,            // 借记卡
    CREDIT=1,           // 信用卡（贷借卡）
    CORPORATE=2,        // 对公
}


// 代付类型, 仅内部记录使用
enum TradeType
{
//    Single=1,  // 单笔代付
    Batch=2,   // 批量代付
}

service cashdraw
{
    ////////  实时代付相关 /////////
    // 单笔代付  暂不支持
    // SinglePayResult single_pay(1:PayArg arg) throws(1:CashdrawError e);  // 返回json字符串

    ////////  批量代付相关 /////////
    // 批量代付
//    BatchResult batch_pay(1:BatchPayArg arg) throws(1:CashdrawError e);
//    BatchResult batch_query(1:BatchQueryArg arg) throws(1:CashdrawError e);


    string ping();
    string trade(1: string req);
}
