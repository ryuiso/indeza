# coding:utf-8
import os
#ディレクトリの変更
os.chdir(r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader")

#印刷コマンド
cmd = "AcroRd32.exe /t C:\Users\\atsushi\Desktop\hoge.pdf \"OKI MC860(PS)\" 133.16.39.25"
#コマンド確認
print cmd
#印刷開始
os.system(cmd)
