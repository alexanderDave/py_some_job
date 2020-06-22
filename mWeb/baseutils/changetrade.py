import mWeb.baseutils.mdao as mdao                #open in pro
import mWeb.baseutils.tradeinfo as tradeinfo      #open in pro
import mWeb.baseutils.controller.apiController as apiController
import mWeb.baseutils.idbaHelper               as idbaHelper




# 修改订单的状态到指定状态 V2仍在使用中
def ChageStatu(trade_no,aim_no):
    infos = tradeinfo.getTradeStatus(trade_no,1)
    print(infos)
    if(not 'err' in infos.keys()):
        # 修改e_trade表中的status
        msql1 = "UPDATE e_trade SET `status`={0} WHERE trade_no='{1}';".format(aim_no,infos['tradeno'])
        print(msql1)
        mdao.updateSql('airent_new_2017',msql1)
        # 修改biz_contract.e_contract_sharding_93的status=2,order_tag=10 根据contract_no来查
        sta = 6 if (aim_no != 10) else 2
        if 26 == aim_no:
            sta = 3
        msql2 = "UPDATE e_contract_sharding_{0} SET `status`={1}, order_tag={2} WHERE contract_no='{3}';".format(infos['fenbiao_num'],sta,aim_no,infos['cont_no'])
        print(msql2)
        mdao.updateSql('biz_contract',msql2)
        # 修改xhj_trade.e_trade_sharding_1 的status=10
        num = 2 if(infos['userid']%2 == 0) else 1
        msql3 = "UPDATE e_trade_sharding_{0} SET `status`={1} WHERE trade_no='{2}';".format(num,aim_no,infos['tradeno'])
        print(msql3)
        mdao.updateSql('xhj_trade',msql3)
        return "db status changed successfuly"
    else :
        # print('trade_no or trade_type err!')
        infos['ChageToRent']='trade_no or trade_type err!'
        return infos

# 5:修订资金方 6:修改担保方 7:自动续租
def changeChannel(trade_no,tp,aim_no):
    infos = tradeinfo.getTradeStatus(trade_no,1)
    num = 2 if(infos['userid']%2 == 0) else 1
    tb_name = ['fund_channel','trade_risk_channel','is_auto_rent']
    if(not 'err' in infos.keys()):
        # 修改e_trade_extend的字段
        msql1 = "UPDATE e_trade_extend SET `{2}`={0} WHERE trade_no='{1}';".format(aim_no,infos['tradeno'],tb_name[tp-5])
        print(msql1)
        mdao.updateSql('airent_new_2017',msql1)
        # 修改分表xhj_trade.e_trade_extend_sharding_ 的字段
        msql2 = "UPDATE e_trade_extend_sharding_{2} SET `{3}`={0} WHERE trade_no='{1}';".format(aim_no,infos['tradeno'],num,tb_name[tp-5])
        print(msql2)
        mdao.updateSql('xhj_trade',msql2)
        return "db status changed successfuly"
    else:
        # print('trade_no or trade_type err!')
        infos['ChageToRent']='trade_no or trade_type err!'
        return infos

# 修改订单的到期时间 dt_end_date
def changeTime(trade_no,types,changetime):
    infos = tradeinfo.getTradeStatus(trade_no,1)
    num = 2 if(infos['userid']%2 == 0) else 1
    dt_name = ['dt_created','dt_signed','dt_end_date']
    tag = int(types)-2
    print(infos)
    if(not 'err' in infos.keys()):
        # 修改e_trade表中的status
        msql1 = "UPDATE e_trade SET `{2}`='{0}' WHERE trade_no='{1}';".format(changetime,trade_no,dt_name[tag])
        print(msql1)
        mdao.updateSql('airent_new_2017',msql1)
        msql2 = "UPDATE e_trade_sharding_{0} SET `{1}`='{2}' WHERE trade_no='{3}';".format(num,dt_name[tag],changetime,trade_no)
        print(msql2)
        mdao.updateSql('xhj_trade',msql2)
        return "db status changed successfuly"
    else:
        # print('trade_no or trade_type err!')
        infos['ChageToRent']='trade_no or trade_type err!'
        return infos

# 单表修改集合
def changeTable(tradeno,tp):
    if (8 == tp):
        msql1 = "UPDATE e_fund_jnnh_order_register SET `register_no`='2019122326152727678760140802511' WHERE order_no='{0}';".format(tradeno)
        print(msql1)
        mdao.updateSql('service_funding',msql1)
        return "db status changed successfuly"
    else:
        return 'changeTable failed!'



if __name__ == "__main__":
    a = ChageStatu('20190412152102985283',8)
    # seq = "UPDATE e_trade SET `status`=10 WHERE trade_no='20190708144255105902';"
    # a = mdao.updateSql('service_funding',seq)
    print(a)