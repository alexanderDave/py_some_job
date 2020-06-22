# -*- coding: UTF-8 -*-


import mWeb.ApiAutoTestUtils.common.dbUtil as dbUtil
import json
from datetime import datetime

class Testcase(object):
    
    def __init__(self):
        pass

    # 保存接口测试用例的excel表格中的数据 用例表
    # caseid  casename  url  params  method  dates  auth  infos  model  except  rules
    @staticmethod
    def saveTestcase(lists):
        times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if lists:
            dbHelper = dbUtil.DB()
            dbHelper.connDb()
            for lt in lists:
                msql = '''insert into testcase (casename,url,params,method,auth,infos,model,`except`,rules,dates) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}',"{7}",'{8}','{9}');
                '''.format(lt[0], lt[1], lt[2], lt[3], lt[4], lt[5], lt[6], lt[7], lt[8],times)
                print(msql)
                dbHelper.insert(msql)
            dbHelper.closeDb()
            return True
        return False

    # 从测试服务器上的测试数据库里读取所有的测试用例
    # 格式{{'case n':{'caseid':'id','casename':'name'...}},{'case n':{'caseid':'id','casename':'name'...}},...}
    @staticmethod
    def getAllcases(asql):
        db = dbUtil.DB()
        db.connDb()
        result = db.select_all(asql)
        db.closeDb()
        minfo = {}
        if () != result:
            for info in result:
                infos = {}
                infos['caseid'] = info[0]
                infos['casename'] = info[1]
                infos['url'] = info[2]
                infos['params'] = info[3]
                infos['method'] = info[4]
                infos['dates'] = str(info[5])
                infos['auth'] = info[6]
                infos['infos'] = info[7]
                infos['model'] = info[8]
                infos['except'] = info[9]
                infos['rules'] = info[10]
                minfo['caseid{0}'.format(info[0])] = infos
        # 转成json格式给前段进行调用；否则页面展示处理比较困难。
        mresult = json.dumps(minfo)
        # print(mresult)
        return mresult

    # 获取对应模块的接口测试case
    # 格式 [[dates],[dates],[dates]... ]
    @staticmethod
    def getModelcase(models):
        asql = "SELECT * FROM testcase where model = '{0}';".format(models)
        db = dbUtil.DB()
        db.connDb()
        result = db.select_all(asql)
        db.closeDb()
        if () != result:
            results = []
            for info in result:
                minfos = []
                minfos.append(info[2])
                minfos.append(info[3])
                minfos.append(info[4])
                minfos.append(info[9])
                results.append(minfos)
        # print(results)
        return results


if __name__ == '__main__':
    print('testcase：')
    # testsql = 'SELECT * FROM testcase;'
    # # Testcase.getAllcases(testsql)
    # Testcase.getModelcase('dqcz');
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))