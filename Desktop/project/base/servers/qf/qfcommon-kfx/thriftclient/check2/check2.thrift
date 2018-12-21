namespace py check2

// 发生错误时的返回码及其对应的描述信息
exception ServerError
{
    1: string code, // 返回码
    2: string msg,  // 描述信息
}

// 差错处理参数
struct MistakeHandleArgs
{
    1: i64    id,
    2: i32    result,
    3: string memo,
}

service Check2
{
    i16 ping();
    // 创建对账批次
    i64 create_bat(1:i32 chnl_id, 2:required string date) throws(1:ServerError e);
    // 下载通道流水
    i32 download_chnlrecord(1:i64 bat_id) throws(1:ServerError e);

    // 导入通道流水
    i32 import_chnlrecord(1:i64 bat_id) throws(1:ServerError e);

    // 导入业务流水
    i32 import_bizrecord(1:i64 bat_id) throws(1:ServerError e);

    // 对账
    i32 check(1:i64 bat_id) throws(1:ServerError e);

    // 差错处理
    i32 mistake_handle(1:list<MistakeHandleArgs> params) throws(1:ServerError e);

    // result: 3:审核成功, 4:审核失败
    // 通道对账审核
    i32 audit(1:i64 bat_id, 2:i32 result) throws(1:ServerError e);
}
