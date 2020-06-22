# -*- coding: UTF-8 -*-
import sys,io
import requests
import re,json
from lxml import etree
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# for urls in website_list:
head = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate'
}
class Mails(object):

    def __init__(self, uname, paswd, port, host):
        self.mhost = host
        self.uname = uname
        self.paswd = paswd
        self.mport = port
        self.mtag = None

    def Send(self, address, context):
        try:
            server = smtplib.SMTP_SSL(self.mhost, port=self.mport)
            server.login(self.uname, self.paswd)
            server.sendmail("<%s>" % self.uname, address, self.get_attach(address, context))
            server.close()
        except Exception as identifier:
            print('er!')

    def get_attach(self, address, context):
        mattach = MIMEMultipart()
        if self.mtag:
            mattach["Subject"] = self.mtag
        mattach["From"] = self.uname
        mattach["To"] = ';'.join(address)
        mattach.attach(MIMEText(context, 'plain', 'utf-8'))
        return mattach.as_string()

def getAccount():
    url = 'https://my.ishadowx.biz/'
    ip_list = []
    r = requests.get(url, headers=head)
    # print(r.text)
    paser = etree.HTML(r.content)

    vemss1 = paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div/div/h4[1]/span/@data-clipboard-text')
    vemss2 = paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[5]/div/div/div/h4[1]/span/@data-clipboard-text')
    vemss3 = paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[6]/div/div/div/h4[1]/span/@data-clipboard-text')
    result = vemss1[0] + vemss2[0] + vemss3[0]

    for x in [1,2,3,7,8,9]:
        ip =   paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[{0}]/div/div/div/h4[1]/span[1]/text()'.format(x))
        port = paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[{0}]/div/div/div/h4[2]/span[1]/text()'.format(x))
        pswd = paser.xpath('/html/body/div[3]/div[2]/div[2]/div/div[{0}]/div/div/div/h4[3]/span[1]/text()'.format(x))
        result = result + ip[0] + port[0] + pswd[0]

    test_receiver = ['jiandanalexander@icloud.com']
    # print(result)
    mailer = Mails('wei.dai@xianghuanji.com','2019@xhj.coM','465','smtp.exmail.qq.com')
    mailer.Send(test_receiver,result)
    # return ip_list
    return result








if __name__=='__main__':
    # for urls in website_list:
    resp = getAccount()

# //*[@id="portfolio"]/div[2]/div[2]/div/div[3]/div/div/div/h4[1]
    # for x in ip_list:
    #     for k,v in x.items:
    #         print("here goes demo:")
    #         print(k,v)
    #         print("new line",'\n')
# //*[@id="portfolio"]/div[2]/div[2]/div/div[1]

