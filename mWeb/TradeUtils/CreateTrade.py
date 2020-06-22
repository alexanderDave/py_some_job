# -*- coding: UTF-8 -*- 

import requests
import time
# import redis
import http.cookiejar as cookielib
from mWeb.TradeUtils.UserLogin import UserHelper

class Trade(object):

	def __init__(self,testevn,phone):
		self.phone = phone
		self.evn = testevn
		self.token_dict = UserHelper(phone,testevn).login()
		self.create_hd = {
			'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
			'cookies': 'utm_source=huabei; utm_source=huabei; utm_medium=huabei; utm_campaign=huabei; channelId=9; user_id_v2={0}; userToken={0}; track_user_id={1}'.format(self.token_dict['user_id_v2'],self.token_dict['track_user_id']),
			'user_id_v2': self.token_dict['user_id_v2'],
			'userToken': self.token_dict['user_id_v2'],
			'utmCampaign': 'huabei',
			'utmMedium': 'huabei',
			'platform': 'h5_browser',
			'utmCampaign': 'huabei',
			'channelId': '9',
			'Connection': 'keep-alive',
			'Referer': 'http://{0}.mm.t.xianghuanji.com/mytrade/order/confirm?contract_product_id=1337'.format(testevn),
		}

	# step1
	def createApplyNo(self):
		base_url = 'http://{0}.mm.t.xianghuanji.com/node-api/trade/order/confirm/createApplyNo'.format(self.evn)
		dates={'contract_product_id':1337,'coupon_ids':'','user_coupon_nums':'','delivery_type':1}
		createApplyNo = requests.post(base_url,data=dates, headers=self.create_hd)
		# {"status":200,"data":{"apply_no":"A202005271513340190654864","interval_time":3,"is_show_alter":false,"is_validate_coupon":true,"validate_msg":""}}
		print('=====createApplyNo=======>', createApplyNo.text)
		result = createApplyNo.json()
		apply_no = result['data']['apply_no']
		return apply_no

	# step2
	def confirmceateTrade(self, apply_no):
		base_url = 'http://{0}.mm.t.xianghuanji.com/node-api/trade/order/confirm/ceateTrade'.format(self.evn)
		dates = {'apply_no': apply_no}
		confirmceateTrade = requests.post(base_url,data=dates, headers=self.create_hd)
		#{"status":200,"data":{"apply_no":"A202005271513340190654864","order_no":"20200527151334513055","contract_no":"4958379103153474","interval_time":3,"is_show_alter":false,"stop_tag":false}}
		print('=====confirmceateTrade=======>',confirmceateTrade.text)
		result = confirmceateTrade.json()
		info = {
			'apply_no':result['data']['apply_no'],'order_no':result['data']['order_no'],'contract_no':result['data']['contract_no'],
		}

		return info

	# step3,有两步？？看后面能不能简化
	def createStrategyPay(self,infos):
		base_url = 'http://{0}.mm.t.xianghuanji.com/node-api-v2/bfa/order/createStrategyPay'.format(self.evn)
		self.create_hd['Referer'] = 'http://{0}.mm.t.xianghuanji.com/mytrade/v2/order/pay?order_no={0}&contract_no={1}'.format(infos['order_no'],infos['contract_no'])
		dates = {'order_no': infos['order_no'],'pis_code':'pis69','is_short':0,'pay_no':'',
				 'return_url':'http://{0}.mm.t.xianghuanji.com/mytrade/v2/order/pay?order_no={1}&pay_no=&pis_code=pis69&is_short=0'.format(self.evn,infos['order_no']),}
		# 1 needs timestamp.
		createStrategyPay1 = requests.post(base_url, data=dates, headers=self.create_hd)

		# 2
		createStrategyPay2 = requests.post(base_url, data=dates, headers=self.create_hd)
		print('=====createStrategyPay1=======>', createStrategyPay1.text)
		print('=====createStrategyPay2=======>', createStrategyPay2.text)

		pass

	# step4
	def route_handle(self, apply_no):
		base_url = 'http://{0}.mm.t.xianghuanji.com/node-api-v2/bfa/cup/route/handle'.format(self.evn)
		dates = {'apply_no': apply_no}
		confirmceateTrade = requests.post(base_url, data=dates, headers=self.create_hd)
		# {"status":200,"data":{"apply_no":"A202005271513340190654864","order_no":"20200527151334513055","contract_no":"4958379103153474","interval_time":3,"is_show_alter":false,"stop_tag":false}}
		print('=====confirmceateTrade=======>', confirmceateTrade.text)
		result = confirmceateTrade.json()
		info = {
			'apply_no': result['data']['apply_no'], 'order_no': result['data']['order_no'],
			'contract_no': result['data']['contract_no'],
		}

		return info

	def getSmscode(self):
		code = input('__sms code here__:')
		base_url = 'http://{0}.mm.t.xianghuanji.com/node-api-v2/bfa/cup/route/handle'.format(self.evn)


		pass

	def CreateTrade(self):
		# 第1步 createApplyNo
		apply_no = self.createApplyNo()
		# 第2步 confirmceateTrade
		trade_info = self.confirmceateTrade(apply_no)
		# 第3步 confirmceateTrade
		self.createStrategyPay(trade_info)


		pass


if __name__ == "__main__":
	print('开始登陆享换机')
	trade = Trade('test2','18616371234')
	trade.CreateTrade()
