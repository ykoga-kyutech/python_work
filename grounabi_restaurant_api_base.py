# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import urllib
import urllib.request
import urllib.parse

class GrounabiRestaurantAPIBase(object):

  def __init__(self, url, apikey):
    self.apikey = apikey
    self.url = url
    self.query = None

  def setQuery(self, query):
    self.query = query

  def getQuery(self):
    return self.query

  """
  def createQuery(self, q):
    query = [
      ( "format", "json" ),
      ( "keyid", keyid )
      #( "name", name )
    ]
    query.append()
    return query
  """

  def execute(self):
    # URL生成
    data = urllib.parse.urlencode( self.query )
    url = self.url + '?'+data
    #print(url)
    # API実行
    try :
      result = urllib.request.urlopen(url)
      return result
    except ValueError :
      return None

  ####
  # 変数の型が文字列かどうかチェック
  ####
  def is_str(self, data = None ) :
    if isinstance( data, str ): # or isinstance( data, unicode )
      return True
    else :
      return False

  def showResult(self, result):
    pass