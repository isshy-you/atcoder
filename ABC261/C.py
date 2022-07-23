# -*- coding: utf-8 -*-
# pypy3 TLEx2 ACx14 ... use this
# pytho3.8 TLEx5 ACx11

import sys

DEBUG=False

N = int(input())

num=1
lib=[]
cnt=[]
for kk in range(N): # N文字入力
    text = sys.stdin.readline()[:-1] #文字列入力
    tmpstr='' # 空白文字で初期化
    for mm in range(len(text)): # 文字列の数値文字列化 文字列のままだとTLEx4 になる。
        tmpstr = tmpstr + str(ord(text[mm])-96).zfill(2) # a~zを01~26に変換
    code = int(tmpstr) #文字列の数値化
    if kk==0: # 最初だけ初期化
        lib.append(code) # 辞書追加
        cnt.append(0)    # 辞書カウンタ0
        print(text)      # 結果表示
    else:
        result = False
        for nn in range(num): # 辞書をなめる
            if (DEBUG):print('compare:',nn,lib[nn],code)
            if lib[nn]==code: # 辞書にあれば（数値比較で比較１回となる）
                cnt[nn]= cnt[nn] + 1 # 辞書カウントアップ
                print(text+'('+str(cnt[nn])+')') # 一致結果表示
                if (DEBUG):print('update:',lib,cnt)
                result = True
                break # 一致したら辞書ループを終わる
            # 辞書になかったら
        if not result:
            num = num + 1    # 辞書数増加
            lib.append(code) # 辞書追加
            cnt.append(0)    # 辞書カウンタ0
            print(text) # 不一致結果表示
            if (DEBUG):print('append:',lib,cnt)
sys.exit()
