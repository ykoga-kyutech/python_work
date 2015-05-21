# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import gnavi_entity_base as base

class GnaviRestaurantEntity(base.GnaviEntity):
    def __init__(self):
        super(GnaviRestaurantEntity, self).__init__()
        self.name                 = list()
        self.url                  = list()
        self.shop_image_url       = list()
        self.access_line          = list()

    def setEntity(self, json_data):

        # レストランデータ取得
        for rest in json_data["rest"] :
          name                 = ""
          url                  = ""
          shop_image_url       = ""
          access_line          = ""

          # 店舗名
          if "name" in rest and self.is_str( rest["name"] ) :
            name = u"{0}".format( rest["name"] )
          self.name.append( name )

          # 店舗URL
          if "url" in rest and self.is_str( rest["url"] ) :
            url = rest["url"]
          self.url.append( url )
          # 店舗画像URL
          if "image_url" in rest :
            access = rest["image_url"]
            if "shop_image1" in access and self.is_str( access["shop_image1"] ) :
              shop_image_url = u"{0}".format( access["shop_image1"] )
          self.shop_image_url.append( shop_image_url )

          if "access" in rest :
            access = rest["access"]
            # 最寄の路線
            if "line" in access and self.is_str( access["line"] ) :
              access_line = u"{0}".format( access["line"] )
            self.access_line.append(access_line)
