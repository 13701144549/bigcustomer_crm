namespace py payquick_api


exception PayquickException {
    1: string 				respcd;				//异常码
    2: string 				respmsg;			//异常描述信息
}

// 实名认证状态
enum RealnameStatus {
    NEW=1,  // 新注册
    UPLOADED=10,  // 已上传实名信息
    FEERATIO_SET=20,  //已设置费率
    CHNLBIND=30,  // 已完成进件，以及通道配置
}

enum BANK_TYPE {
    PERSONAL=1,  // 对私
    CORPORATE=2,  // 对公
}

enum CardbindVerifyStatus {
    PASS=1,  // 通过
    FAILED=2,  // 未通过
    NOACTION=3,  // 未进行过校验
}

// 付款银行卡通道认证方式
enum CardbindVerifyMode {
    URL=1,  // URL
    HTML=2,  // HTML源代码
}

// 费率模式
enum FeeRatioMode {
    PERCENT=1,  // 百分比
    FIXED=2,  // 定额
    MIXED=3,  // 组合的
}

// 费率类型
enum FeeRatioType {
    QD_BASIC=1,  // 渠道成本费率
    QD_MCHNT_DEFAULT=2,  // 渠道商户默认费率
    MCHNT=3,  // 商户费率
}

// 积分类型
enum PointType {
    YES=1,  // 带积分
    NO=2,  // 不带积分
}

// 冻结状态
enum FreezeType{
    NO=1, //   未冻结
    YES=2, //   临时冻结
}

// 到账（清算）类型
enum SettleType {
    D0=1,
    D1=2,
    T0=3,
    T1=4,
}

// 封顶类型
enum FeeMaxType {
    NO=1,  // 不封顶
    YES=2, // 封顶
}

// 付款方式
enum PayMethod {
    SMS_CODE=1,  // 通过短信验证码 完成付款
    HTML=2,  // 渲染HTML 完成付款
    URL=3,  // 重定向到URL 完成付款
    NO_CODE=4, // 直接下单就可以支付, 无需验证码和付款链接
}

// 用户角色
enum UserRole {
    SALESMAN=1,  // 业务员
    MCHNT=2,  // 商户
}

// 查询元数据
struct QueryMeta {
    1: required i64             offset=0;           // 偏移, 默认从 0 开始
    2: required i64             count=100;          // 记录数, 默认 100 条
    3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

// 银行卡信息
struct Card {
    1: BANK_TYPE banktype;  // 银行账户类型。创建必传。
    2: string headbankname;  // 银行总行名称。 创建必传。如： 交通银行
    3: string bankname;  // 银行名称（支行名称）。 创建必传。如： 交通银行成都蜀汉路支行
    4: string bankuser;  // 银行开户姓名。创建必传。
    5: string bankaccount;  // 银行卡号。创建必传。
    6: string bankmobile;  // 银行卡预留手机号。创建必传。
    7: string brchbank_code;  // 开户行银联号。创建必传。
    8: string bankProvince;  // 开户行省份。创建必传。
    9: string bankCity;  // 开户行城市。创建必传。
}

// 实名信息
struct RealnameInfo {
//    1: required i64 id,  // 创建的时候填0
    2: i64 userid,  // USERID。创建必传。
    3: Card card,  // 结算银行卡信息。创建必传。
    4: string idnumber;  // 身份证号码。创建必传。
    5: string src;  // 商户来源，创建实名认证时传空。 创建不传，返回必在。快捷支付自主注册的src是 payquick.
    6: i16 status=RealnameStatus.UPLOADED;  // 实名认证状态，创建实名认证时传空。创建不传，返回必在。

    20: string idcard_front_url;  // 身份证正面照片URL。创建必传。
    21: string idcard_back_url;  // 身份证背面照片URL。创建必传。
    22: string bankcard_front_url;  // 银行卡正面照片URL。创建不传
}

// 好近商户开通快捷支付信息
struct HaojinRealnameArg {
    1: required i64 userid,  // USERID

    20: required string idcard_front_url;  // 身份证正面照片URL
    21: required string idcard_back_url;  // 身份证背面照片URL
    22: required string bankcard_front_url;  // 银行卡正面照片URL
}

// 付款银行卡绑定信息
struct CardBind {
    1: i64 id,  // 绑卡ID。创建不传，返回必在。
    2: i64 userid,  // 绑卡人USERID。创建必传。
    3: Card card,  // 付款银行卡信息。创建必传。
}

// 付款途径信息
struct Payway {
    1: i64 id,  // 付款途径ID。创建不传，返回必在。
    2: i64 chnlid,  // 对应qf_core.channel.id。创建必传。
    3: string title,  // 通道展示名称。创建必传。

    4: PointType point,  // 是否带积分。创建必传。
    5: SettleType settle_type,  // 到账（清算）类型。创建必传。
    6: FeeRatioMode fee_mode,  // 费率模式。创建必传。
    7: string info,  // 提示信息，展示给用户。创建必传
    8: string memo,  // 备注信息，展示给内部系统。创建必传。
    9: i64 enable,  // 是否启用。 创建必传。启用=1， 禁用=0。
    10: FeeMaxType max_type,  // 手续费封顶类型，不封顶=1，封顶=2。创建必传。
    11: FreezeType freeze_status,  //通道冻结状态
    12: string freeze_msg,   // 冻结信息

    20: i64 limit_amt_min,  // 最低交易金额，单位：分。创建必传
    21: i64 limit_amt_max,  // 最高交易金额，单位：分。创建必传
}

// 付款支付途径冻结
struct PaywayFreezeArg{
    1: required list<i64> payway_id_list,   //通道 id 列表
    2: required string freeze_msg,  // 冻结信息
}

// 付款支付途径解除冻结
struct PaywayUnFreezeArg{
    1: required list<i64> payway_id_list,   // 通道 id 列表
}

// 付款通道绑定信息
struct ChnlBind {
    1: i64 id,  // 通道绑定表ID。创建不传，返回必在。
    2: i64 userid,  // USERID。创建必传。
    3: i64 chnlid,  // 通道ID。创建必传。
    4: i16 available,  // 是否可用。创建不传，返回必在。  可用=1， 不可用=0
}

// 快捷支付手续费率
struct FeeRatio {
    1: i64 id,  // 费率ID。创建不传，返回必在。
    2: i64 userid,  // USERID。创建必传，不可修改。
    3: i64 payway_id,  // 支付途径ID，payway.id。创建必传，不可修改。
    4: FeeRatioType fee_type,  // 费率类型。创建必传
    5: string fee_percent,  // 百分比费率。如0.38%则传'0.0038'。创建必传(没有传'0.0')。
    6: i64 fee_fix,  // 定额费率。单位：分。创建必传(没有传0)。
    7: string memo,  // 备注信息。创建必传。
    8: i64 fee_max,  // 手续费封顶金额。单位： 分。创建必传（不封顶传0）
}

// 快捷支付商户关系
struct Relation {
    1: i64 id,  // 关系ID。创建不传，返回必在。
    2: i64 userid,  // USERID。创建必传，不可修改。
    3: i64 inviter_uid,  // 邀请人userid。创建必传，不可修改。
    4: UserRole inviter_role, // 邀请人角色。创建必传，不可修改。
    5: string memo,  // 备注信息。创建必传。
}

// 实名信息查询
struct RealnameQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
}

// 付款银行卡查询
struct CardBindQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
    3: optional list<string> bankaccount_list,  // 银行卡号列表
}

// 付款银行卡进行通道认证的参数
struct CardbindVerifyArg {
    1: required i64 userid,
    2: required i64 payway_id,
    3: required i64 cardbind_id,
    4: required string redirect_url,  // 认证完成后的重定向URL
}

// 付款银行卡进行通道认证的响应
struct CardbindVerifyRet {
    1: required CardbindVerifyMode mode,  // 认证模式： URL方式=1，HTML方式=2。
    2: required string info,  // 认证信息，存放URL或者HTML
    3: optional string extra,  // 扩展字段，json字符串
}

// 付款银行卡在通道的认证检查
struct CardbindVerifyCheckArg {
    1: required i64 userid,
    2: required i64 payway_id,  // 通道ID
    3: required i64 cardbind_id,  //
}

// 付款银行卡在通道的认证状态
struct CardbindVerifyCheckRet {
    1: required CardbindVerifyStatus status,  // 认证状态
    2: optional string message,  // 认证状态信息
}

// 通道绑定查询
struct ChnlBindQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
    3: optional list<i64> chnlid_list,
    4: optional i16 available,  // 是否可用。 可用=1，不可用=0
}

/* 通道创建返回参数 */
struct ChnlbindCreateRet {

}

// 快捷支付通道查询
struct PaywayQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> chnlid_list,  // 通道id列表
    3: optional list<i64> point_list, // 积分类型列表
    4: optional list<SettleType> settle_type_list,  // 清算类型列表
    5: optional list<FeeRatioMode> fee_mode_list,  // 费率模式列表
    6: optional i16 enable,  // 是否启用。 启用=1，禁用=0

    7: optional string title, // 标题搜索(支持模糊查询)
    8: optional list<FreezeType> freeze_status_list, // 冻结状态列表 1 是临时冻结 2 不冻结
    9: optional list<FeeMaxType> max_type_list, // 是否封顶 不封顶=1， 封顶=2
}

struct FeeRatioQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> payway_id_list,
    3: optional list<i64> userid_list,
    4: optional list<FeeRatioType> fee_type_list,  // 费率类型列表
}

struct FeeRatioSyncQudaoArg {
    1: required list<i64> mchnt_uid_list,
}

/* 同步费率到通道 请求 */
struct FeeRatioSync2ChnlArg {
    1: required list<i64> feeratio_id_list,  // 需要同步的费率ID列表
}
/* 同步费率到通道 响应 */
struct FeeRatioSync2ChnlRet {

}

// 商户关系查询参数
struct RelationQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> userid,  // 商户USERID
    3: optional list<i64> inviter_uid_list,  // 邀请人USERID
    4: optional list<UserRole> inviter_role_list,  // 邀请人身份
}

service PayquickServer {

    // 实名认证相关 //
    /*
    * 创建实名认证信息
    * @param info: 实名信息
    * @param admin: 操作发起者，没有传 0
    * @ret: 实名信息
    * */
    RealnameInfo realname_create(1:RealnameInfo info, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 实名信息查询
    * @ret userid列表
    * */
    list<i64> realname_query(1:RealnameQueryArg q) throws (1:PayquickException e);
    /*
    * 实名信息获取
    * @param l: userid列表
    * @ret: userid为key，实名信息为value
    * @attention:
    *   1. 如果包含不存在的userid，结果中不会包含
    * */
    map<i64, RealnameInfo> realname_get(1:list<i64> l) throws (1:PayquickException e);
    /*
    * 好近商户开通快捷支付功能
    * @attention
    *   1. 针对好近自有商户，补充资料信息
    *   2.
    * */
    RealnameInfo realname_haojin_create(1:HaojinRealnameArg info, 2:i64 admin) throws (1:PayquickException e);




    // 付款银行卡相关 //
    /*
    * 付款银行卡绑定
    * @param info: 付款银行卡绑定信息
    * @param admin: 操作发起者，没有传 0
    * @ret: 付款银行卡绑定信息
    * */
    CardBind cardbind_create(1:CardBind info, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 付款银行卡绑定信息查询
    * @param q: 查询参数
    * @ret: cardbind_id 列表
    * */
    list<i64> cardbind_query(1:CardBindQueryArg q) throws (1:PayquickException e);
    /*
    * 付款银行卡绑定信息获取
    * @param l: cardbind_id 列表
    *
    * */
    map<i64, CardBind> cardbind_get(1:list<i64> l) throws (1:PayquickException e);
    /*
    * 完成付款银行卡在通道的认证。
    * 例如：大则通道，需要先进行开卡操作。 */
    CardbindVerifyRet cardbind_verify(1:CardbindVerifyArg arg, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 银行卡在通道的认证状态检查。 */
    CardbindVerifyCheckRet cardbind_verify_check(1:CardbindVerifyCheckArg arg) throws (1:PayquickException e);




    // 通道绑定相关 //
    /*
    * 快捷支付通道绑定信息查询
    * @param q:
    * @ret: chnlbind_id列表。 qf_core.chnlbind.id
    * */
    list<i64> chnlbind_query(1:ChnlBindQueryArg q) throws (1:PayquickException e);
    /*
    * 快捷支付通道绑定信息获取
    * @param l: chnlbind_id列表。 qf_core.chnlbind.id
    * */
    map<i64, ChnlBind> chnlbind_get(1:list<i64> l) throws (1:PayquickException e);
    /*
    * 调用wft_merchant进行进件，进件完成后，wft_merchant会自动创建通道绑定。
    * 本接口为同步接口
    * */
    ChnlbindCreateRet chnlbind_create(1:ChnlBind info, 2:i64 admin) throws (1:PayquickException e);




    // 通道相关 //
    /*
    * 快捷支付通道信息创建
    * @param info: 快捷支付通道信息
    * @param admin: 操作发起者，没有传 0
    * */
    Payway payway_create(1:Payway info, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 快捷支付通道信息查询
    * @ret: payway_id列表。 payway.id
    * */
    list<i64> payway_query(1:PaywayQueryArg q) throws (1:PayquickException e);
    /*
    * 快捷支付通道信息获取
    * @ret: payway_id列表。 qf_payquick.payway.id
    * */
    map<i64, Payway> payway_get(1:list<i64> l) throws (1:PayquickException e);
    /*
    * 快捷支付通道更新相关
    * 冻结相关字段不传
    *
    * */
    Payway payway_update(1:Payway info, 2:i64 admin) throws(1:PayquickException e);
    /*
    * 快捷支付通道冻结接口
    * @ret: payway_id列表。 qf_payquick.payway.id
    */
    void payway_freeze(1: PaywayFreezeArg q, 2: i64 admin) throws(1:PayquickException e);
    /*
    * 快捷支付通道解除冻结接口
    * @ret: payway_id列表。 qf_payquick.payway.id
    */
    void payway_unfreeze(1: PaywayUnFreezeArg q, 2: i64 admin) throws(1:PayquickException e);



    // 费率相关 //
    FeeRatio feeratio_create(1:FeeRatio info, 2:i64 admin) throws (1:PayquickException e);

    list<i64> feeratio_query(1:FeeRatioQueryArg q) throws (1:PayquickException e);
    /*
    * 根据费率id，获取费率信息
    * @params l: feeratio_id列表,  feeratio表的id
    * */
    map<i64, FeeRatio> feeratio_get(1:list<i64> l) throws (1:PayquickException e);
    /*
    * 更新费率信息
    * @attention
    *   1. 更新的时候info必传id
    *   2. 更新的费率必须满足对应payway的fee_mode，否则会更新失败
    * */
    FeeRatio feeratio_update(1:FeeRatio info, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 商户费率和渠道同步
    * @param mchnt_uid_list: 商户的userid列表。 目前只能传入单个userid
    * @attention
    * @return 因费率同步产生的feeratio_id列表。
    * @action
    *   1. 对传入的arg.mchnt_uid_list中的所有商户，做一下动作：
    *     a. 如果商户没有配置某个payway的费率，则从该商户的渠道那里同步该payway的费率
    *     b. 如果商户配置了payway的费率，则跳过。
    * */
    list<i64> feeratio_sync_qudao(1:FeeRatioSyncQudaoArg arg, 2:i64 admin) throws (1:PayquickException e);
    /*
    * 同步费率到通道
    * */
    FeeRatioSync2ChnlRet feeratio_sync2chnl(1:FeeRatioSync2ChnlArg arg, 2:i64 admin) throws (1:PayquickException e);




    //// 商户关系相关 ////
    Relation relation_create(1:Relation info, 2:i64 admin) throws (1:PayquickException e);

    list<i64> relation_query(1:RelationQueryArg q) throws (1:PayquickException e);
    /*
    * 根据费率id，获取商户关系信息
    * @params l: relation_id列表,  relation表的id
    * */
    map<i64, Relation> relation_get(1:list<i64> l) throws (1:PayquickException e);


    // ping //
    void ping();
}
