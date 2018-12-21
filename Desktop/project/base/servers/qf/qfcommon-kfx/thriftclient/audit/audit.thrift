namespace py audit

exception AuditException {
    1: string respcd;  //异常码
    2: string respmsg; //异常描述信息
}

//用户基本信息
struct Audit {
    1: required string audit_type;  // 审核类型
    2: required i64 userid = 0;   // 审核商户的userid
    3: required i64 groupid = 0;  // 审核商户的渠道id
    4: required string info;      // 审核信息
}



//App公众信息
struct AppInfo{
    1:  required string	        appid;        // app唯一id
    2:  required list<string>   jsapipath;  // 支付目录
    3:  required string         pay_appid = "";     // 支付appid
    4:  required i64         uid;     // 商户uid
    5:  required string      cid;     // 渠道id
    6:  required i64         state; //0:关注商户自有,1:关注钱方,2:关注商户所在的渠道
}



service AuditServer {
    i16 ping() throws (1:AuditException e);
    
    // 添加任务
    i16 add_audit(1:Audit audit) throws (1:AuditException e);

    //审核通过|失败|拒绝接口
    i32 audit_api(1:string id, 2:string type , 3:string modify) throws (1:AuditException e);

    map<i64,AppInfo> app_api(1:list<i64> uid_list,2:i64 chnlcode) throws (1:AuditException e);


    // 更新签约宝活动接口
    i32 update_sales(1:i32 userid,2:i32 type,3:string name,4:string licensenumber,5:string licensephoto,6:string checkstand,7:string checkin,8:i32 sls_uid,9:string nickname,10:i32 usertype,11:string shopphoto) throws (1:AuditException e);

    // 更新签约宝活动接口
    // userid: 商户userid
    // type: 1:微信绿洲  2：支付宝蓝海
    // usertype: 商户类型 1:小微 2:个体 3:企业
    // name: 签约实体
    // licensenumber: 营业执照标号
    // nickname: 店铺名
    // licensephoto, checkstand, checkin, shopphoto, goodsphoto 凭证图片
    i32 update_sales_actv(1:i64 userid, 2:string params) throws (1:AuditException e);
}
