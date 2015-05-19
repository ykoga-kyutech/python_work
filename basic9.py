# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題9.
各行を２コラム目、１コラム目の優先順位で辞書の逆順にソートして出力せよ
の解答。
"""
import sys

def camma_plus(s):
    """
    Add "," to the given string on last position
    :param s:
    :return:
    """
    return s+","

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

        # get each line, and write
        for line in sortlist:
            new_line = map(camma_plus, line[:-1]) # don't add "," to the last element
            fout.writelines(new_line)
            fout.write(line[-1])