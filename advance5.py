# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題5.
店舗名・リンク・画像・応援の最低4点を含むhtmlページ
(上位3件のみで可)を作成し、ブラウザでページを開け
参考URL-> http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python
(ただしPython2のようなので注意)
の解答。
"""

import sys
import grounabi_ouen_api as go_api
import gnavi_ouen_entity as oe
import webbrowser

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"
  # エンドポイントURL
  url_ouen = "http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/"
  # 店舗名をコマンドライン引数から貰う
  if len(sys.argv) == 2 :
    name = sys.argv[1]
  else:
    print("Example: python advance5.py 居酒屋")
    sys.exit(0)

  # ぐるなび口コミAPIアクセス用
  api_ouen = go_api.GrounabiOuenAPI(url_ouen, keyid)

  query_ouen = [
    ( "format", "json" ),
    ( "keyid", keyid ),
    ( "shop_name", name)
  ]

  # set query
  api_ouen.setQuery(query_ouen)

  # get result
  result_ouen = api_ouen.execute()

  data_ouen = api_ouen.decode2JSON(result_ouen)
  if result_ouen is not None:
    api_ouen.showResult(data_ouen)
  else:
    print("APIアクセスに失敗しました。")

  entity = oe.GNaviOuenEntity()
  entity.setEntity(data_ouen)

  f = open('advance5_result.html','w')

  # header
  message = """<html>
  <head>
  <title>JSONのデータを表示する</title>
  <script type="text/javascript">
   document.write("<p> JavaScriptテスト</p>")
  </script>
  </head>
  """

  # body
  message +="""
  <body>
  <h1>検索結果情報</h1>
  <p>ああああ</p>
  """
  image_w  = 150
  image_h = 60

  # write name, link, image, ouen
  for name, shop_url, image_url, comment in zip(entity.name, entity.shop_url, entity.image_url, entity.comment):
        print(name, shop_url, image_url, comment)
        #message += "<p>店舗名: "++"</p>"
        message += "<a href="+image_url+">"+name+"</a></br>"
        message += "<img src="+shop_url+" width="+str(image_w)+" height="+str(image_h)+"></br>"
  message +="""
  </body>
  </html>"""

  f.write(message)
  f.close()
  webbrowser.open_new_tab('advance5_result.html')