import requests
import time
import http.cookiejar as cookielib


'''
   用于模拟登录其他os的类  
'''
# tips:
# 经查发现，erp的登陆与 idba的登陆系统一致，后续考虑将两个class合并为一个

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

# 线上idba的模拟登录
class Idbapi(object):

    def __init__(self,uname,pswd):
        self.uname = uname
        self.pswd = pswd

    def getApi(self):
        t = time.time()
        timestamp = str(int(t*1000))
        form_data = {
            'username': self.uname,
            'password': self.pswd,
            'redirect_url': 'L3NxbC9xdWVyeQ==',
            'app_id': '25',
            'timestamp': timestamp,
        }
        ajx_url = 'http://auth.xianghuanji.com/login/ajax/authorize' # post
        mhd = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://auth.xianghuanji.com',
            'Referer': 'http://auth.xianghuanji.com/login/authorize?app_id=25&redirect_url=L3NxbC9xdWVyeQ==',
            'User-Agent': UA,
            'X-Requested-With': 'XMLHttpRequest',
        }

        idbSession = requests.session()
        idbSession.cookies = cookielib.LWPCookieJar(filename='idbaCookies.txt')
        Resp_before = idbSession.post(ajx_url,data=form_data,headers=mhd)
        loginUrl = Resp_before.json()['data']['callbackurl']
        print(loginUrl) # show for checking if the url wrong!
        try:
            Resp_aftere = idbSession.get(loginUrl,timeout=10)
        except (requests.ConnectionError):
            print('connection failed')
        idbSession.cookies.save()
        return idbSession

# erp 后台模拟登陆
class Erpapi(object):

    def __init__(self,testevn,uname,pswd):
        self.testevn = testevn
        self.uname = uname
        self.pswd = pswd

    def getApi(self):
        t = time.time()
        timestamp = str(int(t*1000))
        login = {
            'username':self.uname,'password':self.pswd,'app_id':'47','timestamp':timestamp,
            'redirect_url':'http://{0}.erp.t.xianghuanji.com/'.format(self.testevn),
        }
        mhd = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': r'http://{0}.auth.t.xianghuanji.com/login/auth?app_id=47&redirect_url=http%3A%2F%2F{0}.erp.t.xianghuanji.com%2F'.format(self.testevn),
            'User-Agent': UA,
            'X-Requested-With': 'XMLHttpRequest',
        }
        ajax_url = 'http://{0}.auth.t.xianghuanji.com/login/ajax/authorize'.format(self.testevn)

        idbSession = requests.session()
        idbSession.cookies = cookielib.LWPCookieJar(filename='erpCookies.txt')
        Resp_before = idbSession.post(ajax_url,data=login,headers=mhd)
        loginUrl = Resp_before.json()['data']['callbackurl']
        print(loginUrl)
        try:
            Resp_aftere = idbSession.get(loginUrl,timeout=10)
        except (requests.ConnectionError):
            print('connection failed')
        idbSession.cookies.save()
        return idbSession


if __name__ == "__main__":
    print("here goes the test")

    # this is a test for erpHelper
    myErp = Erpapi('test9','daiwei','000123')
    erper = myErp.getApi()







