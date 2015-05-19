# -*- coding: utf-8 -*-
__author__ = 'tie304184'

"""
問題4. 3で作ったcol1.txtとcol2.txtを結合し，
元のタブ区切りテキストを復元せよ
の解答。
"""

# filenames
fname_col1_input = "basic_output\\col1.txt"
fname_col2_input = "basic_output\\col2.txt"
fname_output = "basic_output\\basic4_output.csv"

with open(fname_col1_input, "r") as fin_col1:
    with open(fname_col2_input, "r") as fin_col2:
        with open(fname_output, "w") as fout:
            # write col1 & col2 to the output file
            for i,j in zip(fin_col1, fin_col2):
                i = str(i).replace("\n","")
                fout.write(i+", "+j)