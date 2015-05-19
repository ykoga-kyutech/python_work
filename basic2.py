# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題 2.
タブ１文字につきスペース１文字に置換せよ
の解答。
"""

filename = "13tokyo\\13TOKYO.CSV"
f = open(filename, "r")

for str in f:
    dst = str.replace('\t', ' ')
    print( str)

f.close()