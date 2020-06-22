# -*- coding: utf8 -*-

import json
import os
import requests
import threading

import mWeb.ApiAutoTestUtils.common.apiUtil        as apiUtils
import mWeb.ApiAutoTestUtils.common.xlsxUtil       as xlsxUtil
import mWeb.ApiAutoTestUtils.testCase.Testcase     as Testcase

class runFlow(object):

    def __init__(self):
        self.testcase = None
        
    # 执行上传的excel里面的接口测试
    def runLocal(self):

        # 获取接口数据
        ts = xlsxUtil.Xlsx().getxls2list()
        # 接口数据处理 简单去除错误的数据信息
        self.testcase = self.cleantc(ts)
        # 执行接口测试用例
        self.runCase()
        # 保存处理后的接口测试用例
        Testcase.saveTestcase(self.testcase)

        pass


    # 根据选择的流程type执行接口测试
    def runFlow(self):
        pass

    # 保存执行的接口用例
    def runCase(self):
        if None == self.testcase:
            return False
        for caselist in self.testcase:
            #
            for cases in caselist:
                #
                pass
            pass
        pass
        #
        #     t = threading.Thread(target=self.apis.get,args=postlist)
        #     t.start()
        #     t.join()
        pass

    # 清理
    @staticmethod
    def cleantc(mlist):
        result = []

        return result
    
    pass







if __name__ == "__main__":
    print('test here')