# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import grounabi_restaurant_api_base as base
import json

class GrounabiRestaurantAPI(base.GrounabiRestaurantAPIBase):

  def __init__(self, url, apikey):
    super(GrounabiRestaurantAPI, self).__init__(url, apikey)

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
      name                 = ""
      access_line          = ""
      access_station       = ""
      access_walk          = ""
      code_category_name_s = []
      # 店舗番号
      if "id" in rest and self.is_str( rest["id"] ) :
        id = rest["id"]
      line.append( id )
      # 店舗名
      if "name" in rest and self.is_str( rest["name"] ) :
        name = u"{0}".format( rest["name"] )
      line.append( name )
      if "access" in rest :
        access = rest["access"]
        # 最寄の路線
        if "line" in access and self.is_str( access["line"] ) :
          access_line = u"{0}".format( access["line"] )
        # 最寄の駅
        if "station" in access and self.is_str( access["station"] ) :
          access_station = u"{0}".format( access["station"] )
        # 最寄駅から店までの時間
        if "walk"    in access and self.is_str( access["walk"] ) :
          access_walk = u"{0}分".format( access["walk"] )
      line.extend( [ access_line, access_station, access_walk ] )
      # 店舗の小業態
      if "code" in rest and "category_name_s" in rest["code"] :
        for category_name_s in rest["code"]["category_name_s"] :
          if self.is_str( category_name_s ) :
            code_category_name_s.append( u"{0}".format( category_name_s ) )
      line.extend( code_category_name_s )
      # タブ区切りで出力
      print("\t".join( line ))
      disp_count += 1

    # 出力件数を表示して終了
    print("----")
    print("{0}件出力しました。".format( disp_count ))