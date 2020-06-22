# -*- coding: UTF-8 -*- 
import os
import decimal
from django.shortcuts               import render
from django.http                    import HttpResponse
from django.views.decorators.csrf   import csrf_exempt
from django.middleware.csrf         import get_token

import json
# ---------------订单相关的路由导航---------------------------
import mWeb.baseutils.tradeinfo as tradeinfo                #open in prod
import mWeb.baseutils.changetrade as changetrade            #open in prod

# ------------------db-----------------------------
import mWeb.ApiAutoTestUtils.common.dbUtil                  as testdbUtil # 测试环境的dbUtil

# ---------------ApiautoTestUtils ------------------------
import mWeb.ApiAutoTestUtils.common.configure               as configure
import mWeb.ApiAutoTestUtils.common.xlsxUtil                as xlsxUtil
import mWeb.ApiAutoTestUtils.common.autoTestContraller      as apiContraller
from mWeb.ApiAutoTestUtils.testCase.Testcase  import        Testcase
# --------------------------------------------------------

# --------------------CreateTradeUtils-------------------
import mWeb.TradeUtils.CreateTrade                         as CreateTrade

# --------------------------------------------------------



# --------------------------------------------------------
# ----------------------other apis------------------------
import mWeb.baseutils.thirdway.getAccount               as getAccount
# --------------------------------------------------------

# Create your views here.


def index(request):
    return HttpResponse("/Volumes/D/Projects/pyProj/XhjTest/mWeb/ApiAutoTestUtils/example.xlsx")

def otherapis(request):
    tradetype = request.GET.get('type')
    # 1:home页面的数据接口
    if '1' == tradetype:
        stat = tradeinfo.getJira()
        print(stat)
        return HttpResponse(json.dumps(stat))
    # 2:获取用户的user_id_v2:
    if '2' == tradetype:
        csrf_token = get_token(request)
        print(csrf_token)
        return HttpResponse(csrf_token)
    if '3' == tradetype:
        stat = tradeinfo.test4sql()
        return HttpResponse(json.dumps(stat))
    if '4' == tradetype: # 获取ishadowx账号
        resp = tradeinfo.test4sql()
        return HttpResponse(json.dumps(resp))
    return HttpResponse("<h1>XHJ django_backend apis</h1><hr />welcome to use xhj.")

'''
    getTradeInfo:状态码说明
    1 测试环境 根据 trade_no 获取订单的信息
    2 测试还机 根据 contract_no 获取订单的信息
    3 pro环境 根据 trade_no 获取订单的还机信息
    4 pro环境 根据 trade_no 获取订单的买断信息
'''
def getTradeInfo(request):
    tradeno = request.GET.get('trade_no')
    tradetype = request.GET.get('type')
    pro = request.GET.get('pro') #0:测试 1:买断 2:还机 3:小程序
    # print('tradeno:{0} and tradetype:{1}'.format(tradeno,tradetype))
    if '1' == tradetype:
        stat = tradeinfo.getTradeStatus(tradeno,1)
    elif '2' == tradetype:
        stat = tradeinfo.getTradeStatus(tradeno,2)
    elif '3' == tradetype:
        stat = tradeinfo.getProTradeinfo(tradeno,1,int(pro))
    elif '4' == tradetype:
        stat = tradeinfo.getProTradeinfo(tradeno,2,int(pro))
    else:
        return HttpResponse("<h1>XHJ django_backend apis/getTradeInfo</h1><hr />Oopsss! 404.")
    # print(stat) #TODO 中文乱码待处理
    print(json.dumps(stat),'->send to front')
    return HttpResponse(json.dumps(stat))

# 获取测试环境订单信息接口：getV2    20200328 v2.0.1
# class DecimalEncoder(json.JSONEncoder):

#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             return float(o)
#         super(DecimalEncoder, self).default(o)

def getV2(request):
    result = {}
    tradeno = request.GET.get('mtradeno')
    info = tradeinfo.getTrade(tradeno)
    if ({} != info):
        result = HttpResponse(json.dumps(info))
        return result
    result['err2'] = 'err2'
    return HttpResponse(result)


    
# 修改测试环境订单信息接口：changeV2 20200327 v2.0.1
def changeV2(request):
    tradeno = request.GET.get('mtradeno')
    changeType = request.GET.get('mtype')
    stats = request.GET.get('mselect')
    changetime = request.GET.get('mtime')
    # changetype 说明：1.修改订单状态 2-4:修改下单、签收、到期时间
    # 5:修订资金方 6:修改担保方 7:续租开关 8.江南人脸识别修改 9.线上用户token
    if '1' == changeType:
        result = changetrade.ChageStatu(tradeno,int(stats))
    elif changeType in ['2','3','4']:
        result = changetrade.changeTime(tradeno,int(changeType),changetime)
    elif changeType in ['5','6','7']:
        result = changetrade.changeChannel(tradeno,int(changeType),int(stats))
    elif changeType in ['8',]:
        result = changetrade.changeTable(tradeno,int(changeType))
    elif '9' == changeType: #查询线上用户的token
        info = tradeinfo.idba_user_token(tradeno)
        result = {'errtoken':'userid not found!'} if ([] == info) else info[0]['token']
    elif '10' == changeType: #创建测试环境的订单
        # tradeno = test9 # 测试环境编号
        pass
    else:
        return HttpResponse("<h1>XHJ django_backend apis/changeTradeInfo</h1><hr />Oopsss! 404.")
    return HttpResponse(result)


# 后续登录相关权限处理
def mlogin(request):
    resp = {

    }
    return HttpResponse(resp)


# 接口自动化相关地址配置
@csrf_exempt
def apitest(request):
    # 下面的方法其实是属于excel类存储到本地的方法，应该交给excel类处理
    # 需要优化一下，后续优化
    xlsfile = None
    # 将post的excel文件存储到本地
    if request.method == 'POST':
        xlsfile = request.body   #从post接口获取excel的二进制格式
        if None != xlsfile:
            dates = xlsfile.split(b'\r\n')  #去除http post多余的参数
            xlsxUtil.Xlsx.save2local(dates[4])
        else:
            return HttpResponse('xlsx 文件错误 请重试！')
    # 解析报错本地的excel文件
    # print(xlsxUtil.Xlsx().pdReadxlsx())
    # 开始执行接口自动化相关的方法了！交给其autotestcontraller类的方法执行！
    # apiContraller.runFlow().runLocal()
    # 开始执行线程跑接口测试
    xls = xlsxUtil.Xlsx().getxls2list()
    Testcase.saveTestcase(xls)


    # test save2db


    return HttpResponse('resp')

# 获取数据库里面所有的接口测试用例 在测试页面展示
def gettscases(request):
    asql = 'SELECT * FROM testcase;'
    result = Testcase.getAllcases(asql)
    return HttpResponse(result)

# 下载测试用例的接口
def downloads(request,types):
    path = ''
    resp = ''
    if 'excel'== types:
        path = configure.Configs().getExcelpath() 
    files = open(path,'rb')
    resp = HttpResponse(files)
    resp['Content-Type']='application/octet-stream'
    resp['Content-Disposition']='attachment;filename="example.xlsx"' 
    return resp

def runflow(request):
    mphone = request.GET.get('mphone')
    testevn = request.GET.get('testevn')
    mtype = request.GET.get('mtype')
    # 操作记录存储到sql中
    tc = apiContraller.runFlow()
    # 登陆

    # 下单

    # 走流程

    # 返回结果

    pass

if __name__ == '__main__':
    print('test goes here:')
    gettscases(1)
