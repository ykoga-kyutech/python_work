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
import grounabi_restaurant_api_base as base_api
import yaml

if __name__ == '__main__':

  # APIアクセスキーを含む設定ファイル
  setting_file = "advance_settings.yaml"

  # エンドポイントURL
  urlname_restsearch = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
  urlname_bilin_restsearch = "http://api.gnavi.co.jp/ver2/RestSearchAPI/"

  # 設定ファイルからAPIキーを読み込む
  try:
    with open(setting_file, 'r') as f:
      data = yaml.load(f)  # 読み込む
      keyid = data['keyid']
  except FileNotFoundError as e:
    print(setting_file+"が見つかりませんでした。")
    print("実行には"+setting_file+"が必要です。README.mdを参照してください。")
    print("終了します。")
    sys.exit(0)

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
    api.showResult(base_api.GrounabiRestaurantAPIBase.decode2JSON(data))
  else:
    print("APIアクセスに失敗しました。")