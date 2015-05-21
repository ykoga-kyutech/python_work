# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
応用問題5.
店舗名・リンク・画像・応援の最低4点を含むhtmlページ
(上位3件のみで可)を作成し、ブラウザでページを開け
参考URL-> http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python
(ただしPython2のようなので注意)
の解答。

jinja2モジュールのインストールが必要。
$ pip install jinja2
"""

import sys
import grounabi_ouen_api as go_api
import gnavi_ouen_entity as oe
import webbrowser
from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':

  # APIアクセスキー
  keyid = "b05b70882f1fca7ba0758afcba03a146"
  # エンドポイントURL
  url_ouen = "http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/"
  # 出力HTML
  output_html = "advance5.html"
  # 出力HTMLのテンプレート
  output_template = "advance5_template.html"

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

  # クエリをセット
  api_ouen.setQuery(query_ouen)

  # API通信、結果を取得
  result_ouen = api_ouen.execute()

  # デコード
  data_ouen = api_ouen.decode2JSON(result_ouen)

  # 結果出力
  if result_ouen is not None:
    #api_ouen.showResult(data_ouen)

    # TODO エンティティはAPIがもつべき?
    entity = oe.GNaviOuenEntity()
    entity.setEntity(data_ouen)

    # テンプレートファイルを指定
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tpl = env.get_template(output_template)

    # テンプレートへ挿入するデータの作成
    title = name+"の検索結果"
    shop_list = []
    for name, shop_url, image_url, comment in zip(entity.name, entity.shop_url, entity.image_url, entity.comment):
          shop_list.append({'name':name, 'comment':comment, 'shop_url':shop_url, 'image':image_url})

    # テンプレートへの挿入
    html = tpl.render({'title':title, 'shop_list':shop_list})

    # ファイルへの書き込み
    tmpfile = open(output_html, 'w') #書き込みモードで開く
    tmpfile.write(html) #.encode('utf-8')
    tmpfile.close()

    # ページを開く
    webbrowser.open_new_tab(output_html)

    print("結果が別ウィンドウで表示されました")
  else:
    print("APIアクセスに失敗しました。")