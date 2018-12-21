namespace py wxcard

// 错误码
enum ERRCODE{
    INNER_SERVICE_ERR=9500,     // 系统内部错误
    ACS_TOKEN=9501,             // ACCESS_TOKEN错误
    EVENT_ERR=9502,             // 通知事件异常
    THIRD_CALL_ERR=9503,        // 第三方调用失败
    DATA_ERR=9504,              // 数据无效
    DB_ERR=9505,                // DB错误
    PARAM_ERR=9506,             // 参数错误
    UNKNOWN_ERR=9506,           // 未知错误
    UPIMG_ERR=9507,             // 上传图片错误
}

// 发生错误时的返回码及其对应的描述信息
exception WXCardError
{
    1: i64 respcd, // 返回码
    2: string respmsg,  // 描述信息
}

// 商户审核状态
enum MerchantStatus{
    CREATED = -1, // 记录创建完成
    CHECKING = 0, // 审核中
    APPROVED = 1, // 审核通过
    REJECTED = 2, // 被驳回
    EXPIRED=3,    // 协议已过期
    SUBMIT_ERR=4, // 提交失败
}

// 卡套状态
enum CardtplStatus {
    CREATED = -1, // 记录创建完成
    CHECKING = 0,    // 审核中(提交成功)
    PASS=1,          // 审核通过
    NOT_PASS = 2,    // 审核未通过
    SUBMIT_ERR=3,    // 提交失败
}

// 卡的状态
enum CardStatus{
    CREATED = -1, // 记录创建完成
    GOT_BUG_NOT_SYNC = 0,  // 已领取未同步信息
    GOT_AND_SYNC = 1,      // 已领取已同步信息
}

// 卡激活的状态
enum CardActivateStatus{
    UNACTIVATED = 0     // 未激活
    ACTIVATED = 1       // 已激活
}

// 激活方式
enum CardActivateWay{
    AUTO_ACTIVATE = 0        //  自动激活
    INTERFACE_ACTIVATE = 1   //  接口激活
}

// 卡类型
enum CardType
{
    MEMBER_CARD =1, // 会员卡
}

// 微信会员卡体系中的 商户
struct Merchant {
    1: required i64 id,                      // merchant表的ID。注册时填0
    2: required i64 userid,                  // 钱方USERID
    3: required i64 merchant_id,             // 微信子商户ID。 注册时填0
    4: required string wx_appid,             // 创建子商户的公众号主体
    5: required MerchantStatus status,       // 当前状态。    注册时填-1(CREATED)
    6: required string reason='',            // 状态描述 或 失败原因。
    7: required bool cachet,                 // 是否带公章，带公章为true不带为false
    8: optional string ctime,                // 创建时间

   10: required string brand_name,           // 子商户名称
   11: required string logo_url,             // 子商户logo
   12: required string protocol_url,         // 授权函id
   13: required string end_time,             // 授权函有效截止时间
   14: required i64 primary_category_id,     // 一级类目id
   15: required i64 secondary_category_id,   // 二级类目id
   16: optional string app_id,               // 子商户的公众号app_id，即子商户自己的公众号，可以在会员卡中展示
   17: optional string agreement_media_url,   // 营业执照或个体工商户营业执照彩照或扫描件
   18: optional string operator_media_url,    // 营业执照内登记的经营者身份证彩照或扫描件
   19: optional string background_pic_url,    // 背景图
}

// 微信会员卡体系中的 卡套，当商户审核通过后，由本系统自动创建
struct CardTpl{
    1: required i64 userid,                  // 钱方USERID
    2: required i64 merchant_id,             // 微信子商户ID
    3: required string card_id,              // 微信卡套ID
    4: required CardType card_type,          // 卡类型
    5: required string info,                 // 创建卡套的各种信息
    6: required CardtplStatus status,        // 卡套的状态
    7: required string ctime,                // 创建时间
    8: required string wx_appid,             // 制卡的主体公众号。 即提交商户资料时使用的公众号appid, 商户自己的appid在info中查询。
    9: required i64 id,                      // cardtpl表的id.  历史遗留原因放在这里
}

// 微信会员卡体系中的 会员卡, 当卡套审核通过后，可由消费者自主领取等（多种发卡方式见微信官方文档）。
struct Card{
    1: required i64 id,                     // card表的id
    2: required i64 userid,                 // 钱方USERID
    3: required i64 cid,                    // 钱方CID
    4: required CardType cardtype,          // 卡类型
    5: required string card_id,             // 微信卡套ID
    6: required CardStatus status,          // 卡状态
    7: required string reason='',            // 状态描述 或 失败原因。

    10: required string card_owner,          //
    11: required string card_code,           // 微信生成的卡序列号
    12: required string card_no,             // 钱方卡号
    // and more...
}

// 查询元数据
struct QueryMeta {
    1: required i64             offset=0;           // 偏移, 默认从 0 开始
    2: required i64             count=100;          // 记录数, 默认 100 条
    3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

struct MerchantQueryArg{
    1: required QueryMeta query_meta,      // 查询元数据
    2: optional list<i64> userids,         // 钱方USERID
    3: optional list<i64> merchant_ids,    // 微信返回的子商户ID
    4: optional list<string> wx_appids,    // 进件子商户的主体公众号
//    5: optional list<string> appids,       // 子商户绑定的公众号. 暂不支持
    6: optional list<MerchantStatus> status,     // 子商户号审核状态
    7: optional string s_ctime,           // 创建时间的开始
    8: optional string e_ctime,           // 创建时间的结束
    9: optional string s_utime,           // 更新时间的开始
    10: optional string e_utime,           // 更新时间的结束
}

struct CardtplQueryArg{
    1: required QueryMeta query_meta,
    2: optional list<i64> userids,          // 钱方USERID
    3: optional list<string> cardids,       // 微信卡套ID
    4: optional list<i64> mchnt_ids,        // 微信子商户ID
    5: optional CardtplStatus status,       // 卡套状态
}

struct CardQueryArg{
    1: required QueryMeta query_meta,    // 查询元数据
    2: optional list<string> card_nos,    // 钱方卡号
    3: optional list<string> card_ids,    // 微信卡套ID
    4: optional list<i64> cids,          // 钱方CID
    5: optional list<i64> userids,       // 钱方USERID
    6: optional list<CardStatus> status,       // 卡状态
    7: optional string s_ctime,        // 创建时间的开始
    8: optional string e_ctime,        // 创建时间的结束
    9: optional string s_utime,        // 更新时间的开始
   10: optional string e_utime,        // 更新时间的结束
}



// 接收公众号事件的数据结构
struct MPEvent
{
    1: required string appid,       // 微信公众号的appid
    2: required string data,        // 事件通知的数据
}

// 微信会员卡更新数据信息
struct CardtplUpdateInfo
{
    2: optional string logo_url,             // 卡券的商户logo
    3: optional string background_pic_url,   // 会员卡自定义卡面背景图
}

// 商户更新数据信息
struct MerchantUpdateInfo
{
    1: optional string brand_name,           // 子商户名称
    2: optional string logo_url,             // 子商户logo
    3: optional string protocol_url,             // 授权函ID
    4: optional i64 end_time,                // 授权函有效期截止时间
    5: optional i64 primary_category_id,     // 一级类目id
    6: optional i64 secondary_category_id,   // 二级类目id
    7: optional string app_id,               // 子商户的公众号app_id
    8: optional string agreement_media_url,   // 营业执照或个体工商户营业执照彩照或扫描件
    9: optional string operator_media_url,    // 营业执照内登记的经营者身份证彩照或扫描件
}

// 手动制卡数据信息
struct CardtplManualMakeInfo
{
    1: required i64 userid,                   // 商户ID
    2: required i64 merchant_id,               // 微信子商户ID
}

// 会员卡接口激活数据信息(点击激活按钮url后带的参数)
struct CardInterfaceActiveInfo
{
    1: required string card_id                       // 卡套编号
    2: required string encrypt_code                  // 加密码码
    3: required string openid                        // 领取人ID
}

service WXCard{
    i64 ping();

    // 接收事件通知
    string auth_event(1: MPEvent me);
    string realname_event(1: MPEvent me);

    // 商户相关
    // 提交制卡商户信息
    Merchant merchant_create(1:Merchant merchant, 2:i64 admin) throws(1:WXCardError e);

    // 返回merchant表的id
    list<i64> merchant_query(1:MerchantQueryArg q) throws(1:WXCardError e);

    // 查询满足条件的商户数量
    i64 merchant_query_count(1:MerchantQueryArg q) throws(1:WXCardError e);

    /*
      通过merchant表id，获取Merchant
    */
    list<Merchant> merchant_get(1:list<i64> merchant_ids) throws(1:WXCardError e);

    // 更新商户信息
    void merchant_update(1:map<i64, MerchantUpdateInfo> merchant_info, 2:i64 admin) throws(1: WXCardError e);


    // 卡套相关
    /*
       查询用户提交的卡套详情
       :attention:
         1. 查询条件不可同时都为空
         2. 排序支持根据ctime
         3. 历史遗留原因，返回的是CardTpl的list
    */
    list<CardTpl> cardtpl_query(1:CardtplQueryArg q) throws(1: WXCardError e);

    // 查询满足条件的卡套数量
    i64 cardtpl_query_count(1:CardtplQueryArg q) throws(1: WXCardError e);

    /*
     通过cardtpl表id，获取CardTpl
    */
    list<CardTpl> cardtpl_get(1:list<i64> cardtpl_ids) throws(1: WXCardError e);

    // 卡套更新
    void cardtpl_update(1:map<i64, CardtplUpdateInfo> cardtpl_update_info, 2:i64 admin) throws(1: WXCardError e);

    // 手动制卡
    void cardtpl_manual_make(1:CardtplManualMakeInfo c, 2:i64 admin) throws(1: WXCardError e);


    // 卡相关
    // 返回card表的id
    list<i64> card_query(1:CardQueryArg q) throws(1: WXCardError e);

    // 查询满足条件的卡套数量
    i64 card_query_count(1:CardQueryArg q) throws(1: WXCardError e);

    /*
      通过card表id，获取Card
    */
    list<Card> card_get(1:list<i64> card_ids) throws(1: WXCardError e);

    // 会员卡接口激活
    void card_interface_active(1: CardInterfaceActiveInfo c, 2:i64 admin) throws(1: WXCardError e);

    // 卡券投放, 返回的是{"succ_mchid_list": [], "fail_mchid_list": []}字符串
    string pay_gift_card(1: string card_id) throws(1: WXCardError e);

    // 返回用户卡包里的属于执行appid下的所有可用卡券
    list<string> get_card_list(1: string openid, 2: string appid) throws(1: WXCardError e);

    // 根据用户的openid和会员卡的card_id获取用户在领卡时候微信给分配的code
    string get_cardcode_by_openid(1: string openid, 2: string card_id) throws(1: WXCardError e);

}
