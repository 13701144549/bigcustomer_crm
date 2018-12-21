namespace py fenqi_api

exception FenqiException {
	1: string           respcd;         //异常码
	2: string           respmsg;         //异常描述信息
}

// 用户状态
enum USER_STATUS {
	NOT_BIND=1,  // 未绑定手机号
	BIND=2,  // 已绑定手机号，未激活
	ACTIVED=3, // 已绑定手机号并激活
	FORBIDDEN=4,  // 已注销
}

// 运营状态
enum RUNNING_STATUS {
	RUNNING=1,
	CLOSED=2,
}

enum BIND_STATUS {
	BIND=1, // 绑定
	NOT_BIND=2, // 解绑
}

enum BIND_TYPE {
	COLLECT=1,
	REPAY=2,
}

enum USER_ROLE {
	OPUSER=1,  // 销售人员
//    STORE=2,  // 门店（商户）。交易发生所在，最小的USERID
	STORE_MGR=3,  // 门店管理人员。 可管理多个门店
//    DISTRICT=4,  // 大区
	DISTRICT_MGR=5,  // 大区负责人
	PARTNER=6,  // 合作商
	LENDER=7,  // 放款方（资金提供方）
	BORROWER=8,  // 借款人
}

// 个人贷款用户授权状态
enum BORROWER_STATUS {
	NOT_CREDIT=1, // 未授信
	REALNAME=2, // 实名认证完成
	CREDIT_WAIT=3, // 授信等待
	CREDIT_PASS=4, //授信通过
	CREDIT_FAIL=5, //授信失败
	CREDIT_FACE=6, // 活体授信放弃
}

//  个人贷款 借款记录状态
enum LOAN_TRADE_STATUS {
	APPLYING=1, // 申请中
	CREDITING=2, // 放款中
	REPAYING=3, // 还款中
	SETTLE=4, // 已还清
	APPLY_REFUSE=5, // 申请拒绝
	CREDIT_FAIL=6, // 放款失败
	OVERDUE=7, // 已逾期
}

// 个人贷款 还款计划状态
enum REPAY_STATUS {
	WAITING=1, //待还款
	CLOSE=2, //已还清
	OVERDUE=3, //已逾期
	REPAYING=4, //还款中
}

//  商户贷 分期状态
enum LOAN_STATUS {
	APPLYING=1, // 申请中
	APPROVING=2, // 审批中
	SIGNING=3, // 待签约
	SIGNED=4, // 签约完成
	REPAYING=5, // 还款中
	OVERDUE=6, // 已逾期
	SETTLE=7, // 已结清
	APPLY_REFUSE=8, // 申请拒绝
	FIRST_AUDIT=9, // 初审通过
	FIRST_AUDIT_AMOUNT=10, // 用户选择初审提额
	PROJECT_END=11, // 项目终止
	GIVE_UP=12, // 客服放弃
}

// 销售
struct Opuser {
	1: optional i64 userid;
	2: optional i64 store_uid;        // 所属门店的USERID，创建必传。
	3: optional string idnumber;     // 身份证号码
	4: optional string name;         // 销售姓名
	5: optional USER_STATUS status;
	6: optional i64 cid;
	7: optional string utime;  // 更新时间， 如： 2018-01-30 00:12:33
}

// 门店
struct Store {
	1: optional i64 userid;
	2: optional i64 store_mgr_uid;  // 门店管理者USERID
	3: optional i64 district_id;  // 所属大区ID
	4: optional string address;  // 门店地址
	5: optional string shop_name;  // 门店名称
}

// 门店管理者
struct StoreMgr {
	1: optional i64 userid;
	2: optional USER_STATUS status;
	3: optional string name;  // 门店管理者姓名
	4: optional string idnumber; // 门店管理者身份证号码
	5: optional i64 district_id;  // 所属大区ID
	6: optional i64 cid;
	7: optional string utime;  // 更新时间， 如： 2018-01-30 00:12:33
}

// 大区
struct District {
	1: optional i64 id;
	2: optional i64 district_mgr_uid;  // 大区负责人的USERID
	3: optional string name;  // 大区名称
}

// 大区负责人
struct DistrictMgr {
	1: optional i64 userid;
	2: optional i64 partner_uid;  // 合作商的USERID
	3: optional USER_STATUS status;
	4: optional string name;      // 大区负责人姓名
	5: optional string idnumber;  // 大区负责人身份证号码
	6: optional i64 cid;
	7: optional string utime;  // 更新时间， 如： 2018-01-30 00:12:33
}

// 合作商
struct Partner {
	1: optional i64 userid;
	2: optional string name;
	3: optional RUNNING_STATUS status;  // 运行状态
	4: optional string join_dtm;  // 加入时间， 如： 2018-01-30 00:12:33
	5: optional string contact_name;  // 联系人姓名
	6: optional string contact_mobile;  // 联系人手机号
	7: optional string app_key;  // 合作商 key
	8: optional string ext;  //  额外的信息
	9: optional i64 saleman_uid;  //  额外的信息

}

// 放款人
struct Lender {
	1: optional i64 userid;
	2: optional string name;                 // 放款方名称
	3: optional RUNNING_STATUS status;
	4: optional string joindtm;              // 加入时间
	5: optional string contact_name;         // 联系人姓名
	6: optional string contact_mobile;        // 联系人手机号
}

// cid user 绑定关系
struct Cid2user {
	1: optional i64 cid; // 借款人的CID
	2: optional i64 userid; // 用户 id
	3: optional i64 role;   // 用户角色。 销售人员=1，门店管理人员=3，大区负责人=5，合作商=6，放款方=7，借款人=8
	4: optional i64 mobile; // 手机号
}

// 借款人
struct Borrower {
	1: optional i64 id;                       // borrower_id
	//2: optional i64 cid;                     // 借款人的CID
	//3: optional i64 userid;                  // 借款人用户id
	4: optional BORROWER_STATUS status;     // 用户状态
	5: optional string mobile;                  // 手机号
	6: optional string name;                  // 姓名
	7: optional string idnumber;              // 身份证号码
	8: optional i64 is_student;               // 是否是学生
	9: optional string contact;               //联系人信息
	10: optional i64 loan_txamt;               //总借款金额
	11: optional i64 remain_loan_txamt;       //剩余借款金额
	12: optional i64 due_date;                // 还款日
	13: optional string agreement;             // 协议相关
	15: optional string reason;                 // 状态原因
	16: optional string reason_detail;          // 详细原因
	17: optional string face_biz;              // face ++ id
	18: optional i64 cardbind_id;              // 自动还款卡id
	19: optional i64 partner_uid;              // 合作商用户id
	20: optional string extra_userid;          // 第三方传递借款人用户id
}

struct BorrowerBase {
	1: optional i64 cid;                     // 借款人的CID
	2: optional i64 userid;                  // 借款人用户id
	3: optional BORROWER_STATUS status;     // 用户状态
	4: optional string reason;             // 状态原因
	5: optional string reason_detail;      // face ++ 返回原因
	6: optional string face_biz;           // face ++ biz_no
	7: optional i64 cardbind_id;           // 自动还款卡id
	8: optional i64 step_refuse;           // 拒绝公司
	9: optional string status_utime;        // 查询状态更新时间
	10: optional string ctime;              // 创建时间
    11: optional i64 partner_uid;          // 添加合作商id 
}

struct BorrowerProfile {
	1: optional string mobile;                  // 手机号
	2: optional string name;                  // 姓名
	3: optional string idnumber;              // 身份证号码
	4: optional i64 is_student;               // 是否是学生
	5: optional string contact;               //联系人信息
	6: optional i64 borrower_id;              // 用户id
}

struct BorrowerCredit {
	1: optional i64 loan_txamt;               //总借款金额
	2: optional i64 remain_loan_txamt;       //剩余借款金额
	3: optional i64 due_date;                // 还款日
	4: optional string agreement;             // 协议相关
	5: optional i64 borrower_id;              // 用户id
}

struct BorrowerPartner {
	1: optional i64 borrower_id;              // 用户id
	2: optional string extra_userid;          // 第三方上传的用户 id
	3: optional i64 partner_uid;              // 合作商用户id
}

//商户贷 贷款记录情况
struct LoanRecord {
	1: optional i64 userid;
	2: optional string orderno;                 // 订单号
	4: optional string chnlno;                 // 外部流水
	5: optional i64 lender_uid;                 // 放款方 userid
	6: optional i64 apply_amt;                  // 申请金额
	7: optional i64 loan_amt;                   // 放款金额
	8: optional LOAN_STATUS status;            // 审核状态
	9: optional string chnl_dtm; // 放款时间 如： 2018-01-30 00:12:33
	10: optional string join_time; // 创建时间
	11: optional string mobile; // 手机号
}

// 银行卡相关信息
struct CardBind {
	1: optional i64 borrower_id; // 借款人id
	2: optional string bankname; // 银行名称
	4: optional string bankuser; // 银行开户名
	5: optional string bankaccount; //银行卡账号
	6: optional string bankmobile; // 银行绑定手机号
	7: optional string brchbank_code; // 开户行银联号
	8: optional BIND_STATUS bind_status; // 绑卡状态
	9: optional BIND_TYPE bind_type; // 绑卡用途
}

// 申请借款记录
struct LoanTrade {
	1: optional i64 borrower_id; // 借款人id
	2: optional i64 lender_uid; // 放款方用户id
	3: optional string orderno; //  订单号
	4: optional string purpose; // 借款用途
	5: optional i32 periods; //分期期数
	6: optional LOAN_TRADE_STATUS status; // 借款状态
	7: optional i64 cardbind_id; // 银行卡 id
	8: optional i64 loan_amt; // 借款金额
	9: optional i64 repay_amt; // 已还金额
	10: optional i64 repay_way; // 还款方式
	11: optional string loan_dtm; // 申请借款时间
	12: optional string agreement; // 借款记录协议
	13: optional string reason; // 借款失败原因
	14: optional i64 disburse_at; // 放款时间 毫秒
	15: optional string repay_end_dtm; //最后还款时间
	16: optional string status_utime; //状态更新时间
	17: optional i64 partner_uid; // 合作商用户id
}

// 还款计划
struct RepayPlan {
	1: optional string loan_orderno; // 借款流水
	2: optional i64 installment_no; // 当前期数
	3: optional string repay_start_dtm; //  起息日期
	4: optional string repay_plan_dtm; // 计划还款日期
	5: optional string repay_real_dtm; // 实际还款日期
	6: optional REPAY_STATUS status; // 当期状态
	8: optional i64 repay_origin_amt; // 还款本金
	9: optional i64 repay_interest_amt; // 应还款利息
	10: optional i64 overdue_amt; //  逾期利息
	11: optional i64 overdue_day; //  逾期天数
	12: optional i64 repay_real_amt; // 实际还款利息
}

// 还款记录
struct RepayRecord {
	1: optional string repay_syssn; // 还款流水
	2: optional i64 repay_amt; // 本次还款总金额
	3: optional i64 cardbind_id; //  银行卡 id
	4: optional i64 repay_method; //  还款方式
	6: optional i64 status;	// 还款记录状态
	7: optional string repay_dtm; // 还款日期
	8: optional i64 borrower_id; // 借款人id
	9: optional string reason; // 还款失败原因
	10: optional string repayplan_ids; // 对应的还款计划id
}

// 查询元数据
struct QueryMeta {
	1: required i64             offset=0;           // 偏移, 默认从 0 开始
	2: required i64             count=100;          // 记录数, 默认 100 条
	3: optional string          orderby;            // 排序方式, 不同的查询支持的字段不同, 详情参照具体接口的注释。
}

// 销售人员查询参数
struct OpuserQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> store_uids;                // 所属门店的USERID
	5: optional list<i64> userids;                   // USERID
	6: optional list<string> idnumbers;              // 身份证号码
	7: optional string name;                         // 销售姓名
	8: optional list<USER_STATUS> status;            // 用户状态
	9: optional list<i64> cids;                      // customer服务的CID
}

// 门店查询参数
struct StoreQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userids;
	5: optional list<i64> store_mgr_uids;           // 门店管理者USERID
	6: optional list<i64> district_ids;             // 所属大区ID
	7: optional string address;                     // 门店地址
	8: optional string shop_name;                        // 门店名称
}

// 门店管理人员查询参数
struct StoreMgrQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userids;
	5: optional list<USER_STATUS> status;
	6: optional string name;                        // 门店管理者姓名
	7: optional list<string> idnumbers;             // 门店管理者身份证号码
	8: optional list<i64> district_ids;             // 所属大区ID
	9: optional list<i64> cids;                 // customer服务的CID
}

// 大区查询参数
struct DistrictQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional string name;                         // 大区名称
	5: optional list<i64> district_mgr_uids;         // 大区负责人的USERID
	6: optional list<i64> district_ids;         // 大区 ID
}

// 大区负责人查询参数
struct DistrictMgrQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userids;
	5: optional list<i64> partner_uids;             // 合作商的USERID
	6: optional list<USER_STATUS> status;
	7: optional string name;                        // 大区负责人姓名
	8: optional list<string> idnumbers;             // 大区负责人身份证号码
	9: optional list<i64> cids;                 // customer服务的CID
}

// 合作商查询参数
struct PartnerQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userid_list;               // 用户 id
	5: optional string name;
	6: optional list<RUNNING_STATUS> status_list;     // 运行状态
	7: optional string contact_name;
	8: optional list<string> contact_mobile_list;
	9: optional list<i64> saleman_uid_list;
}

// 放款人查询参数
struct LenderQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userids;
	5: optional string name;
	6: optional list<RUNNING_STATUS> status;         // 运行状态
}

// Cid2user 查询参数
struct Cid2userQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> cids;                     // 借款人的CID
	5: optional list<i64> userids;                  // 用户 id
	6: optional list<i64> roles;                    // 用户角色
	7: optional list<i64> mobiles;                  // 手机号
}

// loanRecordArg 查询参数
struct LoanRecordArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_time;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_time;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> userid_list;                     // 用户 id
	5: optional list<string> orderno_list;                 // 订单号
	6: optional list<LOAN_STATUS> status_list;              // 放款状态
	8: optional list<i64> lender_uid_list;             // 借款人id
	7: optional list<string> mobile_list;             // 借款人手机号
}

// 借款人基本信息查询参数
struct BorrowerBaseQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_ctime;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_ctime;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> cid_list;                      // customer服务的CID
	5: optional list<i64> userid_list;                   // 用户 id
	6: optional list<BORROWER_STATUS> status_list;       // 用户状态
	7: optional list<i64> partner_uid_list;              // 合作商用户 id
	8: optional string reason;
}

// 借款人profile查询参数
struct BorrowerProfileQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<string> mobile_list;               // customer服务的CID
	5: optional string name;                         // 姓名
	6: optional list<string> idnumber_list;                   // 身份证号
	7: optional list<i64> borrower_id_list;          // 借款人id
}

// 借款人借款相关查询参数
struct BorrowerCreditQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> borrower_id_list;          // 借款人id
	5: optional list<i64> due_date_list;       // 还款日
}

// 借款人借款相关查询参数
struct BorrowerPartnerQueryArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> borrower_id_list;          // 借款人id
	5: optional list<string> extra_userid_list;       // 第三方上传用户id 查询参数
	6: optional list<i64> partner_uid_list;          // 合作商用户id查询
}


// 银行卡查询
struct CardBindArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_join_dtm;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_join_dtm;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<i64> borrower_id_list;          // 借款人id
	5: optional list<i64> bind_status_list;
	6: optional string bankname;
	7: optional string bankuser;
	8: optional list<i64> bind_type_list;
	9: optional list<string> bankaccount_list;
	10: optional list<string> bankmobile_list;
}

// 申请借款记录 查询
struct LoanTradeArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_ctime;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_ctime;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'
	4: optional list<i64> borrower_id_list; // 借款人id
	5: optional list<i64> lender_uid_list; // 放款方用户id
	6: optional list<string> orderno_list; //  订单号
	7: optional string purpose; // 借款用途
	8: optional list<i32> periods_list; //分期期数
	9: optional list<LOAN_TRADE_STATUS> status_list; // 借款状态
	10: optional list<i64> partner_uid_list; // 合作商用户 id 查询
}

// 还款计划 查询
struct RepayPlanArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_ctime;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_ctime;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'
	4: optional list<string> loan_orderno_list; // 借款流水
	5: optional list<i64> installment_no_list; //  当前期数流水
	6: optional list<REPAY_STATUS> status_list;	// 当期状态
	7: optional list<string> repay_syssn_list; // 还款流水号
}

// 还款记录 查询
struct RepayRecordArg {
	1: required QueryMeta query_meta;                // 查询元数据
	2: optional string s_ctime;                   // 最早注册时间. 形如: '2016-01-02 12:22:33'
	3: optional string e_ctime;                   // 最晚注册时间. 形如: '2016-01-30 12:22:33'

	4: optional list<string> repay_syssn_list; // 还款流水
	5: optional list<i64> borrower_id_list; //  用户id
	6: optional list<i64> repay_method_list; //  还款方式
	7: optional list<i64> status_list;	// 还款记录状态
}

service FenqiServer {

	/// 销售人员 ///
	Opuser opuser_create(1:Opuser info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> opuser_query(1:OpuserQueryArg q) throws (1:FenqiException e);
	map<i64, Opuser> opuser_get(1:list<i64> l) throws (1:FenqiException e);
	void opuser_update(1:map<i64, Opuser> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 门店 ////
	Store store_create(1:Store info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> store_query(1:StoreQueryArg q) throws (1:FenqiException e);
	map<i64, Store> store_get(1:list<i64> l) throws (1:FenqiException e);
	void store_update(1:map<i64, Store> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 门店管理人员 ////
	StoreMgr store_mgr_create(1:StoreMgr info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> store_mgr_query(1:StoreMgrQueryArg q) throws (1:FenqiException e);
	map<i64, StoreMgr> store_mgr_get(1:list<i64> l) throws (1:FenqiException e);
	void store_mgr_update(1:map<i64, StoreMgr> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 大区 ////
	District district_create(1:District info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> district_query(1:DistrictQueryArg q) throws (1:FenqiException e);
	map<i64, District> district_get(1:list<i64> l) throws (1:FenqiException e);
	void district_update(1:map<i64, District> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 大区责任人 ////
	DistrictMgr district_mgr_create(1:DistrictMgr info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> district_mgr_query(1:DistrictMgrQueryArg q) throws (1:FenqiException e);
	map<i64, DistrictMgr> district_mgr_get(1:list<i64> l) throws (1:FenqiException e);
	void district_mgr_update(1:map<i64, DistrictMgr> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 合作商 ////
	Partner partner_create(1:Partner info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> partner_query(1:PartnerQueryArg q) throws (1:FenqiException e);
	map<i64, Partner> partner_get(1:list<i64> l) throws (1:FenqiException e);
	void partner_update(1:map<i64, Partner> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 放款人 ////
	Lender lender_create(1:Lender info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> lender_query(1:LenderQueryArg q) throws (1:FenqiException e);
	map<i64, Lender> lender_get(1:list<i64> l) throws (1:FenqiException e);
	void lender_update(1:map<i64, Lender> infos, 2:i64 admin) throws (1:FenqiException e);

	//// ci2 和 user 映射表 ////
	Cid2user cid2user_create(1:Cid2user info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> cid2user_query(1:Cid2userQueryArg q) throws (1:FenqiException e);
	map<i64, Cid2user> cid2user_get(1:list<i64> l) throws (1:FenqiException e);
	void cid2user_update(1:map<i64, Cid2user> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 订单查询 ////
	LoanRecord loanrecord_create(1:LoanRecord info, 2:i64 admin) throws (1:FenqiException e);
	list<i64> loanrecord_query(1:LoanRecordArg q) throws (1:FenqiException e);
	map<i64, LoanRecord> loanrecord_get(1:list<i64> l) throws (1:FenqiException e);
	void loanrecord_update(1:map<i64, LoanRecord> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 借款人 相关 ////
	Borrower borrower_create(1:Borrower info, 2:i64 admin) throws (1:FenqiException e);

	/// 借款人基本信息查询更新 ///
	list<i64> borrower_base_query(1:BorrowerBaseQueryArg q) throws (1:FenqiException e);
	map<i64, BorrowerBase> borrower_base_get(1:list<i64> l) throws (1:FenqiException e);
	void borrower_base_update(1:map<i64, BorrowerBase> infos, 2:i64 admin) throws (1:FenqiException e);
	/// 借款人profile 查询更新 ///
	list<i64> borrower_profile_query(1:BorrowerProfileQueryArg q) throws (1:FenqiException e);
	map<i64, BorrowerProfile> borrower_profile_get(1:list<i64> l) throws (1:FenqiException e);
	void borrower_profile_update(1:map<i64, BorrowerProfile> infos, 2:i64 admin) throws (1:FenqiException e);
	/// 借款人授权信息查询更新 ///
	list<i64> borrower_credit_query(1:BorrowerCreditQueryArg q) throws (1:FenqiException e);
	map<i64, BorrowerCredit> borrower_credit_get(1:list<i64> l) throws (1:FenqiException e);
	void borrower_credit_update(1:map<i64, BorrowerCredit> infos, 2:i64 admin) throws (1:FenqiException e);

	/// 借款人与合作商信息创建 更新///
	BorrowerPartner borrower_partner_create(1: BorrowerPartner info, 2: i64 admin ) throws (1: FenqiException e);
	list<i64> borrower_partner_query(1:BorrowerPartnerQueryArg q) throws (1:FenqiException e);
	map<i64, BorrowerPartner> borrower_partner_get(1:list<i64> l) throws (1:FenqiException e);
	void borrower_partner_update(1:map<i64, BorrowerPartner> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 银行卡绑定相关 ///
	CardBind cardbind_create(1:CardBind info, 2:i64 admin ) throws (1:FenqiException e);
	list<i64> cardbind_query(1:CardBindArg q) throws (1:FenqiException e);
	map<i64, CardBind> cardbind_get(1:list<i64> l) throws (1:FenqiException e);
	void cardbind_update(1:map<i64, CardBind> infos, 2:i64 admin) throws (1:FenqiException e);

	////  申请借款记录 ///
	LoanTrade loantrade_create(1:LoanTrade info, 2:i64 admin ) throws (1:FenqiException e);
	list<i64> loantrade_query(1:LoanTradeArg q) throws (1:FenqiException e);
	map<i64, LoanTrade> loantrade_get(1:list<i64> l) throws (1:FenqiException e);
	void loantrade_update(1:map<i64, LoanTrade> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 还款计划表 ///
	RepayPlan repayplan_create(1:RepayPlan info, 2:i64 admin ) throws (1:FenqiException e);
	list<i64> repayplan_query(1:RepayPlanArg q) throws (1:FenqiException e);
	map<i64, RepayPlan> repayplan_get(1:list<i64> l) throws (1:FenqiException e);
	void repayplan_update(1:map<i64, RepayPlan> infos, 2:i64 admin) throws (1:FenqiException e);

	//// 还款记录 ///
	RepayRecord repayrecord_create(1:RepayRecord info, 2:i64 admin ) throws (1:FenqiException e);
	list<i64> repayrecord_query(1:RepayRecordArg q) throws (1:FenqiException e);
	map<i64, RepayRecord> repayrecord_get(1:list<i64> l) throws (1:FenqiException e);
	void repayrecord_update(1:map<i64, RepayRecord> infos, 2:i64 admin) throws (1:FenqiException e);
}
