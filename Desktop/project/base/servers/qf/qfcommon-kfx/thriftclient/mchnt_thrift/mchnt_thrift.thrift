namespace py mchnt_thrift

// 商品属性
struct GoodsAttr {
    1: optional i64    id;            
    2: optional string name;            
    4: optional list<string> attrs;
    5: optional i32    available;
}

// 商品规格
struct GoodsSpec {
    1: optional i64    id;            
    2: optional string spec;            
    3: optional i64    txamt;
    4: optional i64    origamt;
    5: optional i32    available;
    6: optional i64     total;  // 库存       
    7: optional i64     bought; // 已售数      
}

// 商品goods
struct Goods {
    1:  optional i64     id;            
    2:  optional i64     userid;            
    3:  optional string  name;            
    4:  optional i64     cate_id;
    5:  optional i32     type;     // 商品所属类型 1:点餐 2:抢购
    6:  optional i64     txamt;
    7:  optional i64     origamt;
    8:  optional i32     weight;       
    9:  optional string  descr;       
    10: optional string  info;       
    11: optional i32     txcurrcd;       
    12: optional list<string>  imgs;       
    13: optional i32    available; // 商品是否可用 0:不可用 1:可用
    14: optional list<GoodsAttr> attrs; // 规格            
    15: optional list<GoodsSpec> specs; // 属性     
    16: optional i64     total;  // 库存       
    17: optional i64     bought; // 已售数      
    18: optional list<string>  info_imgs; // 详细页图片列表       
    19: optional string  spec; // 规格描述
    20: optional string  cut_data; // 砍价数据(json.dumps cut_first_amt, cut_limit_amt, cut_total, cut_num, cut_per_num, cut_bought, cut_time)
}

// 推广活动
struct Promo {
    1:  optional i64 id;            
    2:  optional i64 userid;            
    3:  optional i64 unionid; // 商品unionid
    4:  optional i32 status;  // 活动状态 1:不启用 2:启用 3:删除
    5:  optional string start_time;  // 格式%Y-%m-%d %H:%M:%S, 不填默认当前时间
    6:  optional string expire_time; // 格式%Y-%m-%d %H:%M:%S
    7:  optional string create_time; // 格式%Y-%m-%d %H:%M:%S
    8:  optional i32 promo_state;  // 开奖状态 0:未开奖 1:已开奖
    9:  optional i32 type;  // 活动类型 1:抢购活动 2:特卖活动
    10: optional i32 stick; // 置顶状态 0:不置顶 1:置顶
    11: optional i32 buy_limit; // 限购数量 0:不限购 
    12: optional i64 use_userid; // 使用商户id
    13: optional string redeem_stime;  // 兑换开始时间
    14: optional string redeem_etime; // 兑换截止时间
    15: optional string ext; // ext 兑换说明,兑换限制 json.dumps
}

// 消费者地址
struct Addr {
    1:  optional i64 id;
    2:  optional i64 customer_id;
    3:  optional string location; // 底图定位地址
    4:  optional string detail_addr; // 详细门牌号
    5:  optional string mobile; // 联系电话
    6:  optional string contact_name; // 联系电话
    7:  optional double longitude; // 经度，double型
    8:  optional double latitude; // 纬度，double型
    9:  optional i64 weight; // 权重
    10: optional i32 is_default; // 是否是默认地址 0:不是 1:是
    11: optional i32 status;  // 删除状态 0:删除 1:正常
    12: optional i32 adcode;  // 地址编码
    13: optional string city_code;  // 城市区号
    14: optional string create_time; // 格式%Y-%m-%d %H:%M:%S
    15: optional string update_time; // 格式%Y-%m-%d %H:%M:%S
}

exception MTException {
    1: string respcd;   // 异常码
    2: string respmsg;  // 异常描述信息
}


service MchntThrift {

    // ping
    void ping();

    // 创建商品
    // 返回unionid
    i64 create_goods(1:Goods goods) throws (1:MTException e);
    // 修改商品 成功返回0
    // 暂不支持修改attrs, specs 
    i32 edit_goods(1:Goods goods) throws (1:MTException e);


    // 创建抢购活动
    i64 create_promo(1:Promo promo) throws (1:MTException e);
    // 修改抢购活动 成功返回0
    i32 edit_promo(1:Promo promo) throws (1:MTException e);


    // 创建地址
    i32 create_addr(1:Addr addr) throws (1:MTException e);
    // 修改地址
    i32 edit_addr(1:Addr addr) throws (1:MTException e);


    // 创建订单 成功返回订单相关信息
    // params = json.dumps({order_type....})
    // order_type: 订单类型
    // userid, customer_id: 消费者商户id
    // appid, openid: 微信appid和openid
    // goods_info: 商品信息
    // busicd: 支付busicd
    // addr_id:地址信息(抢购和外卖点单需要)
    // promo_id:抢购活动id(抢购点单需要)
    // goods_info: [{'id' : 123, 'attr_list' : [], 'cnt' : 10}]
    string create_order(1:string params) throws (1:MTException e);

    // 修改订单支付状态
    string add_order_pay(1:string params) throws (1:MTException e);

    // 修改订单信息
    // order_id必传
    // 允许修改 promo_state, chnl_sn, orig_chnl_sn, pay_ext
    string edit_order(1:string params) throws (1:MTException e);

    // 商户相关接口
    // params: json.dumps({'op_uid' 'type' 'data'})
    // op_uid: 操作员userid
    // content: 备注
    // type: 操作类型 signup:批量注册 edit:批量修改
    // data: 修改或者注册的数据
    i64 mchnt_batch_op(1:string params) throws (1:MTException e);
    
    // 商户注册
    i64 mchnt_signup(1:string params) throws (1:MTException e);

    // 商户修改
    i64 mchnt_edit(1:string params) throws (1:MTException e);
}
