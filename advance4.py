# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題4.
応援APIを利用し、各店舗の応援を取得せよ。
取得するのは上位3件の店舗分のみで構わないが、
この指定が今後変えられるよう考慮すること。
なお、取得処理は並列で実行すること（asyncioを使用）。
の解答。
"""

import sys
import grounabi_ouen_api as g_api

def callback():
    print("callback called")

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/"

  # ぐるなびレストランAPIアクセス用
  api = g_api.GrounabiOuenAPI(url, keyid)

  if len(sys.argv) == 2 :
    name = sys.argv[1]
  else:
    print("Example: python advance4.py 居酒屋")
    sys.exit(0)

  # create a query
  query = [
    ( "format", "json" ),
    ( "keyid", keyid ),
    ( "shop_name", name)
    #( "callback", callback )
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