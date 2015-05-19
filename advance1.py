# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題1.
1. コマンドライン引数から検索キーワードを受け取り、
ぐるなびAPIにアクセスし検索結果(店舗名)を出力せよ。
受け取るデータ型はJSON形式にすること
の解答。
"""
import sys
import grounabi_restaurant_api as g_api

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
  # 店舗名をコマンドライン引数から貰う
  name = sys.argv[1] 

  # ぐるなびレストランAPIアクセス用
  api = g_api.GrounabiRestaurantAPI(url, keyid)

  # create a query
  query = [
    ( "format", "json" ),
    ( "keyid", keyid ),
    ( "name", name )
  ]

  # set query
  api.setQuery(query)

  # get result
  result = api.execute()

  # show result
  if result is not None:
    api.showResult(result)
  else:
    print("APIアクセスに失敗しました。")