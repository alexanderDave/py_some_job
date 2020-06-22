import mWeb.baseutils.mdao as mdao                          
import mWeb.baseutils.idbaHelper as idbaHelper       

import mWeb.baseutils.controller.apiController as apiController  
import mWeb.baseutils.controller.proInfoController as proInfoController      

import mWeb.baseutils.Utils.idbaUtils as idbaUtils
import mWeb.baseutils.DAO.TablesHelper as tablesHelper      #v2 获取表数据
import mWeb.ApiAutoTestUtils.common.dbUtil as dbUtil        #增加测试环境的db访问



# idba接口初始化
Helper = idbaHelper.Idbapi('daiwei','vStwuU9uYi84g6S=')
idbSession = Helper.getApi()


# 根据trade_no通过sql直接获取e_trade表中的数据，并以json的形式展示出来
def getTradeinfo_tradeno(tradeno):
    infos = mdao.getETradeBytrade_no(tradeno)
    return infos
# 根据contrade_no通过sql直接获取e_trade表中的数据，并以json的形式展示出来
def getTradeinfo_contradeno(contradeno):
    infos = mdao.getETradeBycontract_no(contradeno)
    return infos

# 通过sql直接获取biz_contract.e_contract_sharding_表中的数据，并以json的形式展示出来
def getBizcontractinfo(fb_num,contract_no):
    bizinfos = mdao.getBizcontract(fb_num,contract_no)
    return bizinfos

# 通过sql直接获取tbl_installment_pay_plan 12期还款计划表中的数据，并以json的形式展示出来
def getPayplaninfoTradeno(tradeno):
    payplaninfos = mdao.getPayplanBytrade_no(tradeno)
    return payplaninfos
def getPayplaninfoTradeid(tradeid):
    payplaninfos = mdao.getPayplanByid_trade(tradeid)
    return payplaninfos




# 判断e_trade表中订单的状态
def trade_status(statu):
    TradeType={1:"订单待支付",2:"订单超时关闭",3:"订单待发货（未跑拣货脚本）",4:"订单在拣货（已跑拣货脚本）",
    5:"订单已发货",7:"客服取消",8:"订单已退货",10:"订单已签收",15:"订单在退货中",26:"订单在还机中状态",27:"订单已买断",
    28:"订单还机成功",30:"已逾期",}
    if (statu in TradeType.keys()):
        return "{0}_code {1}".format(TradeType[statu],statu)
    else:
        return "订单状态为{0}".format(statu)


def getTradeinfo(tradeno,ttype):
    tradeInfo = {}
    if 1 == ttype:
        tradeInfo = getTradeinfo_tradeno(tradeno) #airent_2017.e_trade infos
        if ('err' in tradeInfo.keys()):
            print('get trade_info err here!')
            return tradeInfo
    elif 2 == ttype:
        tradeInfos = getTradeinfo_contradeno(tradeno) 
        # print(len(tradeInfos)) #-> 看是否换机单
        if 1 == len(tradeInfos):
            tradeInfo =tradeInfos[0]
        else:
            if ('err' in tradeInfos.keys()):
                return tradeInfos
            else:
                print('line3')
                tradeInfo =tradeInfos[0]
                tradeInfo['is_ChangePhone'] = True
                tradeInfo['info']="订单是还机单，contract_no对应多条记录，请用trde_no查询！"
    # print(tradeInfo)
    return tradeInfo

# --------------------------------- Mainpage apis -------------------------------
# 获取线上用户的token
def idba_user_token(uid):
    result = {}
    try:
        sql_etrade = "select * from xhj_user.e_user_token a where a.user_id ={0} and a.status=2 ORDER by a.id desc limit 1;".format(uid)
        proInfo = proInfoController.proHelper(idbSession,sql_etrade)
        result= proInfo.test()
    except Exception :
        return result
    
    return result

# TODO 根据trade_no来获取订单的信息,并将主要的信息以json形式回传；V2.0
def getTrade(tradeno):
    result = {}
    tabler = tablesHelper.Tables(tradeno)
    e_trade = tabler.get_e_trade()
    e_trade_extend = tabler.get_e_trade_extend()
    print(e_trade_extend)
    if e_trade:
        # e_trade 表信息
        result['用户id'] = e_trade['id_user']
        result['用户名'] = (e_trade['user_name']).encode('utf8').decode('utf8')
        result['身份证号'] = e_trade['user_identi_card']
        result['分表数'] = str(e_trade['id_user']%128)
        result['合约号'] = e_trade['contract_no']
        result['渠道号'] = e_trade['channel_id']
        # result['合约状态'] = e_trade['contract_no']
        result['订单状态'] = e_trade['status']
        result['总租金'] = str(e_trade['sum'])
        result['选择租期'] = e_trade['choose_installments_num']
        result['utmsource'] = str(e_trade['utm_source'])
        result['utmmedium'] = str(e_trade['utm_medium'])
        result['创建时间'] = str(e_trade['dt_created'])
        result['到期时间'] = str(e_trade['dt_end_date'])

        # e_trade_extend 表信息
        result['是否开启续租'] = bool(e_trade_extend['is_auto_rent'])
        result['是否买断'] = bool(e_trade_extend['is_buyout'])
        result['isreturnflow'] = bool(e_trade_extend['is_returnflow'])
        result['buyoutfee'] = str(e_trade_extend['buyout_fee'])
        result['滞纳金规则'] = str(e_trade_extend['late_rule'])

    return result

# 根据trade_no，从idba数据库里拿到数据表的信息，然后处理
def getProTradeinfo(trade_no, mtype,protype):
    results = {}
    if 1 == mtype:
        sql_etrade = "SELECT * FROM e_trade WHERE trade_no ='{0}' limit 1;".format(trade_no)
    elif 2 == mtype:
        sql_etrade = "SELECT * FROM e_trade WHERE contract_no ='{0}' limit 1;".format(trade_no)
    else:
        return {'err':'can\'t find this trade in idba '}
    # trade_info = idbaUtils.getidbaTable(idbSession,sql_etrade,'airent')
    proInfo = proInfoController.proHelper(idbSession,sql_etrade)
    if 1 == protype:
        # 还机
        results = proInfo.getReturnflow()
    elif 2 == protype:
        # 买断 20200201改版以后，小程序订单买断走下面的流程
        results = proInfo.getBuyout()
    elif 3 == protype:
        # 小程序老订单 20200210 newali -> 1;3只有存量未结算完成的订单
        results = proInfo.getSmallAli()
    else:
        return {'err':'tradeinfo.getProTradeinfo -> protype NOT EXISTS!'}
    

    return results

# 获取jira上的bug数量信息
def getJira():
    info = {}
    sql1 = 'select count(*) from jira.jiraissue;'
    sql2 = 'select count(*) from jira.jiraissue WHERE TO_DAYS( NOW() ) - TO_DAYS(CREATED) <= 1;'
    db = dbUtil.DB()
    db.connDb()
    info['jall'] = db.select_one(sql1)[0]
    info['jadd'] = db.select_one(sql2)[0]
    db.closeDb()
    info['gall'] = 500
    info['gadd'] = 10
    print(info)
    return info


# 快捷执行线上sql做测试参考
def test4sql():
    result = {}
    # sql_etrade = "SELECT a.trade_no FROM e_trade a LEFT JOIN e_trade_extend b on a.trade_no = b.trade_no WHERE  a.`status` =10 AND b.is_auto_rent = 1 AND a.dt_created >'2018-10-10'  LIMIT 10;"
    # bugout = "SELECT * FROM biz_contract.e_contract_settlement_item_sharding_{0} where biz_no = '{1}' limit 50;".format(trade_info[0]['id_user']%128,biz_no)
    sqls = "SELECT a.id,a.dt_signed,id_user%128,a.trade_no,`status`,b.fund_channel FROM e_trade a INNER JOIN e_trade_extend b on a.trade_no =b.trade_no where a.dt_signed >= '2020-04-02 10:04:29' limit 100;"

    # 分表执行查询
    # for x in range(1,129):
    #     sql_etrade = "SELECT * FROM biz_contract.e_contract_settlement_item_sharding_{0} WHERE biz_no ='201908220101227506332068' limit 10;".format(x)
    #     proInfo = proInfoController.proHelper(idbSession,sql_etrade)
    #     result[x]= proInfo.test()

    # sql_etrade = "SELECT * FROM e_trade WHERE channel_id ='52' limit 10;"
    proInfo = proInfoController.proHelper(idbSession,sqls)
    result= proInfo.test()
    print(result)
    return {}

# idba执行sql
# def idba_user_token(uid):
#     result = {}
#     sql_etrade = "select * from xhj_user.e_user_token a where a.user_id ={0} and a.status=2 ORDER by a.id desc limit 1;".format(uid)
#     proInfo = proInfoController.proHelper(idbSession,sql_etrade)
#     result= proInfo.test()

#     return result



# --------------------------------- 以下方法待废弃 -------------------------------------------






# 根据trade_no(ttype=1)||contract_no(ttype=2)来获取订单的信息
def getTradeStatus(tradeno,ttype):
    result = {}
    tradeInfo = getTradeinfo(tradeno,ttype)
    print(tradeInfo)
    if ('err' in tradeInfo.keys()):
        return {'reslut':'get trade_info err here!'}
    if {} != tradeInfo:
        order_stat = trade_status(tradeInfo['status'])
        result['order_status'] = order_stat
        result['status'] = tradeInfo['status']
        result['userid'] = tradeInfo['id_user']
        result['tradeid'] = tradeInfo['id']
        result['tradeno'] = tradeInfo['trade_no']
        result['fenbiao_num'] = tradeInfo['id_user']%128
        result['cont_no'] = tradeInfo['contract_no']
        # 获取bizinfo
        bizinfo = getBizcontractinfo(result['fenbiao_num'],result['cont_no'])  #biz_contract.e_contract_sharding_ infos  
        
    return result


if __name__ == "__main__":
    
    # Tradeinfo_tradeno = getTradeinfo_tradeno('20190703144344523890')
    # test = isChangePhone('4958147006431097')
    # test = getBizcontractinfo(100,4947651254399540128)
    # Tradestatus_tradeno = getTradeStatus(20190626155405496265,1)
    # test = getTradeStatus(20190604153703159594)
    getJira()


    

