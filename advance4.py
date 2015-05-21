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
import  grounabi_restaurant_api_base as base_api
import yaml

if __name__ == '__main__':

  # APIアクセスキーを含む設定ファイル
  setting_file = "advance_settings.yaml"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/"

  # 設定ファイルからAPIキーを読み込む
  keyid = ""
  try:
    with open(setting_file, 'r') as f:
      data = yaml.load(f)  # 読み込む
      keyid = data['keyid']
  except FileNotFoundError as e:
    print(setting_file+"が見つかりませんでした。")
    print("実行には"+setting_file+"が必要です。README.mdを参照してください。")
    print("終了します。")
    sys.exit(0)

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