# -*- coding: UTF-8 -*-
import MySQLdb

import mWeb.ApiAutoTestUtils.common.configure as configure

# 注意：这个db的类和haseUtil下的不一样；不能算作冗余代码删除
# 这个类配置的host是测试服务器上的数据库
class DB(object):

    def __init__(self):
        cfg = configure.Configs()
        self.host = cfg.getDbhost()
        self.user = cfg.getDbuser()
        self.pwsd = cfg.getDbpswd()
        self.port = int(cfg.getDbport())
        self.database = cfg.getDbku()
        self.conn = None

    def connDb(self):
        try:
            self.conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwsd,db=self.database,charset='utf8')
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

    def select_all(self,sql,*value):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql,*value)
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
    print('test servier db code goes here:')
    db = DB()
    print(db.update("insert into testcase (casename,url,params,method,dates,auth) values ('demo','/user.local','demo','get','2019-10-10','dw')"))
    print(db.select_one('select * from testcase'))
    db.closeDb()


''' testcase
|casename  | varchar(100) | NO   |     | NULL    |                |
| url      | varchar(100) | NO   |     | NULL    |                |
| params   | varchar(200) | YES  |     | NULL    |                |
| method   | varchar(10)  | NO   |     | NULL    |                |
| dates    | date         | YES  |     | NULL    |                |
| auth     | varchar(20)  | YES  |     | NULL    | 

+--------+----------+-------------+--------+--------+------------+------+-------+-------+
| caseid | casename | url         | params | method | dates      | auth | infos | model |
+--------+----------+-------------+--------+--------+------------+------+-------+-------+
|      1 | demo     | /user.local | demo   | get    | 2019-10-10 | dw   |       |       |
+--------+----------+-------------+--------+--------+------------+------+-------+-------+

'''