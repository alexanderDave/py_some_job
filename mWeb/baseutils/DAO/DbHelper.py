# -*- coding: UTF-8 -*-
import MySQLdb

import mWeb.ApiAutoTestUtils.common.configure as configure

# 注意：这个db的类和ApiAutoTestUtil下的不一样；不能算作冗余代码删除
# 这个类配置的host是测试环境的数据库
class DB(object):

    def __init__(self):
        cfg = configure.Configs()
        self.host = cfg.gettDbhost()
        self.user = cfg.gettDbuser()
        self.pwsd = cfg.gettDbpswd()
        self.port = int(cfg.gettDbport())
        self.conn = None

    def connDb(self,mdatabase):
        try:
            self.conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwsd,db=mdatabase,charset='utf8')
        except Exception as identifier:
            return identifier
        

    def closeDb(self):
        if None != self.conn:
            self.conn.close()
        return True
    
    def getCursor(self):
        if None != self.conn:
            return self.conn.cursor()

    # insert
    def insert(self,sql,*value):
        if None != self.conn:
            num = self.getCursor().execute(sql,*value)
            self.conn.commit()
            return num

    # select
    def select_one(self,sql,*value):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql,*value)
            result = corsor.fetchone()
            self.conn.commit()
            return result

    def select_all(self,sql):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql)
            result = corsor.fetchall()
            self.conn.commit()
            return result

    # update
    def update(self,sql,*value):
        if None != self.conn:
            n = self.getCursor().execute(sql,*value)
            self.conn.commit()
            return n

     

if __name__ == "__main__":
    print('test env db code goes here:')


