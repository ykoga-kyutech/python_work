プロジェクト名
==============
python_work


概要
==============
python課題の解答です（Basic & Extra）


ファイル名について
==============
* Python Basicの問題については、basic○.py(○は各問題番号)です。
* Python Basicの出力ファイルについては、basic_outputに出力されます。
* Python Extraの問題については、advance○.py(○は各問題番号)です。


実行前に用意すべきファイル
==============
* advance_settings.yamlという設定ファイルを作り、
そこに以下のように入力してください。APIキーは自分のものを入力してください

```yaml:advance_settings.yaml

# 例) keyid: aaaaaaaabbbbbbbbb00000000
keyid: あなたのAPIキー

```


実行環境
==============
OS: Windows 7
Python: 3.4.3


* Extra問題5のみ、jinja2のインストールが必要です（HTMLのテンプレートモジュール）

```bash

pip install jinja2

```


実行
==============
例）Python Basic問題１の実行

```bash

$ python basic1.py

```

例）Python Extar問題１の実行

```bash

$ python advance1.py 居酒屋

```

その他、コマンドライン引数は実行してみて表示される実行例に従ってください。
