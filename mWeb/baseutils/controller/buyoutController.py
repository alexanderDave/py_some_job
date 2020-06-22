'''买断的监控'''
import mWeb.baseutils.Utils.idbaUtils as idbaUtils
import mWeb.baseutils.Utils.dtalk as dtalk


Helper = idbaHelper.Idbapi('daiwei','vStwuU9uYi84g6S=')
idbSession = Helper.getApi()
# 获取t-1日申请买断的订单的信息：t-1日创建了买断记录的订单
'''
    func：
    return：
    exception:
'''
def get_buyout_trade():
    static_url = ''
    result = 
    pass


# 获取t-1日买断订单的
'''
    func：
    return：
    exception:
'''

# 买断失败报警
'''
    func：
    return：
    exception:
'''


# t+12h日后订单还没完成买断dtalk报警
'''
    func：
    return：（订单号：申请买断时间：，结算费用：，代扣步骤：，超过12小时没有结算完成，请查看具体原因）
    exception:
'''

# 小程序订单完成买断后没有推送芝麻守约记录报警
'''
    func：
    return：（订单号：申请买断时间：，结算费用：，代扣步骤：，结算完成后没有推送芝麻守约，请查看具体原因）
    exception:
'''