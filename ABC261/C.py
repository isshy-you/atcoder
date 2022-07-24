# -*- coding: utf-8 -*-
# use dict
# pypy3 ACx16
# pytho3.8 ACx16

import sys

DEBUG=False

N = int(input())

num=1
lib={}
for kk in range(N): # N文字入力
    text = sys.stdin.readline()[:-1] #文字列入力
    tmpstr='' # 空白文字で初期化
    for mm in range(len(text)): # 文字列の数値文字列化 文字列のままだとTLEx4 になる。
        tmpstr = tmpstr + str(ord(text[mm])-96).zfill(2) # a~zを01~26に変換
    code = int(tmpstr) #文字列の数値化
    if kk==0: # 最初だけ初期化
        lib.setdefault(code,0) # 辞書追加
        print(text)      # 結果表示
    else:
        # result = False
        # if (DEBUG):print('compare:',key,code,cnt)
        if code in lib: # 辞書にあれば（数値比較で比較１回となる）
            lib[code] = lib[code]+1 # 辞書カウントアップ
            print(text+'('+str(lib[code])+')') # 一致結果表示
            # if (DEBUG):print('update:',key,lib[code])
            # result = True
            # break # 一致したら辞書ループを終わる
        else:
            num = num + 1    # 辞書数増加
            lib[code]=0 # 辞書追加
            print(text) # 不一致結果表示
            # if (DEBUG):print('append:',key,lib[code])
sys.exit()
