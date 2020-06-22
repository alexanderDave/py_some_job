import requests
import urllib
import MySQLdb
import pandas as pd
from lxml import etree

import mWeb.baseutils.mdao as mdao         			 #open in pro
import mWeb.baseutils.idbaHelper as idbaHelper         #open in pro

# import mheaders  									 #open in dev
# import mdao	   	 								 	 #open in dev
# import idbaHelper	   							 	 #open in dev

# 接口http://test31.stock.t.xianghuanji.com/admin/login/index
stock_login = "/admin/login/index" 								# POST stock31_test 后台登陆地址
stock_beforePick = '/admin/delivery/beforePick' 					# GET 查找待捡货状态的产品信息
stock_picking = "/admin/delivery/picking" 						# GET 根据id查看具体信息
stock_sign = "/admin/delivery/UpdateSignTimeAjax"  				# POST 签收订单
# 接口整理
stock_order = "/admin/order/" 				# 订单信息的首页
stock_skulist = '/admin/stock/index' 		# 库存明细的首页


# stock apis:
'''
api_url: http://test1.stock.t.xianghuanji.com/admin/order/
order_no:订单号
return：返回sku   
'''
def get_order(stockSession,order_no,testevn):
	dates = {'Filters[trade_no]':order_no,'Stock_page':'1','ajax':'yw0',}
	urls = "http://{0}.stock.t.xianghuanji.com".format(testevn)+stock_order+"/?"+urllib.parse.urlencode(dates)
	return getInfos(stockSession.get(urls).text,7)


'''
api_url:库存明细页面的接口
sku_name:需要查询的手机的sku
return：返回对应的sku的库存可用的列表      e.g.（货号，imei）
'''
def get_imei(stockSession,testevn,sku_name):
	mdata={'Stock[sku_name]':sku_name,'Stock[quantity]':'0','Stock[status]':'1','Stock_page':'1','ajax':'yw0',}
	urls = "http://{0}.stock.t.xianghuanji.com".format(testevn)+stock_skulist+"/?"+urllib.parse.urlencode(dates)
	return getInfos(stockSession.get(urls).text,1)

'''
api_url:库存明细页面的接口
sku_name:需要查询订单号
return：返回对应的订单状态      e.g.（用户，订单状态）
'''
def getOrderStatus(resqusets,api_url,tradeno):
	mdata = {'Trade[trade_no]': tradeno,'ajax': 'yw0','page': '1',}
	print('get_查询订单信息：',api_url+'/?'+urllib.parse.urlencode(mdata))
	# return resqusets.get(api_url+'/?'+urllib.parse.urlencode(mdata),headers = mheader).text
	return getInfos(resqusets.get(api_url+'/?'+urllib.parse.urlencode(mdata),headers = mheader).text,2)
	
'''捡货页面根据trade_no获取订单的id
return： str类型的id'''
def getBeforePick(resqusets,api_url,tradeno):
	mdata={'Delivery[trade_no]':tradeno,'Delivery_page':'1','ajax':'yw0',}
	print('get_查询订单的信息',api_url+'/?'+urllib.parse.urlencode(mdata))
	return getInfos(resqusets.get(api_url+'/?'+urllib.parse.urlencode(mdata),headers = mheader).text,3)
	
'''根据订单的id在捡货页面获取订单号的id'''
def getDetailInfo(resqusets,api_url,tradeno,sku_name):
	mid = getBeforePick(resqusets,base_url+test31_stock_beforePick,tradeno)
	m_sql = 'SELECT `id` FROM tbl_delivery_item WHERE id_delivery = '+mid+';'
	mdata={'id':mid,}
	tbl_id = str(mdao.exec_mysql_job('118.31.223.114',3306,'root','X1am9hVAnj1','airent_new_2017',m_sql)[0])
	print('get_查询捡货页面的详细信息',api_url+'/?'+urllib.parse.urlencode(mdata))
	fenqi_id = getInfos(resqusets.get(api_url+'/?'+urllib.parse.urlencode(mdata),headers = mheader).text,4)
	# 获取手机型号库存
	code = getImelCode(resqusets,base_url+test31_stock_skulist,sku_name)
	# 出库
	snd_date = {'DeliveryItem['+tbl_id+'][serial_number]':code[0][0],'DeliveryItem['+tbl_id+'][imei]':code[0][1],'Delivery[delivery_type]':'4',}
	print(snd_date)
	send = resqusets.post(api_url+'/?id_delivery='+mid,headers = mheader,data = snd_date)

	# 发货
	sendPhone(resqusets,api_url,mid)
	# 签收
	msignDate(resqusets,mid,'2019-01-01')
	return send.text
	
def sendPhone(resqusets,api_url,mid):
	snd_date={'Delivery[tracking_number]':'66668888','Delivery[delivery_type]':'1','Delivery[id_carrier]':'1',}
	print('post_',api_url+'/?'+urllib.parse.urlencode(snd_date))
	resqusets.post(api_url+'/?id_delivery='+mid,headers = mheader,data = snd_date)
	pass

'''http://test31.stock.t.xianghuanji.com/admin/delivery/UpdateSignTimeAjax post id=31335&dt_signed=2019-03-01'''
def msignDate(resqusets,sid,dates):
	snd_date={'id':sid,'dt_signed':dates,}
	print('post_',base_url+tes31t_stock_sign)
	resqusets.post(base_url+tes31t_stock_sign,headers = mheader,data = snd_date)
	pass


'''lxml解析html片段，获取对于sku的库存可用的list
resp_text：根据不同sku获取库存可用的sku的代码片段
'''
def getInfos(resp_text,mtype):
	# type(1:库存明细页面根据sku获取库存可用的imei&货号 2:3:)
	text = etree.HTML(resp_text)
	if mtype == 1:
		list_imei = text.xpath('//*[@class="odd"]/td[5]/text()')
		list_num = text.xpath('//*[@class="odd"]/td[3]/text()')
		print(list_num)
		print(list_imei)
		return getImeltup(list_imei,list_num)

	elif mtype == 2: # type(2:根据订单号获取订单当前的状态)
		name = text.xpath('//*[@id="yw0"]/table/tbody/tr/td[3]/text()')
		status = text.xpath('//*[@id="yw0"]/table/tbody/tr/td[2]/span[1]/text()')
		return {'user':name,'status':status}

	elif mtype == 3: # type(3:获取订单的id)
		trade_id = text.xpath('//*[@id="yw0"]/table/tbody/tr/td[1]/text()')
		if trade_id != []:
			return str(trade_id[0])
		else:
			print("Error:该订单不在待拣货页面列表中")

	elif mtype == 4:
		fenqi_id = text.xpath('//*[@id="content"]/div/div[4]/dl/dd[4]/code/a/text()')
		return str(fenqi_id[0][1:])
	else:

		return resp_text
	


'''将两个长度相等的list，按imei和货号组成元组，方便以后调用'''
def getImeltup(list1,list2):
	mlist = []
	if len(list2) != len(list1):
		assert Warning
	else:
		for x in range(0,len(list2)):
			mlist.append((list2[x],list1[x]))
	return mlist


'''根据之前取得的imei&货号，进行摘货
'''
def send_sku(resquset,tradeno):
	pass

'''输入运号，进行发货
'''
def send_phone(resquset,tradeno,nums,comp,type):


	pass

'''修改时间进行签收
'''
def sign_sku(resquset,tradeno,dtime):

	# uodate e_trade sign date
	msql='UPDATE e_trade SET dt_end_date = "'+dtime+'" WHERE trade_no = "'+tradeno+'";'
	print(msql)
	mdao.exec_mysql_job('47.110.141.101',3306,'root','X1am9hVAnj1','airent_new_2017',msql)
	pass




# 处理idba的数据
def getIdbaTrade(mtext):
	# print(mtext.text)
	resp_text = etree.HTML(mtext.text)
	# result = {}
	items = resp_text.xpath('//*[@id="simple-table"]')
	table = etree.tostring(items[0]).decode()
	# pandas读取table
	df = pd.read_html(table)[0]
	results = list(df.T.to_dict().values())
	# print(results)
	# values = resp_text.xpath('//*[@id="yw0"]/table/tbody/tr/td[1]/text()')
	# results = getImeltup(items,values)
	# for target_list in results:
	# 	result[target_list[0]]=target_list[1]

	return results



if __name__ == "__main__":
	
	print("code goes here:")
	# mcookies = input("请输入登录stock后的cookies：")
	
	# stock_login(XHJSession,base_url+test31_stock_login,'daiwei','000123')

	# 获取sku对应的库存信息 第一步
	# resp1 = getImelCode(XHJSession,base_url+test31_stock_skulist,sku_name)
	# print(resp1)
	# sign_sku(XHJSession,'TS20190221531077853585','2019-02-28 17:56:33')

	# # 第二步 根据trade_no获取当前订单状态
	# resp2 = getOrderStatus(XHJSession,base_url+test31_stock_order,'TS20181211132454007928')
	# print(resp2['status'])

	# # 第三步 根据trade_no获取订单的beforepick_status
	# resp3 = getBeforePick(XHJSession,base_url+test31_stock_beforePick,'TS20190125063095925970')
	# print(resp3)

	# 第四步 根据trade_no获取捡货页面的详细信息，存储订单id，执行小程序发货出库脚本
	# resp4 = getDetailInfo(XHJSession,base_url+tes31t_stock_picking,'TS20190125063095925970',sku_name)
	# print(resp4)

	# 第五步 发货

	# 第六步 签收

	# 第七步 生成12期还款计划

	# 第八步 修改订单到期时间




