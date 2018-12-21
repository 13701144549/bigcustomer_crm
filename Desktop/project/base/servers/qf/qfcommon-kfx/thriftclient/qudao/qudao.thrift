namespace py qudao


exception QudaoException {
    1: string 				respcd;				//异常码
    2: string 				respmsg;			//异常描述信息
}

// 渠道状态
enum QudaoStatus {
    ENABLE=0,           // 启用
    DISABLE=1,          // 禁用
    DELETED=2,          // 注销
}

// 渠道类型
enum QudaoType {
    BAIPAI=1,           // 白牌
    LIANMING=2,         // 联名
    PARTNER=3,          // 合伙人
    DIRECT=4,           // 直营
    QIANTAI=5,          // 钱台
    TELEMARKET=6,       // 网络电销
    OVERSEAS=7,          // 海外
    DAWANQU=8,           // 大湾区
    BANK_COOPERATION=9,  // 银行合作部
    ADVERTISE=10,        // 广告
}

// 结算类型
enum SettleCycle {
    REALTIME = 1,  // 实时
    MONTHLY = 2,  // 月结
    QUARTERLY = 3,  // 季度结
}

// 渠道增值产品开通状态
enum ProductStatus {
    ENABLE = 0,  // 已开通
    DISABLE = 1,  // 未开通
}

// 渠道增值产品产品类别
enum ProductCate {
    TRADE_TYPE = 1,     // 交易类型
    ACTIVITY = 2,       // 活动
}

enum MchntStatus {
    ENABLE=0,   // 启用
    DISABLE=1,  // 禁用
}

enum SlsmStatus {
    ENABLE=0,   // 启用
    DISABLE=1,  // 禁用
}

enum AnnounceStatus {
    ENABLE=0,   // 启用
    DISABLE=1,  // 禁用
}


// 外部模块入口状态
enum EntranceStatus {
    ENABLE = 1,  // 开启
    DISABLE = 2,  // 关闭
}

//开户网点（用户银行）基本信息
struct BankInfo{
    1: required string			headbankname;		        //所属总行名称
    2: required string			bankuser;			//网点开户名
    3: required string			bankaccount;		        //网点账户号
    4: required i32			    banktype=1;			//账户类型，1，为对私，2为对公
    5: optional string			bankname;			//网点名称（支行名称）
    6: optional string			bankcode;			//网点联行号
    7: optional string			bankProvince = "";	        //支行所属省份
    8: optional string			bankCity = "";		        //支行所属城市
    9: optional string			bankmobile= "";		        // 银行预留手机号
}

// 渠道基本信息
struct QudaoBaseInfo {
    1: required i64             qd_uid;             // 渠道的用户ID
    2: required string          email;              // 注册邮箱
    3: required string          mobile;             // 手机号
    4: required string          password;           // 密码
    5: required QudaoStatus     status;             // 渠道状态, 启用/禁用
    6: required QudaoType       type;               // 渠道类型
    7: optional i64             parent;             // 父渠道
    8: optional i16             level;              // 渠道层级
    9: optional i64             slsm_uid;           // 所属业务员的用户ID
    10: optional string         slsm_mobile;        // 所属业务员的手机号
    11: optional string         join_dtm;          // 注册时间, 形如: '2016-01-02 12:22:33'
    12: optional string         username;          //登录名
}

/* 渠道资料 */
struct QudaoProfile {
    1: required i64             qd_uid;                  // 渠道的用户ID
    2: required string          name="",                 // 渠道名称
    3: required string          short_name="",           // 渠道简称
    4: optional string          legal_name,              // 法人姓名
    5: optional string          legal_idnumber,          // 法人身份证号码

    6: optional string			province;                // 所在省份
    7: optional string			city;                    // 所在城市
    8: optional string			address;                 // 商户地址

    9: optional string          business_name;           // 业务联系人姓名
    10: optional string         business_mobile;         // 业务联系人手机号
    11: optional string         business_email;          // 业务联系人邮箱
    12: optional string         finance_name;            // 财务联系人姓名
    13: optional string         finance_mobile;          // 财务联系人手机号
    14: optional string         finance_email;           // 财务联系人邮箱

    15: optional string         logo_url;                // 企业LOGO的URL
    16: optional string         icon_url;                // 企业LOGO的URL
    17: optional string         business_license_url;    // 企业LOGO的URL
    18: optional string         bank_account_url;        // 企业LOGO的URL

    19: optional string         country;                 // 国家
    20: optional string         auth_province;           // 授权省份, 废弃
    21: optional string         auth_city;               // 授权城市, 废弃
    22: optional string         timezone;                // 时区, 形如 +0800 的格式
    23: optional string         currency;                // 币种

    24: optional string         manager_name;            // 渠道经理姓名
    25: optional string         manager_mobile;          // 渠道经理手机号
    26: optional string         service_manager_name;    // 渠道服务经理姓名
    27: optional string         service_manager_mobile;  // 渠道服务经理电话号(可能是座机号)
    28: optional string         mobile;                 // 渠道手机号
}

// 结算信息
struct AccountInfo {
    1: required SettleCycle settle_cycle;  // 结算方式
    2: required i64 settle_base_amt;       // 起结金额
    3: required double wechat_fee;         // 微信费率
    4: required double alipay_fee;         // 支付宝费率
    5: required double jd_fee;             // 京东费率
    6: required double qqwallet_fee;       // QQ 钱包费率
    7: required double swipecard_fee;      // 刷卡费率
    8: optional double default_mchnt_fee;  // 商户默认费率
    9: optional string royalty_rule_id;    // 分润规则 id
}

/* 增值产品 */
struct ProductItem {
    1: required i64             id;             // 产品id
    2: required string          name;           // 产品名称
    3: required string          intro;          // 产品简介
    4: required i16             available;      // 该产品是否可用
    5: required string          memo='';        // 备注
    6: optional ProductStatus   status;         // 是否已开通
    7: optional ProductCate     cate;           // 产品类型
}

/* 授权区域 */
struct AuthArea {
    1: required string          province;     // 省
    2: required string          city='';      // 市
    3: required string          county='';    // 区县
}

// 渠道
struct QudaoUser {
    1: required i64 uid;        // 渠道用户ID
    2: required QudaoBaseInfo base_info;         // 基本信息
    3: required QudaoProfile profile;       // 渠道资料
    4: required BankInfo bank_info;         // 渠道开户银行信息
    5: required AccountInfo account_info;
    6: required list<ProductItem> product_list;     // 开通的增值产品列表
    7: required list<AuthArea> auth_areas;   // 授权区域列表
}

// 渠道业务员
struct SlsmUser {
    1: required i64        slsm_uid;  // 渠道业务员用户id
    2: required i64        qd_uid;    // 渠道id
    3: optional string     memo;      // 渠道业务员备注
    4: optional SlsmStatus status;    // 业务员状态
    5: optional string     join_dtm;  // 业务员注册时间
}

// 渠道商户
struct MchntUser {
    1: required i64 mchnt_uid;    // 渠道商户用户id
    2: required i64 slsm_uid;     // 渠道业务员用户id
    3: required i64 qd_uid;       // 渠道id
    4: required string memo;      // 商户备注
    5: optional string join_dtm;  // 商户注册时间
    6: optional i16 audit_status;     // 商户审核状态, 审核中=-1,拒绝=0,成功=1,失败=2
    7: optional string audit_memo;       // 审核原因
    8: optional string audit_dtm;        // 审核时间
}

// 查询元数据
struct QueryMeta {
    1: required i64             offset=0;           // 偏移, 默认从 0 开始
    2: required i64             count=100;          // 记录数, 默认 100 条
    3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

// 渠道查询参数
struct QudaoQueryArg {
    1: required QueryMeta       query_meta;         // 查询元数据
    2: optional i64             parent_uid;         // 父渠道
    3: optional string          name;               // 渠道名称, 支持模糊查询
    4: optional QudaoStatus     status;             // 渠道状态
    5: optional string          s_join_dtm;         // 最早注册时间. 形如: '2016-01-02 12:22:33'
    6: optional string          e_join_dtm;         // 最晚注册时间. 形如: '2016-01-30 12:22:33'
    7: optional list<QudaoType> types;              // 渠道类型列表
    8: optional string          auth_areas;         // 授权城市，支持模糊查询
    9: optional list<QudaoStatus> statuses;         // 渠道状态list
    10: optional list<string>   countrys;           // 渠道所属国家
}

// 渠道商户查询参数
struct MchntQueryArg {
    1: required QueryMeta       query_meta;         // 查询元数据
    2: optional list<i64>       qd_uids;            // 渠道商户所属渠道的用户id
    3: optional list<i64>       slsm_uids;          // 渠道商户所属渠道业务员的用户id
    4: optional list<i64>       mchnt_uids;         // 渠道商户id
    5: optional string          s_join_dtm;
    6: optional string          e_join_dtm;
    7: optional list<i16>       audit_statuses;     // 审核状态
    8: optional string          s_audit_dtm;        // 起始审核时间
    9: optional string          e_audit_dtm;        // 结束审核时间
}

// 渠道业务员查询参数
struct SlsmQueryArg {
    1: required QueryMeta       query_meta;         // 查询元数据
    2: optional list<i64>       qd_uids;            // 渠道业务员所属的渠道的用户id
    3: optional list<i64>       slsm_uids;
    4: optional SlsmStatus      status;
    5: optional string          s_join_dtm;
    6: optional string          e_join_dtm;
}

// 增值产品查询参数
struct ProdQueryArg {
    1: required QueryMeta           query_meta;         // 查询元数据
    2: optional list<i64>           product_ids;         // 产品id
    3: optional list<ProductCate>   cates;         // 产品类别
}

// 商户注册完成的回调函数 参数
struct MchntRegisteredArg {
    1: required i64             mchnt_uid;      // 渠道商户用户id
    2: required i64             slsm_uid;       // 渠道业务员用户id， 注册这个商户的业务员.
    3: optional i16             audit_status;   // 商户审核状态
    4: optional string          audit_memo;
    5: optional string          audit_dtm;
}

// 商户注册完成的回调函数 结果
struct MchntRegisteredRet {
    1: required i64             top_qd_uid;     // 该商户所属的一级渠道用户id, 交易系统应存储这个作为groupid
    2: required i64             qd_uid;         // 该商户直属的渠道用户id， 交易系统无需关心
}

// 业务员注册完成的回调函数 参数
struct SlsmRegisteredArg {
    1: required i64             slsm_uid;       // 渠道业务员用户id
    2: required i64             qd_uid;         // 该业务员所属的渠道用户id
}

// 业务员注册完成的回调函数的 结果
struct SlsmRegisteredRet {
    1: required i64             top_qd_uid;     // 该商户所属的一级渠道用户id, 交易系统应存储这个作为groupid
    2: required i64             qd_uid;         // 该渠道业务员直属的渠道用户id
}

// 公告消息
struct Announcement {
    1: required i64            announce_id=0;
    2: required string         title;
    3: required string         content;
    4: required string         create_time;
    5: required i16            istop=0;
    6: required AnnounceStatus status=AnnounceStatus.ENABLE;
    7: required i16            type=0;
    8: required i64            owner;          // 创建公告的 userid.
}

struct QueryAnnounceArg {
    1: required QueryMeta       query_meta;
    2: optional i64             qd_uid=0;
    3: optional AnnounceStatus  status=AnnounceStatus.ENABLE;
}

// 分润规则
struct RoyaltyRuleItem {
    1: required i64 min_trade_cnt;  // 最小交易笔数
    2: required i64 max_trade_cnt;  // 最大交易笔数
    3: required double discount;    // 费用折扣
}

struct RoyaltyRule {
    // 规则 id, 应该为 i64 类型, 但由于 qd_account 表中规则 id 已经是 varchar 类型, 因此这里转为string返回.
    1: required string id;  
    2: required string name;
    3: required list<RoyaltyRuleItem> rules;
    4: required i64 min_trade_amt;
    5: optional string memo;
}

struct RoyaltyRuleQueryArg {
    1: required QueryMeta query_meta;
    2: optional list<string> rule_ids;
    3: optional string name;
    4: optional i64 min_trade_amt;
}

struct TrainingFile {
    1: required i64 id;
    2: required string name;
    3: required string link;
    4: required string memo;
    5: required string create_time;
    6: required i16 status;
}

struct TrainingFileQueryArg {
    1: required QueryMeta query_meta;
    2: optional list<i64> ids;
    3: optional string name;
    4: optional i16 status;
}

// 商圈类型
enum RegionType {
    BUSINESS_REGION=1,              // 商业区
    HIGHTECH_REGION=2,              // 高新区
    OFFICE_BUILDING=3,              // 写字楼
    COMMERCIAL_STREET=4,            // 商业街
    FOOD_STREET=5,                  // 餐饮街
    COMPREHENSIVE_REGION=6,         // 混合型
    SCENIC_REGION=7,                // 景区
    RESIDENTIAL_REGION=8,           // 居住区
}

// 商圈开放程度
enum RegionOpenness {
    OPEN=1,         // 开放型
    SEMIOPEN=2,     // 半开放型
    GATED=3,        // 封闭型
}

//商圈
/*
:attention:
   name, province, city, type, openness 创建商圈时必传
*/
struct Region{
    1:  i64             id;             //商圈id.
    2:  string          name;           //商圈名称
    3:  string          province;       //商圈所在省
    4:  string          city;           //商圈所在市
    5:  RegionType      type;           // 商圈类型
    6:  RegionOpenness  openness;       //商圈开放程度
    7:  string          create_time;    //创建时间
    8:  i16             status;         //商圈状态: 0 正常 1 冻结
    9:  i16             audit_status;   //商圈审核状态: 审核中=0, 拒绝=1, 成功=2
    10: i64             qd_uid;         //创建此商圈的userid
    11: string          qd_name;        //创建此商圈的渠道全称
}

struct RegionQueryArg {
    1: required QueryMeta               query_meta;             // 查询元数据
    2: optional list<i64>               ids;                    // 商圈id
    3: optional string                  name;                   //商圈名称,支持模糊查询
    4: optional string                  province;               //商圈所在省,支持模糊查询
    5: optional string                  city;                   //商圈所在市，支持模糊查询
    6: optional list<RegionType>        type;                   //商圈类型
    7: optional list<RegionOpenness>    openness;               //商圈开放程度
    8: optional list<i16>               status;                 //商圈状态,0 正常 1 冻结
    9: optional list<i16>               audit_status;           //商圈审核状态,审核中=0, 拒绝=1, 成功=2
    10: optional string                 s_join_dtm;             //起始添加时间
    11: optional string                 e_join_dtm;             //结束添加时间
    12: optional list<i64>              qd_uid;                 //创建商圈的userid
    13: optional string                 qd_name;                //创建商圈的渠道全称,支持模糊查询
}

// 操作动作
enum OpAction {
    CREATE=1,                       // 创建
    EDIT=2,                         // 修改
    DELETE=3,                       // 删除
    AUDIT=4,                        // 设置审核状态
    SET_STATUS=5,                   // 设置状态
}

// 操作日志
/*
:attention:
   action, resource_path, detail, opadmin 创建操作日志时必传
*/
struct OperationRecord{
    1:  i64             id;                 //操作日志id
    2:  OpAction        action;             //操作动作
    3:  string          resource_path;      //操作资源路径
    4:  string          detail;             //操作描述
    5:  string          opname;             //操作人用户名称
    6:  i64             opuid;              //操作人的userid
    7:  string          optime;             //操作时间
}

struct OpRecordQueryArg {
    1: required QueryMeta               query_meta;             // 查询元数据
    2: optional list<i64>               ids;                    // 操作日志id
    3: optional list<OpAction>          action;                 //操作动作类型
    4: optional string                  resource_path;          //操作资源路径
    5: optional string                  detail;                 //操作描述
    6: optional list<string>            opname;                 //操作人用户名称
    7: optional list<i64>               opuid;                  //操作人userid
    8: optional string                  s_op_dtm;               //起始时间
    9: optional string                  e_op_dtm;               //结束时间
}

// 外部模块的入口管理
/*
:attention:
   module_name, qd_uid 创建入口时必传
*/
struct Entrance{
    1:  i64             id;                 //入口id
    2:  string          module_name;        //外部模块名称
    3:  i64             qd_uid;             //该入口开放对象，渠道userid
    4:  EntranceStatus  status;             //入口状态
    5:  string          create_time;        //创建时间
}

struct EntranceQueryArg {
    1: required QueryMeta               query_meta;             // 查询元数据
    2: optional list<i64>               ids;                    // 入口id
    3: optional list<string>            module_names;           // 外部模块名称
    4: optional list<i64>               qd_uids;                // 渠道uid
    5: optional list<EntranceStatus>    statuses;               // 入口状态
    6: optional string                  s_join_dtm;             //起始添加时间
    7: optional string                  e_join_dtm;             //结束添加时间
}

service QudaoServer {

    ///////////////
    // 渠道相关 //
    ///////////////

    /*
      渠道注册
      :attention:
            先调用apollo的preRegister接口获取到渠道用户id(userid), 然后再调用本接口完成渠道的注册.
    */
    i64 qd_register(1:QudaoUser user, 2:i64 admin) throws (1:QudaoException e);

    /*
      设置渠道状态
      :param uid_list: 渠道用户id列表
      :param status: 渠道状态
      :attention:
        1. 本函数幂等， 可多次调用. 重复设置不会报错
        2. 传入的渠道用户id无效时会抛出异常
    */
    void qd_set_status(1:list<i64> uid_list, 2:QudaoStatus status, 3:i64 admin) throws (1:QudaoException e);

    /*
      更新渠道基本信息. 目前只允许更新 slsm_uid
      :param profiles: qd_uid 和对应需要修改的 base_info 的 map.
      :param admin: 操作人 id.
      :attention:
        1. 本函数幂等， 可多次调用. 重复修改不会报错
        2. 传入的渠道用户id无效时会抛出异常
    */
    void qd_update_base_info(1:map<i64, QudaoBaseInfo> base_infos, 2:i64 admin) throws (1:QudaoException e);

    /*
      更新渠道信息. 注意并非传入的所有参数均可以更新.
      :param profiles: qd_uid 和对应需要修改的 profile 的 map.
      :param admin: 操作人 id.
      :attention:
        1. 本函数幂等， 可多次调用. 重复修改不会报错
        2. 传入的渠道用户id无效时会抛出异常
    */
    void qd_update_profile(1:map<i64, QudaoProfile> profiles, 2:i64 admin) throws (1:QudaoException e);

    void qd_update_auth_areas(1:map<i64, list<AuthArea>> auth_areas, 2:i64 admin) throws (1:QudaoException e);

    /*
      更新渠道信息. 目前只允许更新 default_mchnt_fee.
      :param profiles: qd_uid 和对应需要修改的 account_info 的 map.
      :param admin: 操作人 id.
      :attention:
        1. 本函数幂等， 可多次调用. 重复修改不会报错
        2. 传入的渠道用户id无效时会抛出异常
    */
    void qd_update_account_info(1:map<i64, AccountInfo> account_infos, 2:i64 admin) throws (1:QudaoException e);

    /*
      给列表中的所有渠道 开通增值产品
      :param uid_list: 渠道用户id列表， 必须保证传入的渠道用户id有效
      :param pid_list:  增值产品id列表， 必须保证传入的增值产品id有效
      :attention:
        1. 本函数幂等， 可多次调用. 重复开通产品不会报错
        2. 传入的渠道用户id无效 或 传入的增值产品id无效， 均会抛出异常
    */
    void qd_open_products(1:list<i64> uid_list, 2:list<i64> pid_list, 3:i64 admin) throws (1:QudaoException e);

    map<i64, QudaoBaseInfo> qd_get_base_infos(1:list<i64> uid_list) throws (1:QudaoException e);
    map<i64, QudaoProfile> qd_get_profiles(1:list<i64> uid_list) throws (1:QudaoException e);
    map<i64, AccountInfo> qd_get_account_infos(1:list<i64> uid_list) throws (1:QudaoException e);
    map<i64, BankInfo> qd_get_bank_infos(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      获取指定渠道可用的 (包括已开通及可开通的) 增值产品列表
      :param uid_list: 渠道用户ID列表
      :ret: 渠道用户id为key, 该渠道开通的产品列表为value的字典
    */
    map<i64, list<ProductItem>> qd_get_products(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      通过渠道uid,获取渠道用户信息
      :param uid_list: 渠道用户id列表
      :attention:
            1. 不保证返回顺序! 可根据QudaoUser.uid来一一对应.
            2. 如果没有uid对应的渠道,则结果中不包含该uid.
    */
    list<QudaoUser> qd_get(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      通过渠道 uid, 获取渠道用户信息.
      :attention:
        1. 与 qd_get 接口的区别在于返回的数据不包含 bank_info, 这样不用多次调用 apollo, 提高查询速度.
    */
    list<QudaoUser> qd_get_simple(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      查询满足指定条件的渠道用户id列表
      :ret: 满足条件的渠道用户id列表
    */
    list<i64> qd_query(1:QudaoQueryArg q) throws (1:QudaoException e);

    map<i64, list<i64>> qd_get_hierarchy(1:list<i64> uid_list, 2:i16 max_hierarchy=1) throws (1:QudaoException e);

    /*
      获取指定渠道下,所有渠道商户的用户id
      :param uid_list: 渠道用户id列表
      :param max_hierarchy: 最大搜索层级(向下递归子渠道的次数). 1 代表搜索当前渠道的商户,以及它们最近一层子渠道的商户.
      :ret: 字典. 渠道用户id为key, 渠道商户用户id列表为value
    */
    map<i64, list<i64>> qd_get_mchnt(1:list<i64> uid_list, 2:i16 max_hierarchy=1) throws (1:QudaoException e);

    /*
      获取指定渠道下,所有业务员的用户id
      :param uid_list: 渠道用户id列表
      :param max_hierarchy: 最大搜索层级(向下递归子渠道的次数). 1 代表搜索当前渠道的业务员,以及它们最近一层子渠道的业务员.
      :ret: 字典. 渠道用户id为key, 渠道业务员用户id列表为value
    */
    map<i64, list<i64>> qd_get_slsm(1:list<i64> uid_list, 2:i16 max_hierarchy=1) throws (1:QudaoException e);

    /*
      查询渠道所属一级渠道 uid.
      当查询不是渠道的 uid 时, 会抛出异常.
    */
    i64 qd_top_parent(1:i64 uid) throws (1:QudaoException e);
    /*
      批量查询渠道所属一级渠道 uid.
      当查询参数有不是渠道的 uid 时, 会抛出异常.
    */
    map<i64, i64> qd_top_parents(1:list<i64> uid_list) throws (1:QudaoException e);

    ///////////////
    // 商户相关 //
    ///////////////

    /*
      渠道商户注册完成后,回调本接口.
        1. 完成渠道商户和渠道业务员的绑定，以及渠道商户和渠道的绑定。
        2. 返回该渠道商户所属的一级渠道用户id
      :param admin: 这个商户的创建人用户id，没有则传递 -1
      :attention:
            1. 若找不到传入业务员所属的渠道，则抛出异常
            2. 返回结果中的渠道用户id，是该渠道商户所属的一级渠道的用户id
     */
    MchntRegisteredRet mchnt_on_registered(1:MchntRegisteredArg arg, 2:i64 admin) throws (1:QudaoException e);

    /*
      渠道商户迁移, 用于将渠道系统商户由一个渠道迁移到另一个渠道
    */
    MchntRegisteredRet mchnt_migrate(1:MchntRegisteredArg arg, 2:i64 admin) throws (1:QudaoException e);

    /*
      查询满足指定条件的渠道商户用户id列表
      :ret: 满足条件的渠道商户用户id列表
     */
    list<i64> mchnt_query(1:MchntQueryArg q) throws (1:QudaoException e);

    /*
      查询满足条件的商户个数
    */
    i64 mchnt_query_count(1:MchntQueryArg q) throws (1:QudaoException e);

    /*
      通过渠道商户用户id,获取渠道商户信息
      :param uid_list: 渠道商户用户id列表
      :attention:
            1. 不保证返回顺序! 可根据MchntUser.uid来一一对应.
            2. 如果没有uid对应的渠道商户,则结果中不包含该uid.
    */
    list<MchntUser> mchnt_get(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      设置商户状态.
    */
    void mchnt_set_status(1:list<i64> uid_list, 2:MchntStatus status, 3:i64 admin) throws (1:QudaoException e);

    ///////////////
    // 业务员相关 //
    ///////////////

    /*
        渠道业务员注册完成后，回调本接口。  完成渠道业务员和渠道的绑定, 同时将该业务员绑定为渠道商户.
        :param admin: 这个业务员的创建人用户id，没有则传递 -1
    */
    SlsmRegisteredRet slsm_on_registered(1:SlsmRegisteredArg arg, 2:i64 admin) throws (1:QudaoException e);

    /*
      查询满足指定条件的渠道业务员用户id列表
      :ret: 满足条件的渠道业务员用户id列表
     */
    list<i64> slsm_query(1:SlsmQueryArg q) throws (1:QudaoException e);

    /*
      通过渠道业务员用户id,获取渠道业务员信息
      :param uid_list: 渠道业务员用户id列表
      :attention:
            1. 不保证返回顺序! 可根据SlsmUser.uid来一一对应.
            2. 如果没有uid对应的渠道,则结果中不包含该uid.
    */
    list<SlsmUser> slsm_get(1:list<i64> uid_list) throws (1:QudaoException e);

    /*
      设置业务员状态.
    */
    void slsm_set_status(1:list<i64> uid_list, 2:SlsmStatus status, 3:i64 admin) throws (1:QudaoException e);

    /*
      迁移业务员下属商户
    */
    void slsm_transfer_mchnts(1:list<i64> uid_list, 2:i64 target_uid, 3:i64 admin) throws (1:QudaoException e);

    /*
      查询业务员直属的渠道基本信息
      :param qd_uid_list: 渠道业务员用户id列表
      :ret: 字典, 业务员 userid 为 key, 渠道基本信息为 value.
    */
    map<i64, QudaoBaseInfo> slsm_get_qd_base_info(1:list<i64> qd_uid_list) throws (1:QudaoException e);

    ///////////////
    // 增值产品相关 //
    ///////////////

    /*
      创建增值产品
      :param item: 增值产品信息，注意：id填-1， status不传
      :param admin: 这个增值产品的创建者用户id
      :ret: 创建成功的增值产品信息。 注意： 返回的id为该增值产品在系统中的id， status字段不可用
    */
    ProductItem prod_create(1:ProductItem item, 2:i64 admin) throws (1:QudaoException e);

    /*
     查询增值产品
     :param q: 查询条件
     :ret: 满足条件的增值产品id列表
    */
    list<i64> prod_query(1:ProdQueryArg q) throws (1:QudaoException e);

    /*
      通过增值产品id，获取增值产品信息
      :param: pid_list: 增值产品id列表
      :attention:
        1. 不保证返回顺序
        2. 如果找不到pid对应的增值产品，则结果中不包含
        3. 结果中的status字段不可用
    */
    list<ProductItem> prod_get(1:list<i64> pid_list) throws (1:QudaoException e);

    ///////////////
    // 公告相关  //
    ///////////////

    // 创建公告
    i64 announce_create(1:Announcement announce, 2:list<i64> qd_uids, 3:i64 admin) throws (1:QudaoException e);
    // 修改公告状态
    void announce_set_status(1:list<i64> announce_ids, 2:AnnounceStatus status, 3:i64 admin) throws (1:QudaoException e);
    // 查询公告信息， 返回公告 id
    list<i64> announce_query(1:QueryAnnounceArg q) throws (1:QudaoException e);
    // 查询满足条件的公告条数
    i64 announce_query_count(1:QueryAnnounceArg q) throws (1:QudaoException e);
    // 查询公告信息
    list<Announcement> announce_get(1:list<i64> announce_ids) throws (1:QudaoException e);

    /* 
      创建分润规则
      :return: 创建成功后的规则id.
    */
    string royalty_rule_create(1:RoyaltyRule rule, 2:i64 admin) throws (1:QudaoException e);

    list<string> royalty_rule_query(1:RoyaltyRuleQueryArg q) throws (1:QudaoException e);

    /* 获取分润规则 */
    list<RoyaltyRule> royalty_rule_get(1:list<string> rule_ids) throws (1:QudaoException e);


    ///////////////
    // 培训资料  //
    ///////////////

    i64 training_file_create(1:TrainingFile training_file, 2:i64 admin) throws (1:QudaoException e);
    void training_file_set_status(1:list<i64> ids, 2:i16 status, 3:i64 admin) throws (1:QudaoException e);
    /*
      更新培训资料
      :param training_files: training_file_id 和对应需要修改的 training_file 的 map.
      :param admin: 操作人 id.
      :attention:
        1. 本函数幂等， 可多次调用. 重复修改不会报错
        2. 传入的培训资料id无效时会抛出异常
    */
    void training_file_update(1:map<i64, TrainingFile> training_files, 2:i64 admin) throws (1:QudaoException e);

    list<i64> training_file_query(1:TrainingFileQueryArg q) throws (1:QudaoException e);
    i64 training_file_query_count(1:TrainingFileQueryArg q) throws (1:QudaoException e);
    list<TrainingFile> training_file_get(1:list<i64> file_ids) throws (1:QudaoException e);


    ///////////////
    // 商圈管理  //
    ///////////////

    // 创建商圈, 返回创建成功后的商圈id.
    i64 region_create(1:Region region, 2:i64 admin) throws (1:QudaoException e);
    // 修改商圈状态
    void region_set_status(1:list<i64> ids, 2:i16 status, 3:i64 admin) throws (1:QudaoException e);
    // 修改商圈审核状态
    void region_audit(1:list<i64> ids, 2:i16 audit_status, 3:i64 admin) throws (1:QudaoException e);
    // 删除商圈
    void region_delete(1:list<i64> ids, 2:i64 admin) throws (1:QudaoException e);
    /*
      更新商圈信息
      :param regions: region_id 和对应需要修改的 region 的 map.
      :param admin: 操作人 id.
      :attention:
        1. 本函数幂等， 可多次调用. 重复修改不会报错
        2. 传入的商圈id无效时会抛出异常
    */
    void region_update(1:map<i64, Region> regions, 2:i64 admin) throws (1:QudaoException e);

    // 查询商圈,返回商圈 id
    list<i64> region_query(1:RegionQueryArg q) throws (1:QudaoException e);
    // 查询满足条件的商圈数量
    i64 region_query_count(1:RegionQueryArg q) throws (1:QudaoException e);
    // 获取指定商圈id列表的商圈信息
    list<Region> region_get(1:list<i64> region_ids) throws (1:QudaoException e);

    ///////////////
    // 操作日志 //
    ///////////////

    // 创建操作日志, 返回创建成功后的操作日志id.
    i64 oprecord_create(1:OperationRecord oprecord, 2:i64 admin) throws (1:QudaoException e);

    // 查询操作日志,返回操作日志id
    list<i64> oprecord_query(1:OpRecordQueryArg q) throws (1:QudaoException e);
    // 查询满足条件的操作日志数量
    i64 oprecord_query_count(1:OpRecordQueryArg q) throws (1:QudaoException e);
    // 获取指定操作日志id列表的操作日志信息
    list<OperationRecord> oprecord_get(1:list<i64> ids) throws (1:QudaoException e);

    //////////////////////
    // 外部模块入口管理 //
    /////////////////////

    // 创建入口, 返回创建成功后的入口id.
    i64 entrance_create(1:Entrance entrance, 2:i64 admin) throws (1:QudaoException e);
    // 查询入口,返回入口id
    list<i64> entrance_query(1:EntranceQueryArg q) throws (1:QudaoException e);
    // 查询满足条件的入口数量
    i64 entrance_query_count(1:EntranceQueryArg q) throws (1:QudaoException e);
    // 获取指定入口ids的列表信息
    list<Entrance> entrance_get(1:list<i64> ids) throws (1:QudaoException e);
    // 关闭指定入口
    void entrance_delete(1:list<i64> ids, 2:i64 admin) throws (1:QudaoException e);

    // ping
    void ping();
}
