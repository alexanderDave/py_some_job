import MySQLdb

# test_sql
sql_getTradeInfo = "SELECT * FROM e_trade WHERE trade_no = 'TS20190521445609878818';"
sql_latest_trade = "SELECT * FROM e_trade WHERE user_name='戴伟' ORDER BY dt_created DESC LIMIT 1 ;"
sql_getsubTradeInfo = "SELECT * FROM e_sub_trade WHERE main_trade_no = 'TS20190523807126645961_1';"

def exec_mysql_job(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchone()
	cur.close()
	con.commit()
	con.close()
	return result

# 从etrade表里获取一条记录
def exec_etrade_job1(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchone()
	if result:
		infos = {
		'id':result[0],'id_user':result[1],'sum':result[2],'origin_contract_charge':result[3],
		'installments_sum':result[4],'first_installment_price':result[4],'per_installment_price':result[6],'mp_service_id':result[7],
		'stock_origin_price':result[8],'ahs_subsidies':result[9],'lbf_price':result[10],'price_per_installments_without_lbf_price':result[11],
		'extra_price':result[12],'trade_no':result[13],'dt_updated':result[14],'choose_installments_num':result[15],
		'pre_installments_num':result[16],'days_per_installments':result[17],'min_installments_num':result[18],'max_installments_num':result[19],
		'price_per_installments_all':result[20],'status':result[21],'dt_created':result[22],'pay_end_time':result[23],'dt_take_effect':result[24],'assurance_sum':result[25],
		'origin_assurance_charge':result[26],'dt_service_start_date':result[27],'user_name':result[28],'user_identi_card':result[29],'is_free':result[30],'lbf_terms':result[31],
		'channel_id':result[32],'utm_source':result[33],'utm_medium':result[34],'utm_campaign':result[35],'dt_return':result[36],'dt_signed':result[37],
		'dt_end_date':result[38],'total_installments_number':result[39],'dt_service_end_date':result[40],'residual_value':result[41],'cash':result[42],'freeze_cash':result[43],
		'is_reduce':result[44],'version':result[45],'origin_first_month_amount':result[46],'origin_per_month_amount':result[47],'is_send_pay_success_mes':result[48],'flag':result[49],'contract_no':result[50],
		}
	else:
		infos = {'err':'no result,check sql','result':result}
	# print(infos)
	cur.close()
	con.commit()
	con.close()
	return infos

# 从etrade表里获取所有的记录
def exec_etrade_job2(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchall()
	infos = {}
	if result != ():
		num = 0
		for info in result:
			infos[num] = {
			'id':info[0],'id_user':info[1],'sum':info[2],'origin_contract_charge':info[3],
			'installments_sum':info[4],'first_installment_price':info[4],'per_installment_price':info[6],'mp_service_id':info[7],
			'stock_origin_price':info[8],'ahs_subsidies':info[9],'lbf_price':info[10],'price_per_installments_without_lbf_price':info[11],
			'extra_price':info[12],'trade_no':info[13],'dt_updated':info[14],'choose_installments_num':info[15],
			'pre_installments_num':info[16],'days_per_installments':info[17],'min_installments_num':info[18],'max_installments_num':info[19],
			'price_per_installments_all':info[20],'status':info[21],'dt_created':info[22],'pay_end_time':info[23],'dt_take_effect':info[24],'assurance_sum':info[25],
			'origin_assurance_charge':info[26],'dt_service_start_date':info[27],'user_name':info[28],'user_identi_card':info[29],'is_free':info[30],'lbf_terms':info[31],
			'channel_id':info[32],'utm_source':info[33],'utm_medium':info[34],'utm_campaign':info[35],'dt_return':info[36],'dt_signed':info[37],
			'dt_end_date':info[38],'total_installments_number':info[39],'dt_service_end_date':info[40],'residual_value':info[41],'cash':info[42],'freeze_cash':info[43],
			'is_reduce':info[44],'version':info[45],'origin_first_month_amount':info[46],'origin_per_month_amount':info[47],'is_send_pay_success_mes':info[48],'flag':info[49],'contract_no':info[50],
			}
			num+=1
	else:
		infos = {'err':'no result,check sql','result':result}
	# print(infos)
	cur.close()
	con.commit()
	con.close()
	return infos

def exec_esubtrade_job1(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchall()
	infos={}
	if result != ():
		num = 0
		for info in result:
			infos[num] = {
				'id':info[0],'main_trade_no':info[1],'sub_trade_no':info[2],'sub_trade_type':info[3],
				'status':info[4],'dt_created':info[5],'dt_updated':info[6],'pay_code':info[7],
			}
			num+=1
	else:
		infos = {'err':'no result,check sql','result':result}
	cur.close()
	con.commit()
	con.close()
	return infos

# 订单的
def exec_bizcontract_job1(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchall()
	infos={}
	if result != ():
		num = 0
		for info in result:
			infos[num] = {
				'id':info[0],'user_id':info[1],'contract_no':info[2],'status':info[3],
				'order_tag':info[4],'returnflow_tag':info[5],'buyout_tag':info[6],'change_tag':info[7],
				'dt_created':info[8],'dt_updated':info[9],'contract_type':info[10],'settlement_tag':info[11],
				'payplan_tag':info[12],'after_sale_tag':info[13],'channel_id':info[14],'cancel_tag':info[15],
				'service_type':info[16],
			}
			num+=1
	else:
		infos = {'err':'no result,check sql','result':result}
	cur.close()
	con.commit()
	con.close()
	return infos

#  搜索12期还款计划
def exec_payplan_job1(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	cur.execute(msql)
	result = cur.fetchall()
	infos={}
	if result != ():
		num = 0
		for info in result:
			infos[num] = {
				'Id':info[0],'id_trade':info[1],'amount':info[2],'pay_plan_type':info[3],'installment':info[4],'start_time':info[5],
				'end_time':info[6],'is_finished':info[7],'finished_time':info[8],'dt_created':info[9],'channel_code':info[10],'already_pay_amount':info[11],'left_pay_amount':info[12],'guarantee_amount':info[13],'has_execute':info[14],'repayment_type':info[15],'has_recover':info[16],'withhold_code':info[17],'clock_time':info[18],'source_from':info[19],'is_delete':info[20],'trade_no':info[21],'auth_no':info[22],'agreement_no':info[23],'user_name':info[24],'user_phone':info[25],'unfreeze_amount':info[26],'origin_price':info[27],'subject':info[28],'has_push_zhima':info[29],'pay_no':info[30],'user_id':info[31],'debit_date':info[32],'is_overdue':info[33],'is_transfer':info[34],'has_push_ward':info[35],'error_reason':info[36],
				'execute_total_num':info[37],'execute_current_num':info[38],'has_call':info[39],'execute_time':info[40],'is_release':info[41],'monthly_credit_limit':info[42],'dt_updated':info[43],'debt_collect_employee_id':info[44],'debt_collect_update_dt':info[45],'is_returnflow':info[46],'is_executing':info[47],'executing_pay_no':info[48],'executing_expired_time':info[49],
				}
			num+=1
	else:
		infos = {'err':'no result,check sql','result':result}
	cur.close()
	con.commit()
	con.close()
	return infos


# def close_mysql_cursor(cur):
# 	cur.close()
# 	con.commit()
# 	con.close()
# 邮寄还机接口
def funcname(parameter_list):
	pass


def update_job(mhost,mport,muser,mpasswd,mdbname,msql):
	con = MySQLdb.connect(host=mhost,port=mport,user=muser,passwd=mpasswd,db=mdbname)
	cur = con.cursor()
	result = 0
	try:
		cur.execute(msql) # 执行sql语句
		result = cur.rowcount
		con.commit() # 提交到数据库
	except:
		con.rollback() # 发生错误的时候回滚
	con.close()
	return result

# 对e_trade表进行操作
def getETradeBytrade_no(trade_no):
	sqls = "SELECT * FROM e_trade WHERE trade_no ='{0}';".format(trade_no)
	# print("getETrade trade_no is {0}".format(trade_no))
	# print("getETrade runs sql like {0}".format(sqls))
	return exec_etrade_job1('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sqls)

def getETradeBycontract_no(trade_no):
	sqls = "SELECT * FROM e_trade WHERE contract_no ='{0}';".format(trade_no)
	# print("getETrade2 trade_no is {0}".format(trade_no))
	# print("getETrade2 runs sql like {0}".format(sqls))
	return exec_etrade_job2('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sqls)

# 对tbl_installment_pay_plan表进行操作
def getPayplanBytrade_no(trade_no):
	sqls = "SELECT * FROM tbl_installment_pay_plan WHERE trade_no ='"+(str(trade_no)).strip()+"';"
	return exec_payplan_job1('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sqls)
def getPayplanByid_trade(id_trade):
	sqls = "SELECT * FROM tbl_installment_pay_plan WHERE id_trade ='"+(str(id_trade)).strip()+"';"
	return exec_payplan_job1('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sqls)

# 对e_sub_trade表进行操作
def getEsubTrade(trade_no):
	sqls = "SELECT * FROM e_sub_trade WHERE trade_no ='"+(str(trade_no)).strip()+"';"
	return exec_esubtrade_job1('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sqls)

# biz_contract.e_contract_sharding_表进行操作
def getBizcontract(modnum,contract_no):
	sqls = "SELECT * FROM e_contract_sharding_"+(str(modnum)).strip()+" WHERE contract_no ='"+(str(contract_no)).strip()+"';"
	return exec_bizcontract_job1('118.31.223.114',3306,'root','X1am9hVAnj1','biz_contract',sqls)

def updateSql(dbname,msql):
	return update_job('118.31.223.114',3306,'root','X1am9hVAnj1',dbname,msql)


if __name__ == "__main__":
	# sqlquery = "SELECT `id` FROM tbl_delivery_item WHERE id_delivery = '31335';"
	# result = exec_esubtrade_job1('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',sql_getsubTradeInfo)
	result = getJiraAll()
	print(result)