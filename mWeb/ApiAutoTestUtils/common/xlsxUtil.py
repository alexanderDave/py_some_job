# -*- coding: UTF-8 -*-
import time,os
import datetime
import xlrd
import pandas as pd

import mWeb.ApiAutoTestUtils.common.dbUtil as dbUtil

# Xlsx 解析excel的类
class Xlsx(object):
    
    # 初始化数据
    def __init__(self):
        pwd1 = os.path.split(os.path.realpath(__file__))[0]
        pwd2 = os.path.dirname(pwd1)
        self.excelpath = os.path.join(pwd2,'dates.xlsx')
        self.dates = None
        self.books = None
        self.lists = None
        
    
    # 根据路径获取excel表的数据
    def openXlsxFile(self):
        try:
            self.books = xlrd.open_workbook(filename=self.excelpath)
            print('self.dates',self.dates)
            print('self.books',self.books)
            return self.books
        except Exception as identifier:
            return identifier

    def openXlsxStream(self):
        try:
            self.books = xlrd.open_workbook(file_contents=self.dates)
            return self.books
        except Exception as identifier:
            return identifier
    
    # 根据字节流获取excel表的数据
    def pdReadxlsx(self):
        if None != self.dates:
            self.dates = None
        self.dates = pd.read_excel(self.excelpath,sheet_name='test')
        # print(type(self.dates))
        # print(self.dates)


    # pd格式的xls表解析字典组装list格式，方便后面传递 TODO :fix bug:that this func doesn't work!
    # caseid  casename  url  params  method  dates  auth  infos  model  except  rules
    def getxls2list(self):
        if None == self.dates:
            self.pdReadxlsx()
        info = []
        for index,row in self.dates.iterrows():
            temp = []
            temp.append(row["casename"])
            temp.append(row['url'])
            temp.append(row['params'])
            temp.append(row['method'])
            temp.append(row['auth'])
            temp.append(row['infos'])
            temp.append(row['Model'])
            temp.append(row['except'])
            temp.append(row['rules'])
            info.append(temp)
        self.lists = info
        return info

    # 解析excel表格方法，方法需要抽象起来，方便后续代码的复用
    def getXlsx(self):
        if self.books:
            # todo:
            print(len(self.books.sheets()))
            if len(self.books.sheets()) > 0:
                sheet = self.books.sheets()[0]
                rows  = sheet.nrows # excel的行数
                cols  = sheet.ncols # excel的列数
                print('this table contains {0} row,{1} cols'.format(rows,cols))
                if 1 < rows:
                    mlist = []
                    for i in range(1,rows):
                        n = []
                        for j in range(cols):
                            n.append(sheet.cell(i,j).value)
                        mlist.append(n)
                    print(str(mlist))
                    self.lists = mlist
                    return mlist
                else:
                    raise Exception

        return False

    # 获取excl表中的post方法的信息，用元祖存成列表格式
    def getPostlists(self):
        
        if False != self.lists:
            mlist = []
            for target in self.lists:
                if 'POST' == (str(target[3])).upper():
                    mlist.append((target[2],target[4]))
            return mlist
        return False

    # 获取excl表中的get方法的信息，用元祖存成列表格式
    def getGetlists(self):
        
        if False != self.lists:
            mlist = []
            for target in self.lists:
                if 'GET' == (str(target[3])).upper():
                    mlist.append((target[2],target[7]))
            return mlist
        return False

    @staticmethod
    def dealCodes(byteStr):
        context = byteStr.splitlines()
        return context[-2]

    # 将excel存储在系统本地，方便读取调用
    @staticmethod
    def save2local(Bdates):
        pwd1 = os.path.split(os.path.realpath(__file__))[0]
        pwd2 = os.path.dirname(pwd1)
        excelpath = os.path.join(pwd2,'dates.xlsx')
        with open(excelpath,'wb') as f:
            f.write(Bdates)
        

if __name__ == "__main__":
    print('test here:')

    xls = Xlsx()
    xls.pdReadxlsx()
    print(xls.getxls2list())

