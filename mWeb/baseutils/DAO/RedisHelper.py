# -*- coding: UTF-8 -*-
import redis


# redis 操作封装

class Redis(object):

    def __init__(self):
        self.host = ''
        self.port = 
        self.db = 
        self.pswd = ''
        self.conn = None

    def connDb(self):
        try:
            self.conn = redis.StrictRedis(host=self.host,port=self.port,db=self.db,password=self.pswd)
            print('connected!')
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
    def insert(self, sql, *value):
        if None != self.conn:
            num = self.getCursor().execute(sql, *value)
            self.conn.commit()
            return num

    # select
    def getKey(self, keyname):
        if None != self.conn:
            print(keyname)
            result = self.conn.get(keyname)
            print(result)
            return result

    def select_all(self, sql):
        if None != self.conn:
            corsor = self.getCursor()
            corsor.execute(sql)
            result = corsor.fetchall()
            self.conn.commit()
            return result

    # update
    def update(self, sql, *value):
        if None != self.conn:
            n = self.getCursor().execute(sql, *value)
            self.conn.commit()
            return n


if __name__ == "__main__":
    print('test env db code goes here:')
    # 图形验证码 模拟登陆相关的需求是可以做的！！
    # $key = 'image-code-' . $phone . '-' . $type;
    # JAF:bfa:image-code-18616376958-mobile_login :: key
    # JAF:bfa:7482                                :: value
    r = Redis()
    r.connDb()
    # a = r.getKey('JAF:bfa:image-code-18616376958-mobile_login')
    a = r.getKey('asdasdasdasdas')
    print(a)

