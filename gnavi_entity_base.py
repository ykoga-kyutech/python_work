# -*- coding: utf-8 -*-
__author__ = 'tie304184'

class GNaviEntity(object):
    def __init__(self):
        self.json_data = None
    def getEntity(self):
        if self.json_data == None:
            print("JSON data have not set! Please set it before call this method!")
            return
        else:
            #return self.json_data
            pass
    def setEntity(self, json_data):
        self.json_data = json_data

    ####
    # 変数の型が文字列かどうかチェック
    ####
    def is_str(self, data = None ) :
        if isinstance( data, str ): # or isinstance( data, unicode )
          return True
        else :
          return False