# -*- coding: utf-8 -*-
"""
問題1.
ファイルの行数をカウントせよ
の解答。
"""

filename = "13tokyo\\13TOKYO.CSV"
f = open(filename, "r")
strList = f.readlines()
print("row length: ", len(strList))
f.close()