namespace py FundSuspend

//通用返回
struct FundSuspendReturn{
    1: required string respcd,
    2: required string respmsg,
}

//添加风控记录参数
struct RiskRecord {
    1: required i64 userid,       #用户id
    2: required i16 hand_type,    #1:风控延迟， 2:风控释放
    3: required i64 amt,          #金额
    4: required i64 tag,          #标签
    5: required string sn,        #流水号
    6: required string txcurrcd,  #币种
    7: required i16 risk_type,    #1:按用户延迟,2:按金额延迟,3:按交易延迟
    8: required string memo,      #备注
}

service FundSuspendService {
    //ping
	FundSuspendReturn ping(),
    
    //生成延迟纪录  ----->参数 txcurrcd 币种  hand_type 操作类型(1 延迟 2释放延迟) src(1 账务  2风控)
    oneway void gen_suspend_records(1:required string txcurrcd,2:required i16 hand_type, 3:required i16 src),

    //生成延迟纪录  ----->参数 txcurrcd 币种  hand_type 操作类型(1 延迟 2释放延迟) userids(用户id串)
    oneway void add_suspend_records(1:required string txcurrcd,2:required i16 hand_type, 3:required string userids),

    //添加风控延迟纪录
    oneway void add_risk_records(1:required RiskRecord riskdata),

    //审核操作延迟纪录
    FundSuspendReturn audit_suspend_records(1:required i64 batid,2:required i16 hand_state),

}
