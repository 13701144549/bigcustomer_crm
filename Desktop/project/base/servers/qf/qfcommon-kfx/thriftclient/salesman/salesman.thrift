namespace py salesman

exception SalesmanException {
    1: string 				respcd;				//异常码
    2: string 				respmsg;			//异常描述信息
}

// 消息发送类型
enum MessageSendType {
    INSTANT=1,   // 立即发送
    TIMING=2,  // 定时发送
}

// 消息发送状态
enum MessageSendStatus {
    PENDING=1,  // 未发送
    DONE=2,   // 已发送
}

// 消息阅读状态
enum MessageReadStatus {
    UNREAD=1,   // 未读
    READ=2,     // 已读
}

// 消息绑定状态
enum MessageBindStatus {
    BIND=1,         // 绑定
    UNBIND=2,     // 未绑定
}

// 发送目标指定方式
enum MessageSpecType {
    ALLUSERS =1,        // 所有用户
    UPLOADFILE =2,      // 上传文件
    CUSTOM = 3          // 自定义
}

// 消息状态
enum MessageStatus {
    ENABLE=1,   // 启用
    DISABLE=2,  // 禁用
}

// 消息是否开启PUSH通知
enum MessagePush {
    ENABLE=1,   // 启用
    DISABLE=2,  // 禁用
}

// 消息
/*
:attention:
   title, brief, content, ispush, send_type, send_time, slsm_uids, spec_type 创建消息时必传
*/
struct Message {
    1:  i64                 message_id;
    2:  string              title;
    3:  string              brief;
    4:  string              content;
    5:  MessagePush         ispush;  //是否通过push通知
    6:  MessageSendType     send_type;
    7:  string              send_time;
    8:  string              create_time;
    9:  string              pushlink;
    10: MessageStatus       status;
    11: MessageSendStatus   send_status;
    12: MessageSpecType     spec_type;
}

// 消息-业务员 绑定关系
/*
:attention:
   slsm_uid, message_id 创建绑定关系时必传
*/
struct MessageBindInfo {
    1:  i64                 bind_id;
    2:  i64                 slsm_uid;
    3:  i64                 message_id;
    4:  MessageReadStatus   read_status;
    5:  MessageBindStatus   bind_status;
    6:  string              create_time;
}

// 查询元数据
struct QueryMeta {
    1: required i64             offset=0;           // 偏移, 默认从 0 开始
    2: required i64             count=100;          // 记录数, 默认 100 条
    3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

struct MessageQueryArg {
    1: required QueryMeta           query_meta;
    2: optional list<i64>           message_ids;
    3: optional string              title;
    4: optional MessagePush         ispush;
    5: optional string              create_start_time;
    6: optional string              create_end_time;
    7: optional string              send_start_time;
    8: optional string              send_end_time;
    9: optional MessageSendStatus  send_status;
    10: optional MessageStatus      status;
}

struct MessageBindQueryArg {
    1: required QueryMeta           query_meta;
    2: optional list<i64>           bind_ids;
    3: optional list<i64>           slsm_uids;
    4: optional list<i64>           message_ids;
    5: optional MessageReadStatus   read_status;
    6: optional MessageBindStatus   bind_status;
    7: optional string              create_start_time;
    8: optional string              create_end_time;
}

service SalesmanServer {

    ///////////////
    // 消息相关  //
    ///////////////

    // 创建消息
    i64 message_create(1:Message msg, 2:i64 admin) throws (1:SalesmanException e);
    // 查询消息信息， 返回消息id
    list<i64> message_query(1:MessageQueryArg q) throws (1:SalesmanException e);
    // 查询满足条件的消息条数
    i64 message_query_count(1:MessageQueryArg q) throws (1:SalesmanException e);
    // 查询消息
    list<Message> message_get(1:list<i64> message_ids) throws (1:SalesmanException e);
    // 设置消息状态
    void message_set_status(1:list<i64> message_ids, 2:MessageStatus status, 3:i64 admin) throws (1:SalesmanException e);
    // 更新消息（未发送）
    void message_update(1:map<i64, Message> message, 2:i64 admin) throws (1:SalesmanException e);

    // 创建消息绑定关系
    list<i64> message_bind_create(1:list<MessageBindInfo> bind_infos, 2:i64 admin) throws (1:SalesmanException e);
    // 查询消息绑定关系， 返回绑定id
    list<i64> message_bind_query(1:MessageBindQueryArg q) throws (1:SalesmanException e);
    // 查询满足条件的绑定关系数量
    i64 message_bind_query_count(1:MessageBindQueryArg q) throws (1:SalesmanException e);
    // 获取消息绑定关系
    list<MessageBindInfo> message_bind_get(1:list<i64> bind_ids) throws (1:SalesmanException e);
    // 设置绑定关系的状态
    void message_bind_set_status(1:list<i64> bind_ids, 2:MessageBindStatus status, 3:i64 admin) throws (1:SalesmanException e);
    // 修改绑定关系信息
    void message_bind_update(1:map<i64, MessageBindInfo> bind_info, 2:i64 admin) throws (1:SalesmanException e);
}
