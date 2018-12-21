//用户类别
struct UserCate {
    1: required string			code;				//类别代码，如：saleman，merchant
    2: optional string 			name;				//类别名称，如：业务员,商户
    3: optional string			ctime;				//创建时间
	4: optional i32				status=1;				//状态，1：有效 0：无效， 默认为1
    5: optional string          remark=''           //类型注释, 默认为空
}

//用户标签
struct UserTag{
    1: required string 			name;				// 标签名称 如:submchnt
    2: optional string			ctime;				// 创建时间
    3: optional string          content;            // 标签备注 如:yyk的一号小店
}

//用户开通服务
struct UserService{
    1: required string 			code;				//服务代码，如：
    2: optional string 			name;				//服务名称，如：买单，外卖
    3: optional string 			starttime;			//服务开始时间，YYYY-MM-DD HH:SS:mm
    4: optional string 			endtime;			//服务结束时间，YYYY-MM-DD HH:SS:mm
    5: optional i32 			status;				//服务开通状态
    6: optional string 			memo;				//服务备注
    7: optional string			ctime;				//创建时间
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

//用户基本信息
struct User{
    1: required i64			    uid = 0;			//用户唯一id
    2: required string 			name = "";			//用户名称
    3: required string 			shopname = "";		        //店铺名称
    4: required string 			email = "";			//用户的email
    5: required string 			mobile = "";		        //手机号码
    6: optional string			telephone;			//座机电话
    7: optional string 			password;			//密码
    8: optional i32			    state;				//状态
    9: optional string			idnumber;			//身份证号
    10: optional string			province;			//所在省份
    11: optional string			city;				//所在城市
    12: optional string			mcc;				//商户mcc
    13: optional string			address;			//商户地址
    14: optional double			longitude = 0.0;	        //商户gps经度
    15: optional double			latitude = 0.0;		        //商户gps维度
    16: optional list<UserCate> userCates;	                //用户类别
    17: optional string			jointime;			//用户创建时间，为"YYYY-MM-DD HH:SS:mm"
    18: optional i32			risklevel = 0;		//风控等级
    19: optional i32			groupid = 0;		// 渠道id
    20: optional i32            user_type = 1;      // 用户类型
    21: optional string         legalperson;        // 法人姓名
    22: optional string         businessaddr;       // 经营地址
    23: optional string         licensenumber;      // 营业执照编号
}

// 图片信息
struct ImgInfo {
    1: required string          name;            // 图片标志如idcardfront等等
    2: required string          imgname;         // 图片名字
}

// 注册商户时候需要到的信息
struct RegisterAllInfo{
    1: required string          username = "";      // 用户名(注册手机号)
    2: optional string          password = '';      // 密码(6-20位)
    3: required string          bankuser = "";      // 开户名
    4: required string          idnumber = "";      // 身份证号
    5: optional i32             banktype = 1;       // 账户类型，1，为对私，2为对公 ，默认为对私
    6: required string          bankprovince = "";  // 支行所在省份
    7: required string          bankcity = "";      // 支行所属城市
    8: required string          bankname = "";      // 支行名称 (如 燕北支行)
    9: required string          headbankname = "";  // 所属总行名称(如 工商银行)
    10: required string         bankcode = "";      // 联行号
    11: required string         bankaccount = "";   // 开户银行号
    12: optional string         bankmobile = "";    // 开户银行预留手机号
    13: required string         shopname;           // 店铺名称
    14: required string         province;           // 所在省份
    15: required string         city;               // 所在市
    16: required string         address;            // 详细地址 (如t3 a17)
    17: optional string         landline = "";      // 座机
    18: optional double         longitude;          // 经度，double型
    19: optional double         latitude;           // 纬度，double型
    20: required string         tenpay_ratio;       // 微信支付费率
    21: required string         alipay_ratio;       // 支付宝费率
    22: required string         jdpay_ratio;        // 京东费率
    23: required string         qqpay_ratio;        // qq钱包费率
    24: required string         credit_ratio;       // 信用卡费率
    25: required string         debit_ratio;        // 借记卡费率
    26: optional string         idstatdate;         // 身份证有效开始日期(格式：2016-01-05)
    27: optional string         idenddate;          // 身份证有效截止日期(格式：2017-01-05)
    28: optional i32            usertype;           // 1小微  2个体 3企业
    29: optional string         legalperson;        // 法人姓名(不填同bankuser)
    30: optional string         name;               // 商户姓名(不填同bankuser)
    31: optional string         mode;               // 注册模式 bigmchnt, mchnt
    32: optional i32            big_uid;            // 大商户userid
    33: required list<ImgInfo>  imgInfos;           // 图片均为选传
    34: required string         mcc;                // 商户的mcc
    35: required i32            groupid;            // 商户的groupid
    36: optional i32            userid;             // 商户的userid, 如果已经预注册有了userid,便不再生成
    37: required string         src;                // 注册来源
    38: optional string         licensenumber;      // 营业执照号
}


// 用户简洁信息
struct UserBrief{
    1:  required i64	        uid = 0;        // 用户唯一id
    2:  required string         shopname = "";  // 店铺名称
    3:  required string         email = "";     // 用户的email
    4:  required string         mobile = "";	// 手机号码
    5:  optional i32	        state;          // 状态
    6:  optional string	        province;	    // 所在省份
    7:  optional string	        city;		    // 所在城市
    8:  optional string         address;	    // 商户地址
    9:  optional string			jointime;	    // 用户创建时间，为"YYYY-MM-DD HH:SS:mm"
    10: optional i32			groupid = 0;    // 渠道id
    11: optional string         name= "";    // 商户姓名
    12: optional string         username= "";    // 登录账号
}


// 用户扩展信息
struct UserExt{
    1: required i64 uid = 0;            // 用户唯一id
    2: optional i64	regionid;       // 商圈id
    3: optional i64 shoptype_id;    // 店铺类型id
    4: optional string contact;    // 联系方式
    5: optional string logo_url;   // logo图片
    6: optional string head_img;   // 背景图片
    7: optional string ctime;      // 创建时间
    8: optional string utime;      // 更新时间
}

// 用户操作员信息
struct Opuser{
    1: required i64 uid = 0;       // 用户唯一id
    2: optional i64	opuid = 0;     // 操作员id
    3: optional string opname;     // 操作员名称
    4: optional string mobile;     // 联系方式
    5: optional string password;   // 密码
    6: optional i32 status;     // 状态 1:启用 2:关闭
    7: optional string ctime;      // 创建时间
    8: optional string utime;      // 更新时间
}


//用户信息，包括用户基本信息
struct UserProfile{
    1: required i64			    uid = 0;			//用户唯一id
    2: required User 			user;				//用户基本信息
    3: optional BankInfo		bankInfo;			//开户银行信息
    4: optional list<UserTag> 	userTags;			//用户标签
    5: optional list<User> 		relations;			//用户的所属关系，比如，业务员，渠道....		
}

struct UserQuery{
    1: optional list<i64> 		uids;				
    2: optional list<string> 	mobiles;				
    3: optional i32             state;
    4: optional list<string> 	names;				
    5: optional list<string>	catenames;
    6: optional list<string>	tagnames;
}

struct UserRelation{
    1: i64                      userid;
    2: string                   link_cate;
}

//用户权限
struct Permission{
    1: string name;  // 权限名称   XXX查看权限
    2: string code;  // 权限代码   can_read_xxx
    3: string group; // 权限组名称 权限组名称默认为空
    4: i64 id;       // 权限id
    5: i32 status;   // 权限状态
}

//权限角色
struct PermissionRole{
    1: string 				name;     			//角色名称      审核专员
    2: string 				code;			     	//角色代码      account_auditer
    3: string 				group;    			//角色组名称    权限组名称默认为空  
}
//上面两个group，不必一一对应

//定义一个基本异常
exception ApolloException {
    1: string 				respcd;				//异常码
    2: string 				respmsg;			//异常描述信息
}

//推荐类型
enum RecommendType {
    SALESMAN=1,								//业务员推荐
}


service ApolloServer{
    //监控接口
    void ping() throws (1:ApolloException e);
    
    //// 用户注册接口
    // 预注册用户 username mobile email  返回userid, 失败返回0
    i64 preRegister(1:string username, 2:string password, 3:string email) throws (1:ApolloException e);

    //注册用户，提交用户信息
    i64 registerUser(1:UserProfile userProfile) throws (1:ApolloException e);

    //注册用户，提交用户信息
    i64 registerUserWithAllInfo(1:RegisterAllInfo registerAllInfo) throws (1:ApolloException e);

    //注册用户，提交用户信息，带推荐方式的
    i64 registerUserWithRecommend(1:UserProfile userProfile, 2:i64 recommenduid, 3:RecommendType recommendtype) throws (1:ApolloException e);

    // 注册商户 注册成功返回userid
    // params: json.dumps({})
    // mode: bigmchnt注册成为大商户 submchnt连锁商户 mchnt普通商户
    i64 user_signup(1:string params) throws (1:ApolloException e);
    
    
    //// 修改用户
    // 修改商户信息
    // userid: 商户userid
    // params: json.dumps({})
    i64 user_edit(1:i64 userid, 2:string params) throws (1:ApolloException e);

    // 修改密码接口
    i32 changePwd(1:i64 uid, 2:string password) throws (1:ApolloException e);

    // 设置用户状态
    i64 setUserState(1:i64 uid, 2:i64 state) throws (1:ApolloException e);
   
    // 修改用户银行信息
    i32 updateBankInfo(1:i64 uid, 2:BankInfo bankinfo) throws (1:ApolloException e);
    
    // 修改用户信息
    // 只允许修改: telephone, shopname, mcc, address, businessaddr, longitude,
    // latitude, groupid name, legalperson, licensenumber
    i32 updateUser(1:i64 uid, 2:User user) throws (1:ApolloException e);


    //// 验证密码接口
    // 验证密码
    // 检查用户密码接口 成功返回0， 不成功返回其他值
    i32 checkUser(1:string mobile, 2:string password) throws (1:ApolloException e);

    // 检查用户密码接口 成功返回商户userid， 不成功抛出相应错误
    i32 checkUsername(1:string username, 2:string password) throws (1:ApolloException e);
    
    // 检查用户密码接口 成功返回商户userid， 不成功抛出相应错误
    i32 checkByUid(1:i64 uid, 2:string password) throws (1:ApolloException e);
    
    
    //// 获取用户信息
    //获取用户基本信息接口，通过uid
    User findUserByid(1:i64 uid) throws (1:ApolloException e);

    //获取用户基本信息接口，通过shopname
    list<UserBrief> findUserByShopname(1:string shopname, 2:i64 groupid) throws (1:ApolloException e);


    //// 用户标签相关接口
    // 设置用户的标签
    i32 setUserTag(1:i64 uid, 2:UserTag usertag) throws (1:ApolloException e);
    
    // 获取用户的标签的备注
    map<i64, string> getUserTagContents(1:list<i64> uids, 2:string tagname) throws (1:ApolloException e);


    //获取用户基本信息接口，通过shopname
    /* spec json.dumps后的字符串
     * 字段示例：
     * 分页信息:
     * offset: i32,  偏移量，默认 0
     * limit: i32,  分页量，默认不分页（全取）
     * where (暂不支持or)
     * 仅支持uid, name, shopname, mobile, state, province, city, address, groupid
     * uid, groupid, email, username 必传其一
     * 
     * 例:
     * {"where": {"uid": 12}} 查询uid为12的商户
     * {"where": {"uid": ('in', (12, 13))}} 查询uid在(12, 13)的商户
     * {"where": {"groupid": ('in', (12, 13)), "shopname": ("like', "yyk%%")}} 
     * 查询在groupid 在 (12, 13), 且店铺名like yyk%的商户
     */ 
    list<UserBrief> findUserBriefs(1:string spec) throws (1:ApolloException e);

    // 获取用户基本信息接口，通过userid
    UserBrief findUserBriefById(1:i64 uid) throws (1:ApolloException e);

    // 获取用户基本信息接口，通过userid
    list<UserBrief> findUserBriefsByIds(1:list<i64> uids) throws (1:ApolloException e);
	
    //获取用户基本信息接口，通过mobile
    User findUserByMobile(1:string mobile) throws(1:ApolloException e);
    
    //获取用户信息接口，通过uid
    UserProfile findUserProfileByid(1:i64 uid) throws (1:ApolloException e);
    
    //获取指定条件的用户数目
    i32 findUserCount(1:UserQuery q) throws (1:ApolloException e);
    //获取指定条件的用户
    list<User> findUsers(1:UserQuery q) throws (1:ApolloException e);
    //获取指定条件的uid
    list<i64> findUserIds(1:UserQuery q) throws (1:ApolloException e);
    
    // 获取指定条件的userids
    // mode:service 根据服务获取userid列表
    // q: (当mode为service时)
    //   page: 页数, 默认0
    //   pagesize: 每页项数, 默认10
    //   service_code:服务code 
    //   status: 状态 
    //   orderby: 默认:orderby userid
    list<i64> findUserIdsEx(1:string q, 2:string mode) throws (1:ApolloException e);

    //获取用户的服务开通状态，state为0为失效，1为有效
    list<UserService> getUserServices(1:i64 uid, 2: i32 status);

    // 获取用户某服务状态
    i32 getUserServiceStatus(1:i64 uid, 2:string service_code);
    
    //批量获取用户的开通状态，不区分状态
    map<i64, list<UserService>> getAllUserServices(1:list<i64> uids);

    //开通或修改用户服务, 返回结果为map<code, errmsg> errmsg如果为空为成功
    map<string, string> setUserServices(1:i64 uid, 2: list<UserService> userServices) throws (1:ApolloException e);

    // 批量设置用户服务 0成功 1失败
    i32 setUsersService(1:list<i64> uids, 2: UserService userServices) throws (1:ApolloException e);

    //给用户分配角色, 返回结果为map<code, errmsg> errmsg如果为空为成功
    map<string, string> setUserCategory(1:i64 uid, 2: list<UserCate> userCategory) throws (1:ApolloException e);

    //批量给用户分配角色, 0成功 1失败
    i32 setUsersCategory(1:list<i64> uids, 2: list<UserCate> userCategory) throws (1:ApolloException e);

    //根据cate_code为标签设置信息,注意只对userid=1生效,只对映射关系生效
    i32 setCategoryByCode(1:string cate_code, 2: UserCate userCategory) throws (1:ApolloException e);

    // 获取用户角色
    // userid 商户id
    // spec 查询条件 json.dumps({'cate_code' : 'merchant'})
    list<UserCate> getUserCategory(1:i64 uid, 2:string spec) throws (1:ApolloException e);

    // 获取多位用户角色
    // userids 商户id
    // spec 查询条件 json.dumps({'cate_code' : 'merchant'})
    map<i64, list<UserCate>> getUsersCategory(1:list<i64> uids, 2:string spec) throws (1:ApolloException e);
    
    
    //// 关系相关操作
    // 获取user_relation的字典
    // userid->link_ids 
    // 若uids为空时, 查询出所有的关联表
    map<i64, list<i64>> getRelationDict(1:list<i64> uids, 2:string link_cate) throws (1:ApolloException e);
    
    // 商户关系 user_relation
    // 获取user_relation 中属于userid 下的link_id
    list<UserRelation> getUserRelation(1:i64 userid,2:string link_cate) throws (1:ApolloException e);

    // 获取user_relation 中属于link_id 下的userid
    list<UserRelation> getUserReverseRelation(1:i64 userid,2:string link_cate) throws (1:ApolloException e);

    // 获取传送的userids的商户对应字典
    // [{link_id->userid}]
    // 如果不传uids，这查出数据库所有的link_id对应的关系
    map<i64, i64> getReverseRelations(1:list<i64> uids, 2:string link_cate) throws(1:ApolloException e);

    // 设置userid的relation
    map<i64, string> setUserRelation(1:i64 userid,2:list<UserRelation> relations) throws (1:ApolloException e);

    // 解绑用户关系 成功将返回0
    // link_id为0时将解绑userid所有的关系, link_cate为空时将解绑userid和link_id所有的关系
    i32 unbindRelation(1:i64 userid, 2:i64 link_id, 3:string link_cate) throws (1:ApolloException e);


    //// 权限相关接口
    // 获取用户权限角色, group可选默认为空字符串用作筛选
    list<PermissionRole> getUserPermissionRole(1:i64 uid) throws (1:ApolloException e);

    // 获取用户权限, group可选默认为空字符串用作筛选
    list<Permission> getUserPermission(1:i64 uid) throws (1:ApolloException e);

    // 获取用户权限, 将会检查组的有效性
    list<Permission> get_user_permissions(1:i64 userid) throws (1:ApolloException e);

    //检查用户权限, code为权限code  group可选默认为空字符串用作筛选  0为有权限
    i32 checkUserPermission(1:i64 uid, 2:string code) throws (1:ApolloException e);

    // 添加新权限, 成功返回0   失败返回其他值
    i32 addPermission(1:Permission p) throws (1:ApolloException e);
    // 修改权限
    i32 editPermission(1:Permission p) throws (1:ApolloException e);

    //添加新权限组, 成功返回0   失败返回其他值
    i32 addPermissionRole(1:PermissionRole r) throws (1:ApolloException e);

    //修改权限组的属性 code字段暂时不可修改
    i32 edit_permission_role(1:PermissionRole r, 2:i32 status) throws (1: ApolloException e);

    //绑定权限到组, 只取其中的code,成功返回0   失败返回其他值
    i32 bindPermissionToRole(1:Permission p, 2:PermissionRole r) throws (1:ApolloException e);

    //重置角色的权限为指定的权限code,如果code不存在自动过滤
    i32 reset_permissions_of_role(1:string role_code, 2: list<string> perm_codes) throws (1: ApolloException e);

    //重置用户的角色为指定的角色code,如果code不存在自动过滤
    i32 reset_role_of_user(1:i32 userid, 2: list<string> role_codes) throws (1: ApolloException e);

    //解绑权限到组, 只取其中的code,成功返回0   失败返回其他值
    i32 unbindPermissionToRole(1:Permission p, 2:PermissionRole r) throws (1:ApolloException e);

    //绑定用户到组, 只取其中的code,成功返回0   失败返回其他值
    i32 bindUserToRole(1:i64 uid, 2:PermissionRole r) throws (1:ApolloException e);

    //解绑用户到组, 只取其中的code,成功返回0   失败返回其他值
    i32 unbindUserToRole(1:i64 uid, 2:PermissionRole r) throws (1:ApolloException e);


    // 获取用户简要信息
    list<UserBrief> findUserBriefsByName(1:string name, 2:i64 groupid) throws (1:ApolloException e);


    // 用户扩展信息相关接口
    // 获取用户扩展信息
    UserExt getUserExt(1:i64 uid) throws (1:ApolloException e); 
    // 获取用户扩展信息
    list <UserExt> getUserExts(1:list<i64> uids) throws (1:ApolloException e); 
    // 添加用户扩展信息
    // 如果不存在将插入
    i32 bindUserExt(1:UserExt user_ext) throws (1:ApolloException e);

    // 商户操作员相关接口
    // 添加opuser 添加成功返回opuid
    i64 addOpuser(1:Opuser opuser) throws (1:ApolloException e);
    // 修改opuser
    i32 changeOpuser(1:Opuser opuser) throws (1:ApolloException e);
    // 获取opuser
    // opuids为空list时, 返回所有的userid下的opuser
    // spec扩展的where (spec不加入status条件， 默认返回启用的)
    list<Opuser> getOpusers(1:i64 userid, 2:list<i64> opuid, 3:string spec) throws (1:ApolloException e);
    // 验证操作员密码
    i32 checkOpuserPwd(1:i64 userid, 2:i64 opuid, 3:string pwd) throws (1:ApolloException e);


    // 修改用户信息相关接口
    // 修改用户账号
    i32 changeUsername(1:i64 userid, 2:string new_username) throws (1:ApolloException e);

    // 获取商户支付appid
    // 返回值: json.dumps({appid : 'XXX'})
    string get_wx_pay_info(1:i64 userid) throws (1:ApolloException e);
}

