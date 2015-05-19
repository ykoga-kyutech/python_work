# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題6.
自然数Nをコマンドライン引数にとり、入力のうち末尾のN行だけ出力せよ
の解答。
"""
import sys

# filenames
fname_input = "13tokyo\\13TOKYO.CSV"
fname_output = "basic_output\\basic6_output.csv"

# get input number
if len(sys.argv) == 2:
    input = int(sys.argv[1])
else:
    print("Example: ")
    print("python basic6 2")
    sys.exit(0)

with open(fname_input, "r") as fin:
    with open(fname_output, "w") as fout:
        all = fin.readlines()
        tail = all[-input:]
        fout.writelines(tail)