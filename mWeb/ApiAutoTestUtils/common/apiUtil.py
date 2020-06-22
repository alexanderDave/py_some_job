# -*- coding: UTF-8 -*- 
'''
                            接口测试api
'''
import os
import requests

import mWeb.ApiAutoTestUtils.common.configure as configure
import mWeb.baseutils.Utils.dtalk             as dtalks

class apis(object):
    
    def __init__(self):
        cfg = configure.Configs()
        self.baseUrl = cfg.getHttpurl()
        self.baseTimeout = cfg.getHttpurl()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.dtalk = 'https://oapi.dingtalk.com/robot/send?access_token=eaa30b4d3c10a49b04afd0acfe323f1b3d8d22840f9bc991445ad76a26a16a90'
        
    def setHeaders(self,mheader):
        self.headers = mheader

    def setParams(self,par):
        self.params = par

    def setTimeout(self,tout):
        self.baseTimeout = tout

    def setData(self,datas):
        self.data = datas

    def setUrl(self,urls):
        self.baseUrl = urls


    def get(self,tupes):
        url = tupes[0] if tupes[0].startswith('http') else self.baseUrl+tupes[0]
        resp = None
        try:
            dtalks.atone('消息:正在执行接口{0}'.format(url),'18616376958',url=self.dtalk)
            resp = requests.get(url,params = tupes[1],headers = self.headers,timeout = self.baseTimeout)
        except TimeoutError:
            print('time out!')
        return resp

    def post(self,tupes):
        url = tupes[0] if tupes[0].startswith('http') else self.baseUrl+tupes[0]
        resp = None
        try:
            dtalks.atone('消息:正在执行接口{0}'.format(url),'18616376958',url=self.dtalk)
            resp = requests.post(url,data = tupes[1],headers = self.headers,timeout = self.baseTimeout)
        except TimeoutError:
            print('time out!')
        return resp

    def test(self):
        pass


if __name__ == "__main__":
    print('test here')