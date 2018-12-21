namespace py withhold2

exception ServerError
{
    1: string code,
    2: string msg,
}

// 规则参数
struct Rule
{
    1: i32 userid,               //用户ID
    2: i32 withhold_type_id,     //扣款类型ID
    3: string title,             //title
    4: i64 withhold_rule_id,     //扣款规则ID
    5: i32 fact_amt,             //实扣金额
    6: i32 should_amt,           //应扣金额
    7: string withhold_month     //扣款月份
    8: string start_time,        //开始时间
    9: string end_time,          //结束时间
    10: i32 enable                //启用状态
    11: i32 finish               //完成状态 
}

service Withhold2
{
    //生成规则
    i32 create_rule(1:Rule rule) throws(1:ServerError e),

    //修改规则
    i32 change_rule(1:Rule rule) throws(1:ServerError e),

    //扣款指定的批次号
    i64 withhold() throws(1:ServerError e),

    //审核成功
    i32 audit_pass(1:i64 bat_id) throws(1:ServerError e),

    //审核拒绝
    i32 audit_refuse(1:i64 bat_id) throws(1:ServerError e),
}
