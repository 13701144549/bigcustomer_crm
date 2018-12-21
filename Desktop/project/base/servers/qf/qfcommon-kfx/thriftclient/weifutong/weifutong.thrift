namespace py weifutong

// 证件照参数
struct UpcertArg
{
    1: required binary p_idcard_pic, //身份证图片, JPG, 正面照, 二进制格式
    2: required binary r_idcard_pic, //身份证图片, JPG, 反面照, 二进制格式
}

// 错误代码
enum ERRCODE
{
    IMG_ERROR = 9000    // 图片错误
    FIELD_LACK = 9001   // 缺少字段
    REMOTE_RESP_ERROR = 9002  // 对方返回错误
    TIMEOUT_ERROR = 9003   // 超时
    DB_ERROR = 9004         // 数据库错误
    USER_ERROR = 9005       // 用户数据错误
    DATA_ERROR = 9006       // 数据错误
    PARAM_ERROR = 9007      // 参数错误
    IO_ERROR = 9008         // IO错误
    SERVER_ERROR = 9010   // 系统内部错误
    DATA_NOT_EXIST = 9011   // 数据不存在
}

// 支付类型
enum PAYTYPE
{
    WEIXIN=1,   // 微信
    ALIPAY=2,   // 支付宝
    QPAY=3,     // QQ钱包
    QUICK=4,    // 快捷支付
}

// 进件通道
enum CHNLCODE{
    CITIC=1,            // 中信普通
    CEB=2,              // 光大(已废弃)
    FUIOU=3,            // 富友
    ZXWC=4,             // 中信围餐
    HUIYI=5,            // 汇宜普通
    HYQK=6,             // 汇宜快捷
    CITIC_ZERO_FEE=7,   // 中信零费率
    DAZE=8,             // 大则
    WANGSHANG=9,        // 网商
    DAZEPOINT=10,       // 大则积分
    YEEPAY=11,          //收款宝
    HUITONG=12,         //汇通
    WEIXIN=13,          // 微信
    FUIOU_LVZHOU=14,    // 富友绿洲
    HELIBAO=15,         // 合利宝
    WEIXIN_LVZHOU=16,   // 微信绿洲
    WSBLUESEA=17,       // 网商蓝海
    XIANFENG=18,        // 先锋
    HUIYI_WEIXIN=19,    // 汇宜微信
    LESHUA=20,          // 乐刷
}

// 中信图片类型
enum CITIC_PIC_TYPE{
    IDCARD = 1,        // 身份证
    LICENSE = 2,       // 营业执照
    ORGANIZE = 3,      // 组织机构照
    USER_PROTO = 4,    // 商户协议照
    SHOP = 5,          // 门头照
}

// 尽量和mis_upgrade_voucher 中的name保持一致
enum PIC_TYPE{
    IDCARDFRONT = 1,    // 身份证正面
    IDCARDBACK = 2,     // 身份证反面
    LICENSEPHOTO = 3,   // 营业执照
    ORGPHOTO = 4,       // 组织机构代码证
    TAXPHOTO = 5,       // 税务登记证
    OPENLICENSE = 6,    // 开户许可证
    SHOPPHOTO = 7,      // 门头照/经营场所/商户店面正门照/店铺门面照片/经营场所外景照片
    GOODSPHOTO = 8,     // 所售商品/经营场所内景照片
    IDCARDINHAND = 9,   // 手持身份证
    DELEGATEAGREEMENT=10, // 业务代理合同或者协议
    PAYPOINT=11, // 收银台
    AUTHBANKCARDFRONT=12, // 银行卡正面
    AUTHBANKCARDBACK=13, // 银行卡反面
    GROUPPHOTO=14, // 业务员与申请人合影
    CHECKSTAND_WEIXIN=15,      //微信活动收银台
    CHECKIN_WEIXIN=16,         // 微信活动餐饮图片入驻
    CHECKSTAND_ALIPAY=17,      // 支付宝活动收银台
    CHECKIN_ALIPAY=18,         // 支付宝各大餐饮平台入驻图片
}

enum AddMchntState {
    DOING=0,  // 进件中
    SUCC=1,  // 进件成功
    FAILED=2,  // 进件失败
    WAIT_NOTIFY=3,  // 进件完成，等待通道通知结果
    CLOSED_MANUAL=4, // 手动关闭
    WAIT_CHNL_1,    // 等待通知, 各通道自由发挥
}

enum CHNLID {
    FUIOU=37,            // 富友
    HUIYI=32,            // 汇宜普通
    HUIYI_WEIXIN=32,    // 汇宜微信
    HYQK=46,             // 汇宜快捷
    DAZE=56,             // 大则
    WANGSHANG=74,        // 网商
    DAZEPOINT=80,       // 大则积分
    YEEPAY=92,          //收款宝
    HUITONG=86,         //汇通
    WEIXIN=20,          // 微信
    FUIOU_LVZHOU=37,    // 富友绿洲
    HELIBAO=118,         // 合利宝
    WEIXIN_LVZHOU=20,   // 微信绿洲
    WSBLUESEA=74,       // 网商蓝海
    XIANFENG=133,        // 先锋
    LESHUA=157,         // 乐刷
}

// 查询元数据
struct QueryMeta {
    1: required i64             offset=0;           // 偏移, 默认从 0 开始
    2: required i64             count=100;          // 记录数, 默认 100 条
    3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

// 费用类型
enum FeeType{
 T0 = 1,  // t0收单手续费
 T1 = 2,  // t1收单手续费
}

// 支付信息
struct PayConf
{
    1: required PAYTYPE paytype,     // 支付类型
    2: required string bill_rate,    // 结算费率, 各个通道不同
    3: optional string extend,       // 扩展字段，以json字符串方式传入。 用于支持特殊的支付方式费率。
    4: optional FeeType ft,          // 费用类型
}

struct PayConfEx{
    1: required list<PayConf> payconfs,
    2: required string mchnt_id,
    3: required CHNLCODE chnlcode,
    4: required string trace_no,
}

// 开户网点（用户银行）基本信息.  Copy from apollo.thrift. 所有字段改为optional
struct BankInfo{
    1: optional string			headbankname;		//所属总行名称
    2: optional string			bankuser;			//开户人姓名
    3: optional string			bankaccount;		//开户人账号
    4: optional i32			    banktype;			//账户类型，1，为对私，2为对公
    5: optional string			bankname;			//网点名称（支行名称）
    6: optional string			bankcode;			//网点联行号
    7: optional string			bankProvince;	    //支行所属省份
    8: optional string			bankCity;		    //支行所属城市
    9: optional string			bankmobile;		    // 银行预留手机号
    10: optional string         idnumber;           // 开户人身份证号
}

// 商户基本信息. Copy from apollo.thrift. 所有字段改为optional
struct User{
    // 1: required i64			    uid;			//用户唯一id
    2: optional string 			name;			//用户名称
    3: optional string 			shopname;		        //店铺名称
    4: optional string 			email;			//用户的email
    5: optional string 			mobile;		        //手机号码
    6: optional string			telephone;			//座机电话
    // 7: optional string 			password;			//密码
    8: optional i32			    state;				//状态
    9: optional string			idnumber;			//身份证号
    10: optional string			province;			//所在省份
    11: optional string			city;				//所在城市
    12: optional string			mcc;				//商户mcc
    13: optional string			address;			//商户地址
    14: optional double			longitude;	        //商户gps经度
    15: optional double			latitude;		        //商户gps维度
    // 16: optional list<UserCate> userCates;	                //用户类别  // NOT USE
    17: optional string			jointime;			//用户创建时间，为"YYYY-MM-DD HH:SS:mm"
    18: optional i32			risklevel;		//风控等级
    19: optional i32			groupid;		// 渠道id
    20: optional i32            user_type;      // 商户类型
    21: optional string         legalperson;        // 法人姓名
    22: optional string         businessaddr;       // 经营地址
    23: optional string         licensenumber,      // 营业执照号
    24: optional string         licenseend_date,    // 营业执照到期时间
}

// 商户信息，包括用户基本信息. Copy from apollo.thrift. 所有字段改为optional
struct UserProfile{
    // 1: required i64			    uid = 0;			//用户唯一id
    2: optional User 			user;				//用户基本信息
    3: optional BankInfo		bankInfo;			//开户银行信息
    // 4: optional list<UserTag> 	userTags;			//用户标签 // NOT USE
    // 5: optional list<User> 		relations;			//用户的所属关系，比如，业务员，渠道....  // NOT USE
}

// 商户进件记录
struct AddMchntRecord {
    1: i64 id,
    2: string batch_id,
    3: string out_trace_no,  // 进件发起方 追踪号
    4: string trace_no,  // 进件系统 追踪号

    10: i64 userid,  // 钱方USERID
    11: string mchnt_id,  // 通道商户号
    12: CHNLCODE chnlcode,  // 通道代码
//    13: string paytype,  // 进件时选择开通的支付类型
    14: string src,  // 进件发起方
    15: string extend,  // 扩展信息，不同的chnlcode格式不一样
//    16: string req_info,  // 请求信息
    17: string qf_mchnt_id,  // 向通道进件时，动态生成的钱方商户号

    30: AddMchntState state,  // 进件状态
    31: string errmsg,  // 错误信息

    50: string ctime,  // 记录创建时间
    51: string utime,  // 记录更新时间
    52: string amtime,  // 通道进件时间

    70: string smid,  // 支付宝进件后的SMID
    71: string wx_chnl_id,  // 微信渠道号
    72: string wx_mchnt_id, // 进件成功后，微信生成的子商户号
    73: string subscribe_appid,  // 该商户的推荐关注公众号
}


// 当前关注状态
enum SubscribeState {
    DOING=0,  // 系统处理中
    SUCC=1,  // 成功
    FAILED=2,  // 失败
    WAIT_NOTIFY=3,  // 等待通道结果
}

// 配置关注的方式
enum SubscribeType {
    REGISTER=1,     // 进件时候配置了关注
    SWITCHCHNL=2,   // 切渠道号
    APPENDCONF=3    // 追加配置
}


struct SubscribeQueryArg{
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
    3: optional list<string> mchnt_id_list,  // 通道商户号
    4: optional list<CHNLCODE> chnlcode_list,  // 通道代码
    5: optional list<string> batch_id_list,  // 批次号
    6: optional list<string> out_trace_no_list,  // 外部流水号
    7: optional list<string> trace_no_list,  // 系统流水号
    8: optional list<string> src_list,  // 发起方
    9: optional list<AddMchntState> state_list,  // 状态
    10: optional list<string> subscribe_appid_list, // 关注公众号
    11: optional string s_ctime,  // 记录创建开始时间
    12: optional string e_ctime,  // 记录创建结束时间
}


// 商户关注记录
struct SubscribeAppidRecord {
    1: i64 id,
    2: string batch_id,
    3: string src,  // 发起方
    4: SubscribeType subscribe_type,
    5: i64 userid,  // 钱方USERID
    6: CHNLCODE chnlcode,  // 通道代码
    7: string mchnt_id,  // 通道商户号
    8: string wx_chnl_id,  // 微信渠道号
    9: string wx_mchnt_id, // 微信生成的子商户号
    10: string subscribe_appid,  // 该商户在此微信渠道号下的关注公众号
    11: string out_trace_no,  // 发起方追踪号
    12: string trace_no,  // 内部追踪号
    13: string extend,  // 扩展信息，不同的chnlcode格式不一样
    14: SubscribeState state,  // 状态
    15: string errmsg,  // 错误信息
    16: string ctime,  // 记录创建时间
    17: string utime,  // 记录更新时间
    18: string result_time,     // 结果时间
}

// 微信参数配置
struct WechatConf
{
    1: optional string mchnt_id,        // 商户号
    // json字符串形式的列表. 形如： '["https://o2.qfpay.com", "https://o2.qfpay.com/dc"]'
    2: optional string jsapipath,       // 子商户公众号JS API 支付授权目录
    3: optional string sub_appid,       // 子商户 sub appid
    4: optional string subscribe_appid, // 子商户推荐关注公众账号APPID
    5: optional string partner,         // 交易识别码
    6: optional string cid,                // 微信渠道号
    7: optional i32 relationship,       // 商户与关注公众号的关系, 采用Audit的AppInfo.state, 网商进件必传
    8: optional i64 priority,           // 写入 chnlbind 优先级, 不传会取默认配置. 
}

// 原有进件(先保留供paymis查看, 更新DB后可删除)
struct StoreNewCITIC
{
    1: required i64 userid,             // 商户ID
    2: required list<PayConf> payconf,  // 支付信息
    3: required string indentity_photo,  //证件照路径, 需要先调用upcert_citic获取
    4: required string trace_no,        // 外部追踪号
}

// 中信进件参数
struct StoreNewCitic
{
    1: required i64 userid,              // 商户ID
    2: required CHNLCODE chnlcode,       // 进件通道
    3: required string indentity_photo,  // 证件照路径, 需要先调用upcert_citic获取
    4: required string trace_no,         // 外部追踪号
    5: optional string license_photo,    // 营业执照
    6: optional string protocol_photo,   // 商户协议照
    7: optional string org_photo,        // 组织机构代码照
    8: optional string main_photo,       // 门头照
}

// 进件通用参数
struct StoreNewReq{
    1: required i64 userid,                  // 商户ID
    2: required string batch_id,             // 批次号(属于同一次操作)
    3: required string src,                  // 来源
    4: required CHNLCODE chnlcode,           //
    5: optional string trace_no,
    6: optional list<PayConf> payconfs,      // 不能获取的情况使用(目前仅有大则积分)
    //  jsapipath,sub_appid,subscribe_appid必传
    7: optional WechatConf wechat_conf,      // 微信支付参数配置，当需要强制指定时传入。
    8: optional string chnlbind_sync_time,   // 进件成功后, 同步 chnlbind 时间.
    9: optional string link_id,             // 要挂靠的商户号
}

struct StoreQueryReq {
    1: required i64 userid,                  // 商户ID
    2: required string mchnt_id,             // 通道商户号
    3: required CHNLCODE chnlcode,           //
    4: required string trace_no,            //
}

struct TradePartner{
    1: required string mchnt_id,              // 渠道返回的商户号
    2: required CHNLCODE chnlcode,       // 进件通道
    3: required string trace_no,         // 外部追踪号
    4: required PAYTYPE paytype,        // 支付类型
}

struct MchntReq{
    1: required i64 userid,                  // 商户ID
    2: required string mchnt_id,              // 渠道返回的商户号
}

// 光大进件参数
struct StoreNewCEB
{
    1: required i64 userid,              //商户ID
    2: required string english_name,     //商户英文名
    3: required string post_code,        // 商户邮编
    4: required list<PayConf> payconf,   // 支付信息
    5: required string indentity_photo,  //证件照路径, 需要先调用upcert_ceb获取
    6: optional bool active_eleacc=0,// 激活电子账户, 默认不激活
}

// 富友进件参数
struct StoreNewFY
{
    1: required i64 userid,             // 商户ID
    2: required list<PayConf> payconf,   // 支付信息
    3: optional string settle_tp='1',       // 清算类型：1自动结算;2手动结算
    4: optional string tx_flag='0',         // 是否开通D0提现 (0:不开通，1：开通)
    5: optional string tx_set_cd='',       // 提现扣率, 开通D0则必须有值
    6: optional string acnt_artif_flag='1', // 法人入账标识 (0: 非法人, 1: 法人)
    7: required string link_mchnt_cd,       // 挂靠商户号
}

// 富友更新参数
struct UpdateFY
{
    1: required i64 userid,             // 商户ID
    2: required string mchnt_id,        // 富友商户ID
    3: required list<PayConf> payconf,  // 支付信息
    4: optional string settle_tp,       // 清算类型：1自动结算;2手动结算。 默认 1
    5: optional string tx_flag,         // 是否开通D0提现 (0:不开通，1：开通)。 默认0
    6: optional string tx_set_cd,       // 提现扣率, 开通D0则必须有值。 默认''
    7: optional string acnt_artif_flag, // 法人入账标识 (0: 非法人, 1: 法人)。 默认 1
    8: optional UserProfile profile,    // 商户资料信息
    9: optional string link_mchnt_cd,   // 挂靠商户号
    10: optional string daily_settle_flag,   // 是否开通天天结(0: 不开通, 1: 开通)
    11: optional string daily_settle_set_cd,   // 天天结扣率, 开通天天结必传
}

// 计算方式
enum SettleMode{
 ToOtherBank = 1,  // 到他行卡
 ToYLB = 2,    // 到余利宝
}

// 更新统一参数
struct UpdateReq{
    1: required i64 userid,             // 商户ID
    2: required string mchnt_id,        // 对方商户ID
    3: required string batch_id,        // 批次号
    4: required string trace_no,        // 追踪码
    5: required CHNLCODE chnlcode,      // 更新通道
    6: required string src,             // 更新来源
    7: optional list<PayConf> payconfs, // 费率信息
    8: optional UserProfile profile,    // 商户资料信息
    9: optional list<PIC_TYPE> pics,    // 要更新的图片
}

struct UpdateQueryReq {
    1: required i64 userid,
    2: required string mchnt_id,      // 通道商户号
    3: required string out_trace_no,  // 更新时传的 trace_no
    4: required CHNLCODE chnlcode,    // 通道
    5: optional string extend,        // 扩展信息, json 字符串
}

struct UpdateMchntResp {
    1: required i64 userid,
    2: required string mchnt_id,
    3: required string out_trace_no,  // 更新时传的 trace_no
    4: required CHNLCODE chnlcode,    // 通道
    5: required i16 state,            // 更新状态. 更新中=0, 成功=1, 失败=2
}

// 富友微信参数配置
struct WechatConfFY
{
    1: required string mchnt_id,        // 富友商户号
    2: optional string jsapipath,       // 子商户公众号JS API 支付授权目录
    3: optional string sub_appid,       // 子商户 sub appid
    4: optional string subscribe_appid, // 子商户推荐关注公众账号APPID
}

// 富友微信参数配置响应
// code '0000' 表示成功, '' 表示这项未设置, 其余均为失败
struct WechatConfFYResp
{
    1: required string mchnt_id,        // 富友商户号
    2: optional string jsapipath_code,  // JS API支付授权目录返回码
    3: optional string jsapipath_msg,   // JS API支付授权目录错误信息
    4: optional string sub_appid_code,  // 商户 sub appid
    5: optional string sub_appid_msg,   // 商户 sub appid错误信息
    6: optional string subcribe_appid_code,  // 商户推荐关注公众账号APPID返回码
    7: optional string subcribe_appid_msg,   // 商户推荐关注公众账号APPID错误信息
}

// 电子协议
struct ElecContractInfo{
    1: optional string mchnt_id,            // 商户号
    2: optional string verify_no,           // 验证码
    3: optional string verify_no_expire_ts, // 验证码失效时间
    4: optional string contract_no,         // 协议编号
    5: optional string sign_url,            // 协议签署服务地址
}


// 中信围餐进件参数
struct StoreNewWC
{
    1: required i64 userid,              //商户ID
    2: required list<PayConf> payconf,   // 支付信息, 暂时只能用微信
    3: required string indentity_photo,  //证件照路径, 需要先调用upcert_citic获取
}

// 大则进件
struct StoreNewDZ
{
    1: required i64 userid,              //商户ID
    2: required string trace_no,        // 外部追踪号
}

// 汇宜快捷支付进件
struct StoreNewHuiyi
{
    1: required i64 userid,              // 商户ID
    /* 使用extend字段记录费率信息。
      extend 是一个list， 形如
      [
        # 境内贷记卡手续费
        {
            'prod_cd': '1171',
            'biz_cd': '0000026',
            'sub_biz_cd': '0002001',
            'fee_md': '0',
            'fee_percent': 0.4,
        },

        # 产品手续费， **必传**
        {
            'prod_cd': '1171',
            'biz_cd': '0000026',
            'sub_biz_cd': '0002004',
            'fee_md': '0',
            'fee_percent': 0,
        },
        # 实时划手续费， **必传**
        {
            'prod_cd': '1171',
            'biz_cd': '0000026',
            'sub_biz_cd': '0002005',
            'fee_md': '0',
            'fee_percent': 0.3,
        },
      ]

      a. prod_cd、biz_cd、sub_biz_cd详见汇宜的 "会员信息接口文档".
      b. 费率模式有两种： 固定费率 和 百分比费率，详见  "会员信息接口文档".
    */
    2: required list<PayConf> payconf,   // 支付信息, 暂时只能用 '快捷支付'。
}

// 汇宜更新参数
struct HuiyiUpdateArg{
    1: required i64 userid,
    2: required string mchnt_id,
    3: optional UserProfile profile,
    4: optional PayConf payconf
}

// 汇宜查询结果
struct HuiyiQueryResp{
    1: required UserProfile profile,
    3: required string fee
}


// 注销结果
struct CancelledResp{
    1: required string mchnt_id,
    2: required string respcd,      // 成功0000
    3: required string respmsg,
}

// 进件查询参数
// 注意: out_merchant_id 和 st, et 不可同时为空
struct StoreNewQuery
{
    1: optional string out_merchant_id,         // 外部商户号
    2: optional string st,          // 查询进件初始时间, 形如'2016-08-01 00:00:00'
    3: optional string et,          // 查询进件结束时间, 形如'2016-08-02 00:00:00'
}

// 进件结果
struct StoreNewResult
{
    1: required i64 userid,                 // 商户ID, 咱们的ID
    2: required string merchant_id,         // 中信/富友等生成的ID
    3: required string out_merchant_id,     // 本次进件外部商户号, 外部追踪码
    4: optional string active_api,          // 激活支付类型
}

// 查询结果
struct QueryResult
{
    1: required string merchant_id,         // 威富通生成的ID
    2: required string out_merchant_id,     // 外部商户号
    3: optional string examine_status,              // 是否审核, 1 审核通过
    4: optional string activate_status,          // 是否激活, 1 激活成功
}

// 证书上传结果
struct UpcertResult
{
    1: required string  indentity_photo,    // 威富通返回的证书路径
}


struct UploadPicArg{
    1: required binary content,
    2: required string imgname,
    3: required CHNLCODE chnlcode,
    4: required string trace_no,
    5: optional i64 pic_type,    // 图片类型
    6: optional i64 userid,      // 钱方商户id
    7: optional string mchnt_id,    // 商户号
}

// 商户结算账户查询
struct BankAccountQueryArg {
    1: required CHNLCODE chnlcode,   // 通道
    2: required string trace_no,
    3: optional string merchant_id,  // 通道商户号
}

// 威富通服务异常
exception WeifutongError
{
    1: i32 respcd,     // 返回码
    2: string respmsg,  // 错误信息
    3: optional string ext, // 额外错误信息, json字符串
}

// 网商注册查询
struct RegisterQuery
{
    1: required i64 userid,             // 商户ID
    2: optional string trace_no,        // 外部追踪号
}

// 网商微信号修改
struct WSAddMerchantConfigArg
{
    1: required i64 userid,             // 商户ID
    2: required i64 chnlcode,           // 通道号
    3: required i64 trace_no,           // 外部追踪号
    4: required string mchnt_id,           // 网商商户ID
    5: optional string path,            // 支付路径
    6: optional string appid,           // 微信 appid
    7: optional string subscribe_appid, // 微信公众号 id
}

// 微信注册查询
struct WeixinRegisterQuery
{
    1: required i64 userid,             // 商户ID
    2: optional string trace_no,        // 外部追踪号
    3: optional i64 chnlcode,           // 通道号
}

struct WeixinRegisterQueryResp
{
    1: required i64 userid,                 // 商户ID, 咱们的ID
    2: required string merchant_id,         // 中信/富友等生成的ID
    3: required string out_merchant_id,     // 本次进件外部商户号, 外部追踪码
    4: optional string active_api,          // 激活支付类型
    5: optional string sign_url,            // 商户签约 url
}

struct WeixinSignContractArg
{
    1: required i64 userid,             // 商户ID
    2: optional string trace_no,        // 外部追踪号
    3: optional i64 chnlcode,           // 通道号
}

// 微信直连配置查询
struct WeixinConfigQuery
{
    1: required i64 userid,             // 商户ID
    2: optional string trace_no,        // 外部追踪号
    3: optional i64 chnlcode,           // 通道号
}

struct HelibaoStoreNewQueryArg {
    1: required i64 userid,  // 商户 id
    2: required string out_trace_no,  // 进件时传的 trace_no
}

struct HelibaoStoreNewQueryResp {
    1: required i64 userid,  // 商户 id
    2: required string sign_url,  // 签约 url
}

struct HelibaoAgreementQueryArg {
    1: required i64 userid,             // 商户ID
    2: required string out_trace_no,        // 外部追踪号
}

enum HelibaoAgreementStatus {
    INIT=0,     // 初始化, 未签署
    WAIT=1,     // 已签署, 等待审核
    REFUSE=2,   // 已拒绝
    AUDITED=3,  // 审核通过
}

struct HelibaoAgreementQueryResp {
    1: required i64 userid,
    2: required HelibaoAgreementStatus status,
}

struct AddMchntQueryArg{
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
    3: optional list<string> mchnt_id_list,  // 通道商户号
    4: optional list<CHNLCODE> chnlcode_list,  // 通道代码
    5: optional list<string> batch_id_list,  // 进件批次号
    6: optional list<string> out_trace_no_list,  // 外部进件流水号
    7: optional list<string> trace_no_list,  // 进件系统流水号
    8: optional list<string> src_list,  // 进件发起方
    9: optional list<AddMchntState> state_list,  // 进件状态
//    10: optional list<string> qf_mchnt_id_list,  // 进件时，送给通道的钱方商户号
    11: optional list<string> subscribe_appid_list,
//    12: optional list<string> wx_chnl_id_list,  // 微信渠道号

    30: optional string s_ctime,  // 记录创建开始时间
    31: optional string e_ctime,  // 记录创建结束时间
    32: optional string s_utime,  // 记录更新开始时间
    33: optional string e_utime,  // 记录更新结束时间
}

// 短信类型
enum SmsType{
	OpenBankAccount = 1,	# 开通银行账户
	ChangeBankAccount = 2,	# 更改银行账户
	ChangeBankMobile=3,		# 更改银行预留手机号
}

// 短信参数
struct SendSmsArg {
    1: required i64 userid,
	2: required SmsType sms_type,
	3: required string mchnt_id,
	4: required string out_trace_no,
    5: required CHNLCODE chnlcode,
	6: string mobile,
}

// 服务类型
enum ServiceType {
	OpenBankAccount = 1,	# 开通银行账户
	OpenYLB = 2,			# 开通余利宝
    QueryBankAccount = 3,   # 查询银行账户
    Weixin = 4,             # 微信支付
    Alipay = 5,             # 支付宝支付
    QueryWxMchntId = 6,    # 查询微信子商户号(富友会直接请求通道方, 并不是查DB)
    WeixinOasis = 7,        # 微信绿洲
    QueryRegisterResult=8,  # 注册结果查询
    CreateActivity=9,       # 创建活动
    NotifyResult=10,        # 回调
    AppendWechatconfQuery=11, # 追加公众号结果查询
}

# 服务请求参数
struct ServiceArg{
    1: required i64 userid,
    2: required string mchnt_id,
    3: required string out_trace_no,
    4: required ServiceType srv_type,
    5: required CHNLCODE chnlcode,
    6: optional string extend,        # json字符串, 例如开通银行账户, 需填入'{"auth_code": "xxxx", "mobile": "13800138000"}'
}

// state, 不同接口不同类型含义不同
struct TradeRet{
    1: required string code,    # 0000成功, 其余失败
	2: required string errmsg,
	3: required string out_trace_no,
	4: required i32 state,				# code=0000才有意义, 1:成功, 2:失败, 3:审核中
    5: optional string extend,
}

struct UpPicArg{
    1: required string out_trace_no,
    2: required CHNLCODE chnlcode,
    3: required list<PIC_TYPE> pic_types,
    4: required string mchnt_id,
    5: required i64 userid,
}


struct DataPenetrateArg{
    1: required string out_trace_no,
    2: required CHNLCODE chnlcode,  // 通道代码
    3: required i64 userid,
    4: required string paychnl_id,      // 在支付类型下标识, 例如微信子商户号
}

// 微信支付参数变更item。
struct WechatConfUpdateItem {
    1: required i64 userid,  // 钱方USERID
    2: optional string trace_no,  // 外部跟踪号，选填
    3: required CHNLCODE chnlcode,  // 通道代码
    // jsapipath,sub_appid,subscribe_appid必传
    4: required WechatConf wechat_conf,  // 微信支付参数
    5: optional string mchnt_id,  // 通道商户号
    6: optional string chnlbind_sync_time,  // 同步到 chnlbind 时间.
    7: optional string link_id,             // 要挂靠的商户号
}

// 微信支付参数变更请求参数， 目前用于变更商户关注公众号。
struct WechatConfUpdateArg {
    1: required string batch_id,  // 批次号,保证每次不重复。 可使用uuid.uuid4().hex
    2: required string src,  // 发起方服务名称， 如apollo.1、addmchnt_mis.0
    3: required list<WechatConfUpdateItem> wechatconf_list,  // 微信参数更新列表
}

struct AppendWechatConfArg {
    1: required string batch_id,  // 批次号,保证每次不重复。 可使用uuid.uuid4().hex
    2: required string src,  // 发起方服务名称， 如apollo.1、addmchnt_mis.0
    3: required WechatConfUpdateItem wechatconf,  // 微信参数
}

// 配置微信参数请求参数
struct WechatConfReq {
    1: required WechatConf wechat_conf,
    2: required CHNLCODE chnlcode,
    3: required string out_trace_no,
    4: required string mchnt_id,
}

struct ChnlbindSyncQueryArg {
    1: required QueryMeta query_meta,
    2: optional list<i64> userid_list,
    3: optional list<string> mchnt_id_list,      // 通道商户号
    4: optional list<string> batch_id_list,      // 进件批次号
    5: optional list<string> out_trace_no_list,  // 外部进件流水号
    6: optional list<string> trace_no_list,      // 进件系统流水号
    7: optional list<string> src_list,           // 进件发起方
    8: optional list<i16> sync_state_list,       // 同步状态

    9: optional string ctime_start,              // 记录创建开始时间
    10: optional string ctime_end,               // 记录创建结束时间
    11: optional string utime_start,             // 记录更新开始时间
    12: optional string utime_end,               // 记录更新结束时间
}

struct ChnlbindRecord {
    1: required i64 userid,
    2: optional string mchntid,       // 通道商户号
    3: optional string termid,        // 通道终端号
    4: optional string mchntnm,       // 通道商户名称
    5: optional string mcc,           // 通道 mcc
    6: required i64 chnlid,           // 通道 id
    7: optional string key1,          // 秘钥 1
    8: optional string key2,          // 秘钥 2
    9: optional string key3,          // 秘钥 3
    10: required i64 priority,        // 优先级
    11: required i64 change,          // 是否可切换
    12: required i64 bigmchnt,        // 是否大商户
    13: required i64 available,       // 通道是否可用
    14: optional double chnlfee,      // 通道费率
    15: optional double qffee,        // 钱方费率
    16: required i64 admin,
    17: required i64 last_admin,
    18: optional string create_time,
    19: optional string update_time,
    20: optional string tag1,         // 标签
    21: optional string tag2,         // 标签
    22: optional string memo,         // 备注
    23: required i64 tradetype,       // 交易类型
}

enum CHNLBIND_SYNC_STATE {
    PROCESSING = 0,
    SUCCESS = 1,
    FAIL = 2,
    WAIT = 3
}

struct ChnlbindSyncRecord {
    1: required i64 id,
    2: required ChnlbindRecord chnlbind_record,
    3: required string batch_id,                 // 批次号
    4: required string src,                      // 进件来源
    5: required string trace_no,                 // 内部追踪号
    6: required string out_trace_no,             // 外部追踪号
    7: required string sync_plan_time,           // 计划同步时间
    8: required string sync_time,                // 实际同步时间
    9: required CHNLBIND_SYNC_STATE sync_state,  // 同步状态
    10: required string errmsg,
}

struct ChnlbindSyncUpdateArg {
    1: required i64 id,
    2: optional ChnlbindRecord chnlbind_record,  // chnlbind 参数, 暂不支持修改, 仅预留
    3: optional string chnlbind_sync_time,       // 计划同步时间
}


// 本地挂靠
struct LinkArg{
    1: required string mchnt_id,    // 被挂靠的商户号
    2: required CHNLCODE chnlcode,  // 进件通道
    3: required list<i64> userids,  // 要挂靠的userid
    4: required string batch_id,  // 批次号,保证每次不重复
    5: required string src,  // 发起方服务名称， 如apollo.1、addmchnt_mis.0
    6: optional string chnlbind_sync_time,  // 同步到 chnlbind 时间.
}

service weifutong {

    string ping(),

    /*
     * 富友-微信、支付宝
     */
    # 富友上传图片
    # 富友更新
    StoreNewResult update_mchnt_fuiou(1: UpdateFY fy) throws(1:WeifutongError e);
    # 富友微信参数查询
    /*list<WechatConfFY> wechat_config_get_fuiou(1: string mchnt_id) throws(1: WeifutongError e);*/
    # 富友微信参数配置
    /*list<WechatConfFYResp> wechat_config_set_fuiou(1: list<WechatConfFY> wcf) throws(1: WeifutongError e);*/

    # 生成电子协议
    /*ElecContractInfo elec_contract_gen_fuiou(1: string mchnt_id, 2: string trace_no) throws(1: WeifutongError e);*/
    # 签署电子协议
    /*void elec_contract_sign_fuiou(1: string mchnt_id, 2:string trace_no, 3: ElecContractInfo eci) throws(1: WeifutongError e);*/



    /*
     * 汇宜普通-微信、支付宝
     */
    # 更新, 更新失败抛出异常, 成功不返回, 费率是百分制
    void update_mchnt_huiyi_normal(1: UpdateReq ur) throws(1:WeifutongError e);

    // 微信直连注册查询
    WeixinRegisterQueryResp store_new_weixin_register_query(1: WeixinRegisterQuery snr) throws(1:WeifutongError e);
    // 微信直连签约
    StoreNewResult sign_contract_weixin(1: WeixinSignContractArg arg) throws(1:WeifutongError e);
    // 微信直连配置查询
    list<WechatConf> weixin_config_query(1:WeixinConfigQuery arg) throws(1: WeifutongError e);

    // 合利宝注册查询, 如果审核通过会返回签约 url.
    HelibaoStoreNewQueryResp store_new_query_helibao(1:HelibaoStoreNewQueryArg arg) throws(1:WeifutongError e);
    // 合利宝签约查询, 如果签约成功会自动调用开通产品, 报备和微信公众号进件.
    HelibaoAgreementQueryResp agreement_query_helibao(1:HelibaoAgreementQueryArg arg) throws(1:WeifutongError e);

    //// 各种快捷支付通道 ////
    /*
     * 汇宜-快捷支付
    */
    # 汇宜快捷进件
    StoreNewResult store_new_huiyi(1: StoreNewHuiyi arg) throws(1:WeifutongError e);
    # 汇宜快捷查询
    HuiyiQueryResp store_query_huiyi(1: string mchnt_id) throws(1:WeifutongError e);
    # 汇宜注册信息变更
    void update_mchnt_huiyi(1: HuiyiUpdateArg hua) throws(1:WeifutongError e);
    # 汇宜注销
    list<CancelledResp> cancel_huiyi(1:list<string> mchnt_ids) throws(1:WeifutongError e);


    /*
     * 大则不带积分-快捷支付
     */
    # 大则进件
    StoreNewResult store_new_daze(1: StoreNewDZ wc) throws(1:WeifutongError e);


    /*
     * 大则积分-快捷支付
     */

    StoreNewResult store_new_dazepoint(1: StoreNewReq snr) throws(1:WeifutongError e);
    void update_mchnt_dazepoint(1: UpdateReq ur) throws(1:WeifutongError e);


    /*
     * 收款宝-快捷支付
     */

    StoreNewResult store_new_yeepay(1: StoreNewReq snr) throws(1:WeifutongError e);
    void update_mchnt_yeepay(1: UpdateReq ur) throws(1:WeifutongError e);


    /*
     * 聚合汇通-快捷支付
     */

    StoreNewResult store_new_huitong(1: StoreNewReq snr) throws(1:WeifutongError e);
    void update_mchnt_huitong(1: UpdateReq ur) throws(1:WeifutongError e);

    // 数据传递给微信/支付宝(针对已经进过件)
    string data_penetrate(1:DataPenetrateArg sda) throws(1:WeifutongError e);


    ////  其它通用接口 ////
    /*
     根据userid查询注册的商户号
     */
    map<i64, list<string>> query_mchntid_by_uids(1:list<i64> uids, 2:CHNLCODE chnlcode) throws(1:WeifutongError e);

    // 进件记录相关
    /*
    * 返回进件记录ID列表
    * */
    list<i64> addmchnt_query(1: AddMchntQueryArg q) throws(1:WeifutongError e);
    /*
    * 根据进件记录ID，获取进件记录
    * */
    map<i64, AddMchntRecord> addmchnt_get(1:list<i64> l) throws(1:WeifutongError e);

    // 关注记录相关
    list<i64> subscribeappid_query(1: SubscribeQueryArg q) throws(1:WeifutongError e);
    map<i64, SubscribeAppidRecord> subscribeappid_get(1:list<i64> l) throws(1:WeifutongError e);

    /*
    * 通用商户进件接口
    * */
    StoreNewResult register_mchnt(1:StoreNewReq snr) throws(1:WeifutongError e);

    /*
     进件成功后, 对商户号追加关注
     */
    void append_wechatconf(1:AppendWechatConfArg arg) throws(1:WeifutongError e);

    /*
     * 配置微信参数
     */
    /*WechatConf set_wechatconf(1:WechatConfReq weconf) throws(1:WeifutongError e);*/

    /*
    * 通用商户信息更新接口
    * */
    void update_mchnt(1:UpdateReq ur) throws(1:WeifutongError e);

    /*
     * 通用商户信息更新查询接口
     */
    UpdateMchntResp update_mchnt_query(1:UpdateQueryReq req) throws(1:WeifutongError e);

    /*
    * 查询通道商户信息
    * */
    string query_mchnt(1:StoreQueryReq req) throws(1:WeifutongError e);

    // 上传图片统一接口
    string upphoto(1: UpPicArg upa) throws(1:WeifutongError e);

    // 开通服务
    TradeRet OpenService(1:ServiceArg sa) throws(1:WeifutongError e);
    // 查询, 目前仅支持网商商户银行账户
    TradeRet OpenServiceQuery(1:ServiceArg sa) throws (1:WeifutongError e);
    // 发送验证码
    void SendSms(1:SendSmsArg sms) throws(1:WeifutongError e);

    // 查询 / 修改 chnlbind 同步记录
    list<i64> chnlbind_sync_query(1:ChnlbindSyncQueryArg q) throws(1:WeifutongError e);
    map<i64, ChnlbindSyncRecord> chnlbind_sync_get(1:list<i64> ids) throws(1:WeifutongError e);
    /*
     注意下面情况
     1. 同步状态已经确定的(成功/失败), 不能做更新
     2. 计划同步时间 < 当前时间的不能做更新
     3. 当前时间距离计划同步时间 < 5min, 不能做更新
     */
    map<i64, ChnlbindSyncRecord> chnlbind_sync_update(1:list<ChnlbindSyncUpdateArg> req, 2:i64 admin) throws(1:WeifutongError e);


    ////  特殊接口 ////
    void wechatconf_update(1:WechatConfUpdateArg arg) throws(1:WeifutongError e);
    /*
       商户注册异步接口
     */
    void register_mchnt_async(1:list<StoreNewReq> l) throws(1:WeifutongError e);
    void link_mchnt_local(1:LinkArg la) throws(1:WeifutongError e);
}
