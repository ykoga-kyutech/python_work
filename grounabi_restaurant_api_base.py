# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import urllib
import urllib.request
import urllib.parse
import sys
import json

class GrounabiRestaurantAPIBase(object):

  def __init__(self, url=None, apikey=None):
    if url == None:
      print("Please set the API URL! The system will exit. ")
      sys.exit(0)
    if apikey == None:
      print("Please set the API key! The system will exit. ")
      sys.exit(0)
    self.apikey = apikey
    self.url = url
    self.query = None

  def setQuery(self, query):
    self.query = query

  def getQuery(self):
    return self.query

  def execute(self):
    # URL生成
    data = urllib.parse.urlencode( self.query )
    url = self.url + '?'+data
    #print(url)
    # API実行
    try :
      return urllib.request.urlopen(url)
    except ValueError :
      return None

  @staticmethod
  def decode2JSON(result):
    return json.loads( result.read().decode('utf-8') )

  ####
  # 変数の型が文字列かどうかチェック
  ####
  @staticmethod
  def is_str(data = None ) :
    if isinstance( data, str ): # or isinstance( data, unicode )
      return True
    else :
      return False

  def showResult(self, result):
    pass