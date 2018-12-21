namespace py remit2

exception ServerError
{
    1: string code,
    2: string msg,
}

struct RemitBackArgs
{
    1: i64 bat_id   //退票批次号
    2: string start_time   
    3: string end_time
}

service Remit2
{
    //根据结算类型ID和交易时间生成批次
    i64 create_remit_bat(1:i64 remit_type_id, 2:i64 account_type_id) throws(1:ServerError e),

    //结算指定的批次号
    i32 remit(1:i64 bat_id) throws(1:ServerError e),

    //出款审核成功
    i32 remit_audit_pass(1:i64 bat_id) throws(1:ServerError e),

    //出款审核拒绝
    i32 remit_audit_refuse(1:i64 bat_id) throws(1:ServerError e),

    //生成excel文件
    i32 generate_excel(1:i64 bat_id) throws(1:ServerError e),

    //创建退票批次
    i64 create_remitback_bat(1:i64 remitback_type_id) throws(1:ServerError e),

    //根据批次、出款批次和excel文件解析生出出款明细
    i32 remitback(1:RemitBackArgs remit_back_args) throws(1:ServerError e),

    //退票审核通过
    i32 remitback_audit_pass(1:i64 bat_id) throws(1:ServerError e),

    //退票审核拒绝
    i32 remitback_audit_refuse(1:i64 bat_id) throws(1:ServerError e),
}
