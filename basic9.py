# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題9.
各行を２コラム目、１コラム目の優先順位で辞書の逆順にソートして出力せよ
の解答。
"""
import sys

# filenames
fname_input = "13tokyo\\13TOKYO.CSV"
fname_output = "basic_output\\basic9_output.csv"

lines = list()
with open(fname_input, "r") as fin:
    with open(fname_output, "w") as fout:
        for line in fin:
            lines.append(line.split(","))
        # sort
        sortlist = sorted(lines, key=lambda x:(x[1],x[0]), reverse=True)
        # write
        for line in sortlist:
            for str in line:
                fout.write(str+",") # TODO remove "," if the str is the last one