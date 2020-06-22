# -*- coding: UTF-8 -*- 
# 模拟用户登陆的类

import time,json
import requests
import http.cookiejar as cookielib

from mWeb.baseutils.DAO import RedisHelper

class UserHelper(object):
    
    def __init__(self,phone_nu,test_env):
        self.evnnu = test_env
        self.session = None
        self.phone_nu = phone_nu
        self.evn = "http://{0}.mm.t.xianghuanji.com".format(test_env)
        self.hd = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
            'Referer':'{0}/account/login?redirect=%2Faccount%2Fcenter'.format(self.evn),
            'X-Requested-With': 'XMLHttpRequest',
            'Host': '{0}.mm.t.xianghuanji.com'.format(test_env),
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 下方配置是测试登陆IP限制的时候开启
            # 'Remote Address':'{0}.mm.t.xianghuanji.com/10.10.10.11:80',
            # 'X-Forwarded-For': '10.10.10.11', 
        }

    def getIp(self,msession):
        #     http://test2.mm.t.xianghuanji.com/node-api/login/getIP
        base_url = '{0}/node-api/login/getIP'.format(self.evn)
        resp = msession.get(base_url,headers=self.hd)

        print(resp.text)


    # 从redis获取登陆时候的图形验证码
    def getImageCode(self,msession):
        mtimestamp = str(int(time.time() * 1000))
        rediskey = 'JAF:bfa:image-code-{0}-mobile_login'.format(self.phone_nu)
        mredis = RedisHelper.Redis()
        mredis.connDb()
        codes = mredis.getKey(rediskey)
        code = codes.decode('utf8')
        print('从redis获取登陆::{0}时候的图形验证码::{1}'.format(rediskey,code))
        postdate = {
            'phone': self.phone_nu, 'type': 'mobile_login', 'captcha_code': code,'timestamp':mtimestamp,
            'fp': 'f08dd59eecab5ad1fe9388f34d9516ca', 'fp_hash': 'a5da6d77b8a05ca6834f33622278ff14',
        }
        return self.sendSms(msession,postdate)
        # phone=19616376958&type=mobile_login&captcha_code=8176&timestamp=1590481548766&fp=f08dd59eecab5ad1fe9388f34d9516ca&fp_hash=26f051b0daf511cc7c7b6babdf4d02ba

    # 获取登陆时候的短信验证码
    def sendSms(self,msession,dates):
        print('----------开始请求验证码----------')
        base_url = '{0}/node-api/login/sendSMS'.format(self.evn)
        print('获取登陆时候的短信验证码,',base_url)
        resp = msession.post(base_url, headers=self.hd,data=dates)
        print(resp.text)
        code = ''
        if resp.text.__contains__('need_verify'):
            codeurl = '{0}/node-api/captcha/image?phone={1}&type=mobile_login'.format(self.evn,self.phone_nu)
            msession.get(codeurl)
            code = self.getImageCode(msession)
            print('now starts login by code 2:{0}'.format(code))
            # 先声明了一个code
            return code

        if resp.text.__contains__('sms_code'):
            code = resp.json()['data']['sms_code']

        print('now starts login by code 1:{0}'.format(code))

        return code



    def login(self, code=None):
        mtimestamp = str(int(time.time()*1000)) #超时时间传递
        # 获取session
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename='userCookies.txt')

        # step1:
        resp1 = self.session.get('{0}/myaccount/login?redirect=%2Fmyaccount%2Fcenter'.format(self.evn),headers=self.hd)
        resp2 = self.getIp(self.session)
        dates = {'phone' : self.phone_nu,'type' : 'mobile_login','captcha_code': code,'timestamp':mtimestamp,
                 'fp':'f08dd59eecab5ad1fe9388f34d9516ca','fp_hash':'308514e7ff24e1dc8f6892c7e9e777d5',}
        # step2:
        code = self.sendSms(self.session,dates)
        self.session.cookies.save()
        # login
        login_url = '{0}/node-api/login/registerPhoneAccount'.format(self.evn)
        logindate = {
            'phone' : self.phone_nu,'type' : 'mobile_login','sms_code' : code,
        }
        print('uri is {0},{1}'.format(login_url,logindate))
        logsp = self.session.post(login_url,data=logindate)
        self.session.cookies.save()
        result = {
            'user_id_v2':logsp.json()['data']['user_token'],
            'track_user_id':logsp.json()['data']['track_user_id'],
        }
        # with open('userCookies.txt','a+') as f:
        #     f.write('Set-Cookie3: user_id_v2={0}; path="/"; domain=".test2.mm.t.xianghuanji.com"; path_spec; expires="2021-05-27 16:13:20Z"; version=0 \n'.format(logsp.json()['data']['user_token']))
        #     f.write('Set-Cookie3: track_user_id="{0}"; path="/"; domain=".test2.mm.t.xianghuanji.com"; path_spec; expires="2021-05-27 16:13:20Z"; version=0'.format(logsp.json()['data']['track_user_id']))
        # print(logsp.text)
        return result


    def leave(self):
        pass


if __name__ == '__main__':
    print('login code goes here:!!----->')
    # Auser = UserHelper(13812340005,'test2')
    # user = Auser.login()

    thd = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        'cookies':'utm_source=huabei; utm_source=huabei; utm_medium=huabei; utm_campaign=huabei; channelId=9; user_id_v2=XHJfacb756078dbd5c4aa8336bd5dc2ea4c; userToken=XHJfacb756078dbd5c4aa8336bd5dc2ea4c; track_user_id=s0UIAyYQngc%3D',
        'user_id_v2' : 'XHJfacb756078dbd5c4aa8336bd5dc2ea4c',
        'userToken' : 'XHJfacb756078dbd5c4aa8336bd5dc2ea4c',
        'utmCampaign':'huabei',
        'utmMedium': 'huabei',
        'platform':'h5_browser',
        'utmCampaign': 'huabei',
        'channelId':'9',
        'Connection':'keep-alive',
        'Referer': 'http://test2.mm.t.xianghuanji.com/mytrade/order/confirm?contract_product_id=1337',
    }
    # dates={'contract_product_id':1337,'coupon_ids':'','user_coupon_nums':'','delivery_type':1}
    # createApplyNo = requests.post('http://test2.mm.t.xianghuanji.com/node-api/trade/order/confirm/createApplyNo',data=dates,headers=thd)
    # apply_no = createApplyNo.json()['data']['apply_no']
    # print(apply_no)
    apply_no = 'A202005271713341752112837'
    date2 = {'apply_no':apply_no}
    confirmceateTrade = requests.post('http://test2.mm.t.xianghuanji.com/node-api/trade/order/confirm/ceateTrade',data=date2, headers=thd)


