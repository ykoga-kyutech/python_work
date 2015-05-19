# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題8.
各行を２コラム目の辞書順にソートして出力せよ
の解答。
"""
import sys

# filenames
fname_input = "13tokyo\\13TOKYO.CSV"
fname_output = "basic_output\\basic8_output.csv"

lines = list()
with open(fname_input, "r") as fin:
    with open(fname_output, "w") as fout:
        for line in fin:
            lines.append(line.split(","))
        # sort
        sortlist = sorted(lines, key=lambda x:x[1])
        # write
        for line in sortlist:
            for str in line:
                line = str(line)
                fout.write(str+",") # TODO remove "," if the str is the last one