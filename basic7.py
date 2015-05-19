# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題7.
１コラム目の文字列を集計して表示せよ(文字列/カウントを表示）
の解答。
"""
import sys
from collections import Counter

fname_input = "13tokyo\\13TOKYO.CSV"

col1 = list()
with open(fname_input, "r") as fin:
    for m in fin:
        col1.append(m.split(",")[0])
    counter = Counter(col1)
    for m, count in counter.most_common():
        result = m+"/"+str(count)
        print(result)