# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題8.
各行を２コラム目の辞書順にソートして出力せよ
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
fname_output = "basic_output\\basic8_output.csv"

lines = list()
with open(fname_input, "r") as fin:
    with open(fname_output, "w") as fout:
        for line in fin:
            lines.append(line.split(","))
        # sort
        sortlist = sorted(lines, key=lambda x:x[1])

        # get each line, and write it to the file
        for line in sortlist:
            new_line = map(camma_plus, line[:-1]) # don't add "," to the last element
            fout.writelines(new_line)
            fout.write(line[-1])