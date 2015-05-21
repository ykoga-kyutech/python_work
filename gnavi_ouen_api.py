# -*- coding: utf-8 -*-
__author__ = 'tie304184'

import gnavi_restaurant_api_base as base
import json
import asyncio
from asyncio.futures import Future
from functools import partial

class GnaviOuenAPI(base.GnaviRestaurantAPIBase):

  def __init__(self, url, apikey):
    super(GnaviOuenAPI, self).__init__(url, apikey)

  @asyncio.coroutine
  def showOuen(self, data, i):
    photo = data["response"]["{0}".format(i)]["photo"]
    line                 = []
    id                   = ""
    name                 = ""
    mname                = ""
    comment              = ""

    """
    # 店舗番号
    if "shop_id" in photo and self.is_str( photo["shop_id"] ) :
        id = photo["shop_id"]
    line.append( id )
   """

    # 店舗名
    if "shop_name" in photo and self.is_str( photo["shop_name"] ) :
     name = photo["shop_name"]
    line.append( name )

    # メニュー名
    if "menu_name" in photo and self.is_str( photo["menu_name"] ) :
        mname = photo["menu_name"]
    line.append( mname )

    # コメント
    if "comment" in photo and self.is_str( photo["comment"] ) :
      comment = photo["comment"]
    line.append( comment )

    # タブ区切りで出力
    print("\t".join( line ))

  @asyncio.coroutine
  def show_parallel(self, loop, data, disp_count):
    tasks = list()
    for i in range(disp_count):
        tasks.append(asyncio.Task(self.showOuen(data, i)))
    yield from asyncio.gather(*tasks)
    loop.stop()

  """
  @asyncio.coroutine
  def show_parallel(self, loop, data, disp_count):
    sentinel = asyncio.Future(loop = loop)

    tasks = list()
    for i in range(disp_count):
        tasks.append(asyncio.async(self.showOuen(data, i)))

    results = [None] * len(tasks)
    N = 0

    def _done_callback(i, f):
        nonlocal N
        results[i] = f._result
        N += 1
        if N == len(tasks):
            sentinel.set_result(results)

    for i, t in enumerate(tasks):
        t.add_done_callback(partial(_done_callback, i))

    yield from sentinel
    loop.stop()
  """

  def showResult(self, data):

    # 取得した結果を解析
    #data = json.loads( result.read().decode('utf-8') )
    #print(data)

    # エラーの場合
    if "error" in data :
      if "message" in data :
        print(data["message"])
      else :
        print("データ取得に失敗しました。")
        return

    # ヒット件数取得
    total_hit_count = None
    if "total_hit_count" in data["response"] :
      total_hit_count = int(data["response"]["total_hit_count"])

    #ページごとの件数を取得
    hit_per_page = None
    if "hit_per_page" in data["response"] :
        hit_per_page = data["response"]["hit_per_page"]

    # ヒット件数が0以下、または、ヒット件数がなかったら終了
    if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
      print("指定した内容ではヒットしませんでした。")
      return

    # ヒット件数表示
    print("{0}件ヒットしました。".format( total_hit_count ))
    print("----")

    # 出力件数
    disp_count = 3

    # 応援口コミデータ取得（並列で取得）
    loop = asyncio.get_event_loop()
    asyncio.async(self.show_parallel(loop, data, disp_count))
    loop.run_forever()
    loop.close()

    # 出力件数を表示して終了
    print("----")
    print("{0}件出力しました。".format( disp_count ))