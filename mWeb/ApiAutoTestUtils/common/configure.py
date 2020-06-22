# -*- coding: UTF-8 -*- 
import os

import mWeb.ApiAutoTestUtils.common.crpytUtil as crpytUtil

# import crpytUtil

pwd1 = os.path.split(os.path.realpath(__file__))[0]
pwd2 = os.path.dirname(pwd1)
cfgpath = os.path.join(pwd2,'config.ini')       # 接口配置文件路径
excelpath = os.path.join(pwd2,'example.xlsx')   # 接口测试用例模板

'''
func:getInfo    获取配置文件信息
params:file     配置文件路径
'''
def getInfo(file):
    mstr = ''
    result = {}
    with open(file) as f:
        line = f.readline()
        while line:
            line = line.replace('\n','').replace(' ','')
            if (not line.startswith('#')) and (line != ''):
                mstr += line+'\n'
            line = f.readline()
        title = mstr.split('[')[1:]
        for tt in title:
            info = tt.split(']')
            title = info[0]
            lists = info[1].split('\n')[1:-1]
            mdict = {}
            for info in lists:
                key = info.split('=')[0]
                value = info.split('=')[1]
                mdict[key] = value
            result[title] = mdict

    f.close()
    return result

class Configs(object):

    def __init__(self):

        infos = getInfo(cfgpath)
        Crypts = crpytUtil.MyCrypt()
        # db
        self.__dbhost = Crypts.decrypt(infos['DATABASE']['host'])
        self.__dbname = Crypts.decrypt(infos['DATABASE']['username'])
        self.__dbpswd = Crypts.decrypt(infos['DATABASE']['password'])
        self.__dbport = Crypts.decrypt(infos['DATABASE']['port'])
        self.__dbku   = infos['DATABASE']['database']

        # testdb
        self.__testdbhost = Crypts.decrypt(infos['TESEDB']['host'])
        self.__testdbname = Crypts.decrypt(infos['TESEDB']['username'])
        self.__testdbpswd = Crypts.decrypt(infos['TESEDB']['password'])
        self.__testdbport = Crypts.decrypt(infos['TESEDB']['port'])

        # http
        self.__httpurl = infos['HTTP']['baseurl']
        self.__httport = infos['HTTP']['timeout']
        
        # mail
        self.__mailhost = infos['EMAIL']['mail_host']
        self.__mailname = infos['EMAIL']['mail_user']
        self.__mailpswd = Crypts.decrypt(infos['EMAIL']['mail_pass'])
        self.__mailport = infos['EMAIL']['mail_port']   

    def getDbhost(self):
        return self.__dbhost

    def getDbuser(self):
        return self.__dbname

    def getDbpswd(self):
        return self.__dbpswd

    def getDbport(self):
        return self.__dbport

    def gettDbhost(self):
        return self.__testdbhost

    def gettDbuser(self):
        return self.__testdbname

    def gettDbpswd(self):
        return self.__testdbpswd

    def gettDbport(self):
        return self.__testdbport

    def getDbku(self):
        return self.__dbku

    def getHttpurl(self):
        return self.__httpurl

    def getHttptout(self):
        return self.__httport

    def getMailhost(self):
        return self.__mailhost

    def getMailname(self):
        return self.__mailname

    def getMailpswd(self):
        return self.__mailpswd

    def getMailport(self):
        return self.__mailport

    def getExcelpath(self):
        return excelpath




if __name__ == '__main__':
    print('test here:')
    print(Configs().getDbhost())
    print(Configs().gettDbhost())
    