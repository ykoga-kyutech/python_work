# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import gnavi_restaurant_api_base as base
import json

class GnaviBilingualRestaurantAPI(base.GnaviRestaurantAPIBase):

  def __init__(self, url, apikey):
    super(GnaviBilingualRestaurantAPI, self).__init__(url, apikey)

  def showResult(self, result):

    # 取得した結果を解析
    data = json.loads( result.read().decode('utf-8') )

    # エラーの場合
    if "error" in data :
      if "message" in data :
        print(data["message"])
      else :
        print("データ取得に失敗しました。")
        return

    # ヒット件数取得
    total_hit_count = None
    if "total_hit_count" in data :
      total_hit_count = int(data["total_hit_count"])

    # ヒット件数が0以下、または、ヒット件数がなかったら終了
    if total_hit_count is None or total_hit_count <= 0 :
      print("指定した内容ではヒットしませんでした。")
      return

    # レストランデータがなかったら終了
    if not "rest" in data :
      print("レストランデータが見つからなかったため終了します。")
      return

    # ヒット件数表示
    print("{0}件ヒットしました。".format( total_hit_count ))
    print("----")

    # 出力件数
    disp_count = 0

    # レストランデータ取得
    for rest in data["rest"] :
      line                 = []
      id                   = ""
      name            = ""
      access          = ""
      # 店舗番号
      if "id" in rest and self.is_str( rest["id"] ) :
        id = rest["id"]
      line.append( id )
      # 店舗名
      if "name" in rest and "name" in rest["name"] :
        #name = u"{0}".format( rest["name"]["name_sub"] )
        name = rest["name"]["name"]
        #print(name)
      line.append( name )
      # アクセス
      if "access" in rest :
        access = rest["access"]
      line.extend(access)
      # タブ区切りで出力
      print("\t".join( line ))
      disp_count += 1

    # 出力件数を表示して終了
    print("----")
    print("{0}件出力しました。".format( disp_count ))
