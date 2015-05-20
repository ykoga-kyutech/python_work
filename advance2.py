# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題2.
1. コマンドライン引数から受け取った検索キーワードが日本語かどうか判定し、
それにより利用する検索APIをそれぞれレストラン検索API/多言語版レストラン
検索APIで切り替えよ。
なお、条件により対応するAPIの数は今後増えていくということを考慮した設計にすること
の解答。
"""

import sys
import grounabi_restaurant_api as g_api
import grounabi_bilingual_restaurant_api as gb_api

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"

  # エンドポイントURL
  urlname_restsearch = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
  urlname_bilin_restsearch = "http://api.gnavi.co.jp/ver2/RestSearchAPI/"

  name = ""
  api = None
  try:
      if len(sys.argv) != 2:
        print("Example1: $ python advance2.py 居酒屋")
        print("Example2: $ python advance2.py Dining")
        sys.exit(0)
      else:
        # 店舗名をコマンドライン引数から貰う（日本語/英語）
        name = sys.argv[1]
        name.encode('ascii', 'strict')
        # ぐるなびレストランAPIアクセス用（英語）
        api = gb_api.GrounabiBilingualRestaurantAPI(urlname_bilin_restsearch, keyid)
  except UnicodeEncodeError:
      # ぐるなびレストランAPIアクセス用
      api = g_api.GrounabiRestaurantAPI(urlname_restsearch, keyid)

  # create a query
  query = [
    ( "format", "json" ),
    ( "keyid", keyid ),
    ( "name", name )
  ]

  # set query
  api.setQuery(query)

  # get result
  data = api.execute()

  # show result
  if data is not None:
    api.showResult(api.decode2JSON(data))
  else:
    print("APIアクセスに失敗しました。")