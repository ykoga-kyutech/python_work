__author__ = 'tie304184'
# -*- coding: utf-8 -*-

"""
応用問題2.
1. コマンドライン引数から受け取った検索キーワードが日本語かどうか判定し、
それにより利用する検索APIをそれぞれレストラン検索API/多言語版レストラン
検索APIで切り替えよ。
なお、条件により対応するAPIの数は今後増えていくということを考慮した設計にすること
の解答。
"""
import sys
import urllib
import urllib.request
import urllib.parse
import json

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ): # or isinstance( data, unicode )
    return True
  else :
    return False

####
# 初期値設定
####
# APIアクセスキー
keyid = "b05b70882f1fca7ba0758afcba03a146"
# エンドポイントURL
urlname_restsearch = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
urlname_bilin_restsearch = "http://api.gnavi.co.jp/ver2/RestSearchAPI/"
url = ""
# 店舗名をコマンドライン引数から貰う
name = ""
try:
    name = sys.argv[1]
    name.encode('ascii', 'strict')
    url = urlname_bilin_restsearch # bilingual
    #print("aaaa")
except UnicodeEncodeError:
    url = urlname_restsearch       # japanese
    #print("bbbb")

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "name",  name  )
]

# URL生成
data = urllib.parse.urlencode( query )
url = url + '?'+data
print(url)

# API実行
try :
  result = urllib.request.urlopen(url)
except ValueError :
  print("APIアクセスに失敗しました。")
  sys.exit()

####
# 取得した結果を解析
####
data = json.loads( result.read().decode('utf-8') )
#print(data)

# エラーの場合
if "error" in data :
  if "message" in data :
    #print("{0}".format( data["message"] ))
    print(data["message"])
  else :
    print("データ取得に失敗しました。")
  sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data :
  total_hit_count = int(data["total_hit_count"])

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 :
  print("指定した内容ではヒットしませんでした。")
  sys.exit()

# レストランデータがなかったら終了
if not "rest" in data :
  print("レストランデータが見つからなかったため終了します。")
  sys.exit()

# ヒット件数表示
print("{0}件ヒットしました。".format( total_hit_count ))
print("----")

# 出力件数
disp_count = 0

if url.find(urlname_restsearch) == 0:
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
      if "id" in rest and is_str( rest["id"] ) :
        id = rest["id"]
      line.append( id )
      # 店舗名
      if "name" in rest and is_str( rest["name"] ):
        name = u"{0}".format( rest["name"] )
      line.append( name )
      if "access" in rest :
        access = rest["access"]
        # 最寄の路線
        if "line" in access and is_str( access["line"] ) :
          access_line = u"{0}".format( access["line"] )
        # 最寄の駅
        if "station" in access and is_str( access["station"] ) :
          access_station = u"{0}".format( access["station"] )
        # 最寄駅から店までの時間
        if "walk"    in access and is_str( access["walk"] ) :
          access_walk = u"{0}分".format( access["walk"] )
      line.extend( [ access_line, access_station, access_walk ] )
      # 店舗の小業態
      if "code" in rest and "category_name_s" in rest["code"] :
        for category_name_s in rest["code"]["category_name_s"] :
          if is_str( category_name_s ) :
            code_category_name_s.append( u"{0}".format( category_name_s ) )
      line.extend( code_category_name_s )
      # タブ区切りで出力
      print("\t".join( line ))
      disp_count += 1
else:
    # レストランデータ取得
    for rest in data["rest"] :
      line                 = []
      id                   = ""
      name            = ""
      access          = ""
      # 店舗番号
      if "id" in rest and is_str( rest["id"] ) :
        id = rest["id"]
      line.append( id )
      # 店舗名
      if "name" in rest and "name" in rest["name"] :
        print("aaaa")
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
sys.exit()