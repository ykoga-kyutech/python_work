__author__ = 'tie304184'
# -*- coding: utf-8 -*-

"""
応用問題3.
3. コマンドラインから都道府県番号も受け取れるようにせよ
(番号の頭0は不要。また、都道府県を指定するかは任意とする)
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
url_rest = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
url_pref = "http://api.gnavi.co.jp/ver2/PrefSearchAPI/"
# 店舗名をコマンドライン引数から貰う
pref = str(sys.argv[1])

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
# 都道府県コードクエリ
query_pref = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     )
]

# レストランクエリ
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "pref",  pref  )
  #,("name", "tokyo")
]

# URL生成
data = urllib.parse.urlencode( query_pref )
url = url_pref + '?'+data
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
data = json.loads( result.read().decode('utf-8') )#readall?
print(data)

# エラーの場合
if "error" in data :
  if "message" in data :
    #print("{0}".format( data["message"] ))
    print(data["message"])
  else :
    print("データ取得に失敗しました。")
  sys.exit()

# 都道府県コード取得
code_list = list()
pref_code = []
for pref in data["pref"] :
  #print(rest)
  # 店舗番号
  if "pref_code" in pref :
    pref_code.append(pref["pref_code"])
#print(pref_code)

# get pref code
idx = pref_code.index(pref)
pref = str(pref_code[idx])
print(pref)

#==============================================
# ↑本日の実装はここまで↑
#==============================================

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
  if "name" in rest and is_str( rest["name"] ) :
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

# 出力件数を表示して終了
print("----")
print("{0}件出力しました。".format( disp_count ))
sys.exit()