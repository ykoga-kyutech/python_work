__author__ = 'tie304184'

"""
問題10.
各行の２コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べよ。ただし、
3で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ
の解答。
"""
import sys
from collections import Counter

# filenames
fname_input = "basic_output\\col2.txt"
fname_output = "basic_output\\basic10_output.csv"

col1 = list()
with open(fname_input, "r") as fin:
    with open(fname_output, "w") as fout:
        for m in fin:
            col1.append(m)
        counter = Counter(col1)
        for m, count in counter.most_common():
            result = m[:-1]+", "+str(count)+"\n"
            fout.write(result)