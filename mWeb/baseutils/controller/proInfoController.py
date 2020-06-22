'''辅助判断线上买断还机订单所处的状态'''
import json
import mWeb.baseutils.Utils.idbaUtils as idbaUtils

# 买断明细里面的step代表的步骤名称说明
buyout_status={1:'支付宝代扣',2:'冻结转支付',3:'账户余额冻结',4:'释放冻结金额',
                5:'银联信用卡冻结转支付',6:'乐百分信用卡冻结转支付',7:'享换机用信额度释放',
                8:'银联行用卡额度释放',9:'乐百分信用卡额度释放',10:'用户主动支付',11:'小程序推结清'}

returnflow_status={1:'支付宝代扣',2:'冻结转支付',3:'账户余额冻结',4:'释放冻结金额',
                5:'主动支付',6:'释放用信'}

paymentStat={
    1:'结算中',2:'结算取消',3:'结算成功',4:'结算失败',0:'待结算'
}
# 线上信息判断
class proHelper(object):
    '''--todo--'''

    def __init__(self,idbaSession,sql_etrade):
        self.sql_etrade = sql_etrade
        self.idba = idbaSession

    # 买断的结算流程判断
    def getBuyout(self):
        # 获取主订单的订单信息
        result = {}
        trade_info = idbaUtils.getidbaTable(self.idba,self.sql_etrade,'airent')
        # 判断是否能获取主订单的订单信息，否则报错
        if ([] != trade_info):
            result['trade_info']=idbaUtils.list2json(trade_info[0])
            result['subTrade'] = self.getEsubtrade(trade_info[0]['trade_no'])
            if ((27 == trade_info[0]['status']) or (28 == trade_info[0]['status'])):
                msg = '已买断' if(27 == trade_info[0]['status']) else '已还机'
                result['status']=msg
                # return result
            # 增加对e_contract_settlement 有多个结算单的逻辑判断
            settlement = "SELECT * FROM biz_contract.e_contract_settlement WHERE trade_no = '{0}' limit 100; ".format(trade_info[0]['trade_no'])
            settlement_info = idbaUtils.getidbaTable(self.idba,settlement,'airent')
            settlement_item_info=[] # 防止为空 先占位
            biz_no = ''
            if ([] != settlement_info):
                if (1 < len(settlement_info)):
                    for infos in settlement_info:
                        if 1 == infos['is_active']:
                            biz_no = infos['biz_no']
                            result['settlement']=idbaUtils.settlemrnt2json(infos)
                else:
                    if 1 == settlement_info[0]['is_active']:
                        biz_no = settlement_info[0]['biz_no']
                        result['settlement']=idbaUtils.settlemrnt2json(settlement_info[0])
                if ('' == biz_no):
                    result['err']='e_contract_settlement,没有生成有效的买断结算单！'
                    return result
                
                settlement_item = "SELECT * FROM biz_contract.e_contract_settlement_item_sharding_{0} where biz_no = '{1}' limit 50;".format(trade_info[0]['id_user']%128,biz_no)
                settlement_item_info = idbaUtils.getidbaTable(self.idba,settlement_item,'airent')
                if ([] != settlement_item_info):
                    step = 1
                    result1={}
                    result2={}
                    for items in settlement_item_info:
                        msg=idbaUtils.sharding2json(items)
                        result1['sharding_{0}'.format(step)] = msg
                        step = step + 1
                    result['sharding']=result1
                    step1 = 1
                    for items in settlement_item_info:
                        msg='步骤:{0},类型:{6}，金额:{1}，执行次数:{2}，执行结果:{3}，创建时间:{4}，更新时间:{5}'.format(
                            items['step'],items['amount'],items['execute_num'],paymentStat[items['status']],items['dt_created'],items['dt_updated'],buyout_status[items['settlement_category']]
                        )
                        result2['step{0}'.format(step1)] = msg
                        step = step + 1
                    result['step']=result2
                else:
                    result['err']='e_contract_settlement_item_sharding_{0},没有生成买断结算步骤结算单！'.format(trade_info[0]['id_user']%128)
                    return result

            else:
                result['err']='e_contract_settlement,没有生成有效的买断结算单！'
                return result
            
        else:
            result['err'] = '买断订单查询信息失败，请查看sql！'
            result['debug'] = self.sql_etrade
        return result


    # 还机的结算流程判断
    def getReturnflow(self):
        # 获取主订单的订单信息
        result = {}
        trade_info = idbaUtils.getidbaTable(self.idba,self.sql_etrade,'airent')
        # 判断是否能获取主订单的订单信息，否则报错
        if ([] != trade_info):
            result['trade_info']=idbaUtils.list2json(trade_info[0])
            result['subTrade'] = self.getEsubtrade(trade_info[0]['trade_no'])
            if ((27 == trade_info[0]['status']) or (28 == trade_info[0]['status'])):
                msg = '已买断' if(27 == trade_info[0]['status']) else '已还机'
                result['status']=msg
                # return result
            # 增加对e_contract_settlement 有多个结算单的逻辑判断
            settlement = "SELECT * FROM service_settlement.e_settlement_payment WHERE out_trade_no = '{0}' limit 100; ".format(trade_info[0]['trade_no'])
            settlement_info = idbaUtils.getidbaTable(self.idba,settlement,'airent')
            settlement_item_info=[] # 防止为空 先占位
            biz_no = ''
            if ([] != settlement_info):
                if (1 < len(settlement_info)):
                    for infos in settlement_info:
                        if 1 == infos['is_active']:
                            biz_no = infos['biz_no']
                            result['settlement']=idbaUtils.payment2json(infos)
                else:
                    if 1 == settlement_info[0]['is_active']:
                        biz_no = settlement_info[0]['biz_no']
                        result['settlement']=idbaUtils.payment2json(settlement_info[0])
                if ('' == biz_no):
                    result['err']='e_contract_settlement,没有生成有效的还机结算单！'
                    return result
                
                settlement_item = "SELECT * FROM service_settlement.e_settlement_payment_item_sharding_{0} where biz_no = '{1}' limit 50;".format(trade_info[0]['id_user']%128,biz_no)
                settlement_item_info = idbaUtils.getidbaTable(self.idba,settlement_item,'airent')
                if ([] != settlement_item_info):
                    result1={}
                    result2={}
                    step = 1
                    for items in settlement_item_info:
                        msg=idbaUtils.paysharding2json(items)
                        result1['sharding_{0}'.format(step)] = msg
                        step = step + 1
                    result['sharding']=result1
                    step1 = 1
                    for items in settlement_item_info:
                        msg='步骤:{0},类型:{6}，金额:{1}，执行次数:{2}，执行结果:{3}，创建时间:{4}，更新时间:{5}'.format(
                            items['step'],items['amount'],items['execute_num'],paymentStat[items['status']],items['dt_created'],items['dt_updated'],returnflow_status[items['settlement_category']]
                        )
                        result['step{0}'.format(step1)] = msg
                        step = step + 1
                    result['step']=result2
                else:
                    result['err']='e_contract_settlement_item_sharding_{0},没有生成还机结算步骤结算单！'.format(trade_info[0]['id_user']%128)
                    return result

            else:
                result['err']='e_contract_settlement,没有生成有效的还机结算单！'
                return result
            
        else:
            result['err'] = '还机订单查询信息失败，请查看sql！'
            result['debug'] = self.sql_etrade
        return result


    # smallali 的结算流程
    def getSmallAli(self):
        # 获取小程序的订单信息
        result = {}
        trade_info = idbaUtils.getidbaTable(self.idba,self.sql_etrade,'airent')
        # 判断是否能获取小程序的订单信息，否则报错
        if ([] != trade_info):
            result['trade_info']=idbaUtils.list2json(trade_info[0])
            result['subTrade'] = self.getEsubtrade(trade_info[0]['trade_no'])
            if ((27 == trade_info[0]['status']) or (28 == trade_info[0]['status'])):
                msg = '已买断' if(27 == trade_info[0]['status']) else '已还机' 
                result['status']=msg
                # return result
            # 增加对e_contract_settlement 有多个结算单的逻辑判断
            settlement = "SELECT * FROM biz_contract.e_contract_settlement WHERE trade_no = '{0}' limit 100; ".format(trade_info[0]['trade_no'])
            settlement_info = idbaUtils.getidbaTable(self.idba,settlement,'airent')
            settlement_item_info=[] # 防止为空 先占位
            biz_no = ''
            if ([] != settlement_info):
                # print(len(settlement_info),'-----len/n')
                if (1 < len(settlement_info)):
                    for infos in settlement_info:
                        if 1 == infos['is_active']:
                            biz_no = infos['biz_no']
                            result['settlement']=idbaUtils.settlemrnt2json(infos)
                            # print(biz_no,'-> getSmallAli::biz_no')
                else:
                    if 1 == settlement_info[0]['is_active']:
                        biz_no = settlement_info[0]['biz_no']
                        result['settlement']=idbaUtils.settlemrnt2json(settlement_info[0])
                if ('' == biz_no):
                    result['err']='e_contract_settlement,没有生成有效的结算单！'
                    return result
                print(biz_no,'-> getSmallAli::biz_no')
                settlement_item = "SELECT * FROM biz_contract.e_contract_settlement_item_sharding_{0} where biz_no = {1} limit 50;".format(trade_info[0]['id_user']%128,biz_no)
                settlement_item_info = idbaUtils.getidbaTable(self.idba,settlement_item,'airent')
                if ([] != settlement_item_info):
                    # print(settlement_item_info)
                    step = 1
                    result1={}
                    result2={}
                    for items in settlement_item_info:
                        msg=idbaUtils.sharding2json(items)
                        result1['sharding_{0}'.format(step)] = msg
                        step = step + 1
                    result['sharding']=result1
                    step1 = 1
                    for items in settlement_item_info:
                        msg='步骤:{0},类型:{6}，金额:{1}，执行次数:{2}次，执行结果:{3}，创建时间:{4}，更新时间:{5}'.format(
                            items['step'],items['amount'],items['execute_num'],paymentStat[items['status']],items['dt_created'],items['dt_updated'],items['settlement_category']
                        )
                        result2['step{0}'.format(step1)] = msg
                        step = step + 1
                    result['step']=result2
                else:
                    result['err']='e_contract_settlement_item_sharding_{0},没有生成结算步骤结算单！'.format(trade_info[0]['id_user']%128)
                    return result
            else:
                result['err']='e_contract_settlement,没有生成有效的结算单！'
                return result
            
        else:
            result['err'] = '小程序订单信息查询失败，请查看sql！'
            result['debug'] = self.sql_etrade
        return result

    # 获取还机单
    def getEsubtrade(self,trade_no):
        # result = {}
        step = {}
        msql = "SELECT * FROM e_sub_trade WHERE main_trade_no = '{0}' limit 100;".format(trade_no)
        esubtrade = idbaUtils.getidbaTable(self.idba,msql,'airent')
        if ([]!= esubtrade):
            n=0
            for trade in esubtrade:
                step['{0}'.format(n)]=idbaUtils.subtrade2json(trade)
                n = n+1
            # result['subTrade'] = step
            return step
        else:
            step['err'] = 's_sub_trade not exists'
        
        return step
    
    def test(self):
        trade_info = idbaUtils.getidbaTable(self.idba,self.sql_etrade,'airent')
        return trade_info