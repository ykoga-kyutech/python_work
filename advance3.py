# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題3.
3. コマンドラインから都道府県番号も受け取れるようにせよ
(番号の頭0は不要。また、都道府県を指定するかは任意とする)
の解答。
"""

import sys
import grounabi_restaurant_api as g_api

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"

  if len(sys.argv) != 3:
    print("Example: $ python advance3.py 33 居酒屋")
    sys.exit(0)
  else:
    # 都道府県番号をコマンドライン引数から貰う
    pref = "PREF"+sys.argv[1]
    # 店舗名のキーワードをコマンドライン引数から貰う
    name = sys.argv[2]

  # ぐるなびレストランAPIアクセス用
  api = g_api.GrounabiRestaurantAPI(url, keyid)

  # create a query
  query = [
    ( "format", "json" ),
    ( "keyid", keyid ),
    ( "pref", pref ),
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