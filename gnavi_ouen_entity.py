# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import gnavi_entity_base as base

class GNaviOuenEntity(base.GNaviEntity):
    def __init__(self):
        super(GNaviOuenEntity, self).__init__()
        self.name                 = list()
        self.shop_url             = list()
        self.image_url            = list()
        self.comment              = list()

    def setEntity(self, json_data):

        i = 0
        j = 0
        while j < 3:
            i += 1
            photo = json_data["response"]["{0}".format(i)]["photo"]
            name                 = ""
            shop_url             = ""
            image_url            = ""
            comment              = ""

            # 店舗名
            if "shop_name" in photo and self.is_str( photo["shop_name"] ) :
             name = photo["shop_name"]
            if name in self.name:
                continue
            self.name.append( name )


            # 店舗URL
            if "shop_url" in photo and self.is_str( photo["shop_url"] ) :
                shop_url = photo["shop_url"]
            self.shop_url.append( shop_url )

            # 店舗画像URL
            if "shop_url" in photo and self.is_str( photo["shop_url"] ) :
                image_url = photo["image_url"]["url_320"]
            self.image_url.append( image_url )

            # 口コミ
            if "comment" in photo and self.is_str( photo["comment"] ) :
                comment = photo["comment"]
            self.comment.append( comment )

            j += 1;