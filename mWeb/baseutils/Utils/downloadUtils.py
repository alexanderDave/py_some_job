# -*- coding: UTF-8 -*- 
import os

mpath = os.path.abspath(__file__)
excelpath = os.path.dirname(os.path.dirname(os.path.dirname(mpath)))
excelpath = os.path.join(excelpath,'ApiAutoTestUtils/example.xlsx')

class Downloads(object):

    def __init__(self,path):
        self.path = path
    
    
    def Starts(self):
        pass

    def funcname(self):
        pass
    

    def getDownload(self,path):
        pass

    
if __name__ == "__main__":
    print('test')
    print(excelpath)