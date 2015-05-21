# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題3.
コマンドラインから都道府県番号も受け取れるようにせよ
(番号の頭0は不要。また、都道府県を指定するかは任意とする)
の解答。
"""

import sys
import gnavi_restaurant_api as g_api
import gnavi_restaurant_api_base as base_api
import yaml

if __name__ == '__main__':

  # APIアクセスキーを含む設定ファイル
  setting_file = "advance_settings.yaml"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"

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

  if len(sys.argv) != 3:
    print("Example: $ python advance3.py 33 居酒屋")
    sys.exit(0)
  else:
    # 都道府県番号をコマンドライン引数から貰う
    pref = "PREF"+sys.argv[1]
    # 店舗名のキーワードをコマンドライン引数から貰う
    name = sys.argv[2]

  # ぐるなびレストランAPIアクセス用
  api = g_api.GnaviRestaurantAPI(url, keyid)

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
  data = api.execute()

  # show result
  if data is not None:
    api.showResult(base_api.GnaviRestaurantAPIBase.decode2JSON(data))
  else:
    print("APIアクセスに失敗しました。")