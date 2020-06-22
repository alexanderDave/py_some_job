# -*- coding: utf8 -*-

import json
import os
import requests
def atone(content,atmobiles,url='https://oapi.dingtalk.com/robot/send?access_token=69e5a052abfe1cec249d141618690e7ce30fd2beed35357bc798d75c9082c95f'):
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
                atmobiles
            ],
            "isAtAll": False
        }
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
               "Content-Type": "application/json"}

    send_data = json.dumps(data).encode('utf-8')
    requests.post(url=url, data=send_data, headers=headers)


def atall(content,url='https://oapi.dingtalk.com/robot/send?access_token=69e5a052abfe1cec249d141618690e7ce30fd2beed35357bc798d75c9082c95f'):

    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },

    }
    # data = {"msgtype": "markdown", "markdown": {"title": "监控", "text": content}}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    send_data = json.dumps(data).encode('utf-8')
    requests.post(url=url, data=send_data, headers=headers)


def atallmd(content,url='https://oapi.dingtalk.com/robot/send?access_token=69e5a052abfe1cec249d141618690e7ce30fd2beed35357bc798d75c9082c95f'):
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=28f73f0cf7125ac2aa8dc1a0619dc2b74844b513d62d68e67cac153d9c160394'

    # data = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": content
    #     },
    #
    # }
    data = {"msgtype": "markdown", "markdown": {"title": "监控", "text": content}}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    send_data = json.dumps(data).encode('utf-8')
    requests.post(url=url, data=send_data, headers=headers)


def getpast(urls):
    resp = requests.get(urls)
    text = resp.text
    return text

if __name__ == "__main__":
    
    atone("监控：接口测试执行中...", '18616376958')

    # baseurl = 'http://test4.bfa.t.xianghuanji.com/alipayMiniApp/returnFlow/commit?'
    # params = 'ahs_store_id=&express_code=zhongtong&express_number=731223814105961&id_user=9670365&return_type=2&trade_no=TS20190801434860836624&utm_campaign=&utm_medium=small_xhj&utm_source=alipay'

    # urls = baseurl+params


    # for i in range(1,5):
    #     print(getpast(urls))
    #     print()
    # pass