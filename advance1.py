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
import gnavi_restaurant_api as g_api
import gnavi_restaurant_api_base as base_api
import yaml

if __name__ == '__main__':

  # APIアクセスキーを含む設定ファイル
  setting_file = "advance_settings.yaml"
  # エンドポイントURL
  url = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"

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

  # 店舗名をコマンドライン引数から貰う
  if len(sys.argv) == 2:
    name = sys.argv[1]
  else:
    print("Example: python advance1.py 居酒屋")
    sys.exit(0)

  # ぐるなびレストランAPIアクセス用
  api = g_api.GnaviRestaurantAPI(url, keyid)

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
    api.showResult(base_api.GnaviRestaurantAPIBase.decode2JSON(result))
  else:
    print("APIアクセスに失敗しました。")