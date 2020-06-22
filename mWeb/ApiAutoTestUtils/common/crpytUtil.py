# -*- coding: UTF-8 -*- 


class MyCrypt(object):

    def __init__(self):
        self.__key = ''

    def getKey(self):
        return self.__key

    def setKey(self,key):
        self.__key = key

    def encrypt(self,mstr):
        mbyte = bytearray(str(mstr).encode('utf8'))
        lens = len(mbyte)
        change = bytearray(lens*2)
        j = 0
        for i in range(0,lens):
            b1 = mbyte[i]
            b2 = b1^self.__key
            c1 = b2%16
            c2 = b2 // 16
            c1 = c1+65
            c2 = c2+65
            change[j] = c1
            change[j+1] = c2
            j = j+2

        return change.decode('utf8')

    def decrypt(self,mstr):
        mbyte = bytearray(str(mstr).encode('utf8'))
        n = len(mbyte)
        if n%2 != 0:
            return False
        n = n // 2
        change = bytearray(n)
        j=0
        for i in range(0,n):
            c1 = mbyte[j]
            c2 = mbyte[j+1]
            j = j+2
            c1 = c1 -65
            c2 = c2 -65
            b2 = c2*16 + c1
            b1 = b2^self.__key
            change[i] = b1
        try:
            return change.decode('utf8')
        except:
            return False
        
    
if __name__ == "__main__":
    print('test here')
    

