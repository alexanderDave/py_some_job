import re
import pandas as pd
import json
from lxml import etree

def getidbaTable(idbSession,sql_etrade,db_chosen):
    print(sql_etrade,' -> the getidbaTable is runing this')
    query_url = 'http://idba.xianghuanji.com/sql/query'
    # sql_etrade for test
    # sql_etrade = "SELECT * FROM biz_withhold.e_withhold_request WHERE user_id =11421756 limit 100;"
    online_query = {
    'instance_id_chosen':'1',
    'db_chosen':db_chosen,
    'sql':sql_etrade,
    }
    info = idbSession.post(query_url,data=online_query)
    resp_text = etree.HTML(info.text)
	# 获取idba的查询结果的table
    items = resp_text.xpath('//*[@id="simple-table"]')
    # 增加对查询不到结果情况的判断
    tbody = resp_text.xpath('//*[@id="simple-table"]/tbody/tr')
    if ([]== tbody):
        return tbody
    
    table = etree.tostring(items[0]).decode()
    # print(table)
	# pandas读取table
    df = pd.read_html(table)[0]
    results = list(df.T.to_dict().values()) #返回的是一个dict的list；
    print(results,"getidbaTable_info  debug here")
    return results

def list2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['id_user']=str(mlist['id_user'])
    result['sum']=str(mlist['sum'])
    result['origin_contract_charge']=str(mlist['origin_contract_charge'])
    result['installments_sum']=str(mlist['installments_sum'])
    result['first_installment_price']=str(mlist['first_installment_price'])
    result['per_installment_price']=str(mlist['per_installment_price'])
    result['mp_service_id']=str(mlist['mp_service_id'])
    result['stock_origin_price']=str(mlist['stock_origin_price'])
    result['ahs_subsidies']=str(mlist['ahs_subsidies'])
    result['lbf_price']=str(mlist['lbf_price'])
    result['price_per_installments_without_lbf_price']=str(mlist['price_per_installments_without_lbf_price'])
    result['extra_price']=str(mlist['extra_price'])
    result['trade_no']=str(mlist['trade_no'])
    result['dt_updated']=str(mlist['dt_updated'])
    result['choose_installments_num']=str(mlist['choose_installments_num'])
    result['pre_installments_num']=str(mlist['pre_installments_num'])
    result['days_per_installments']=str(mlist['days_per_installments'])
    result['min_installments_num']=str(mlist['min_installments_num'])
    result['max_installments_num']=str(mlist['max_installments_num'])
    result['price_per_installments_all']=str(mlist['price_per_installments_all'])
    result['status']=str(mlist['status'])
    result['dt_created']=str(mlist['dt_created'])
    result['pay_end_time']=str(mlist['pay_end_time'])
    result['dt_take_effect']=str(mlist['dt_take_effect'])
    result['assurance_sum']=str(mlist['assurance_sum'])
    result['origin_assurance_charge']=str(mlist['origin_assurance_charge'])
    result['dt_service_start_date']=str(mlist['dt_service_start_date'])
    result['user_name']=str(mlist['user_name'])
    result['user_identi_card']=str(mlist['user_identi_card'])
    result['is_free']=str(mlist['is_free'])
    result['lbf_terms']=str(mlist['lbf_terms'])
    result['channel_id']=str(mlist['channel_id'])
    result['utm_source']=str(mlist['utm_source'])
    result['utm_medium']=str(mlist['utm_medium'])
    result['utm_campaign']=str(mlist['utm_campaign'])
    result['dt_return']=str(mlist['dt_return'])
    result['dt_signed']=str(mlist['dt_signed'])
    result['dt_end_date']=str(mlist['dt_end_date'])
    result['total_installments_number']=str(mlist['total_installments_number'])
    result['dt_service_end_date']=str(mlist['dt_service_end_date'])
    result['residual_value']=str(mlist['residual_value'])
    result['cash']=str(mlist['cash'])
    result['freeze_cash']=str(mlist['freeze_cash'])
    result['is_reduce']=str(mlist['is_reduce'])
    result['version']=str(mlist['version'])
    result['origin_first_month_amount']=str(mlist['origin_first_month_amount'])
    result['origin_per_month_amount']=str(mlist['origin_per_month_amount'])
    result['is_send_pay_success_mes']=str(mlist['is_send_pay_success_mes'])
    result['flag']=str(mlist['flag'])
    result['contract_no']=str(mlist['contract_no'])

    return result

    # biz_contract.e_contract_settlement
def settlemrnt2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['trade_no']=str(mlist['trade_no'])
    result['biz_no']=str(mlist['biz_no'])
    result['status']=str(mlist['status'])
    result['settlement_source']=str(mlist['settlement_source'])
    result['finished_time']=str(mlist['finished_time'])
    result['next_finished_time']=str(mlist['next_finished_time'])
    result['execute_num']=str(mlist['execute_num'])
    result['is_active']=str(mlist['is_active'])
    result['dt_created']=str(mlist['dt_created'])
    result['dt_updated']=str(mlist['dt_updated'])
    result['user_id']=str(mlist['user_id'])
    return result

# biz_contract.e_contract_settlement_item_sharding_
def sharding2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['trade_no']=str(mlist['trade_no'])
    result['biz_no']=str(mlist['biz_no'])
    result['bill_no']=str(mlist['bill_no'])
    result['settlement_category']=str(mlist['settlement_category'])
    result['amount']=str(mlist['amount'])
    result['step']=str(mlist['step'])
    result['status']=str(mlist['status'])
    result['execute_num']=str(mlist['execute_num'])
    result['is_active']=str(mlist['is_active'])
    result['dt_created']=str(mlist['dt_created'])
    result['dt_updated']=str(mlist['dt_updated'])
    result['freeze_no']=str(mlist['freeze_no'])

    return result

# service_settlement.e_settlement_payment
def payment2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['out_sn']=str(mlist['out_sn'])
    result['out_trade_no']=str(mlist['out_trade_no'])
    result['out_pay_no']=str(mlist['out_pay_no'])
    result['user_id']=str(mlist['user_id'])
    result['amount']=str(mlist['amount'])
    result['biz_no']=str(mlist['biz_no'])
    result['notify_url']=str(mlist['notify_url'])
    result['notify_status']=str(mlist['notify_status'])
    result['status']=str(mlist['status'])
    result['type']=str(mlist['type'])
    result['guarantee_sub_type']=str(mlist['guarantee_sub_type'])
    result['last_execute_time']=str(mlist['last_execute_time'])
    result['next_execute_time']=str(mlist['next_execute_time'])
    result['execute_num']=str(mlist['execute_num'])
    result['is_active']=str(mlist['is_active'])
    result['dt_created']=str(mlist['dt_created'])
    result['dt_updated']=str(mlist['dt_updated'])
    return result

# service_settlement.e_settlement_payment_item_sharding_
def paysharding2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['biz_no']=str(mlist['biz_no'])
    result['bill_no']=str(mlist['bill_no'])
    result['settlement_category']=str(mlist['settlement_category'])
    result['amount']=str(mlist['amount'])
    result['step']=str(mlist['step'])
    result['status']=str(mlist['status'])
    result['execute_num']=str(mlist['execute_num'])
    result['is_active']=str(mlist['is_active'])
    result['dt_created']=str(mlist['dt_created'])
    result['dt_updated']=str(mlist['dt_updated'])
    result['out_trade_no']=str(mlist['out_trade_no'])
    result['pay_no']=str(mlist['pay_no'])
    result['pay_time']=str(mlist['pay_time'])
    result['expire_time']=str(mlist['expire_time'])
    result['freeze_no']=str(mlist['freeze_no'])
    result['unfreeze_amount']=str(mlist['unfreeze_amount'])
    return result

# e_sub_trade
def subtrade2json(mlist):
    result = {}
    result['id']=str(mlist['id'])
    result['main_trade_no']=str(mlist['main_trade_no'])
    result['sub_trade_no']=str(mlist['sub_trade_no'])
    result['sub_trade_type']=str(mlist['sub_trade_type'])
    result['status']=str(mlist['status'])
    result['dt_created']=str(mlist['dt_created'])
    result['dt_updated']=str(mlist['dt_updated'])
    result['pay_code']=str(mlist['pay_code'])
    return result