# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題3.
各行の１列目だけを抜き出したものをcol1.txtに、
２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ
の解答。
"""

filename = "13tokyo\\13TOKYO.CSV"
f = open(filename, "r")
fcol1 = open("basic_output\\col1.txt", "w")
fcol2 = open("basic_output\\col2.txt", "w")

for s in f:
    #print(s)
    itemList = s[:-1].split(',')
    print(itemList)
    fcol1.writelines(itemList[0]+"\n")
    fcol2.writelines(itemList[1]+"\n")

fcol1.close()
fcol2.close()
f.close()