# -*- coding: utf-8 -*-
# ACx32

import sys
import math

sys.setrecursionlimit(1000000)

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

S = sys.stdin.readline()
T = sys.stdin.readline()

DEBUG=0

if DEBUG==1:
    print('S:',S[:-1],len(S)-1)
    print('T:',T[:-1],len(T)-1)
lens=len(S)-1
lent=len(T)-1
if lens>lent: # TはS以上の文字数であること
    if DEBUG==1:print('len(S)>len(T)')
    print('No')
    sys.exit()
elif S[0]!=T[0]: #最初1文字が同じであること
    if DEBUG==1:print('S[0]!=T[0]')
    print('No')
    sys.exit()
elif S[1]!=T[1]: #最初の2文字が同じであること
    if DEBUG==1:print('S[1]!=T[1]')
    print('No')
    sys.exit()
else:
    flag = 0
    sp = 2 #2つ目から開始
    tp = 2
    while (sp <= lens) and (tp < lent):
        if DEBUG==1:print('sp,tp,S,P',sp,tp,S[sp],T[tp])
        #Sの1つ前と2つ前が同じ文字ならフラグを立てる
        if S[sp-1]==S[sp-2]:
            flag = 1
            if DEBUG==1:print('flagON')
        else:
            flag = 0
            if DEBUG==1:print('flagOFF')
        # SとPのそれぞれのポインタの文字が不一致で
        # Pが直前と同じ文字で
        # 　flag=1ならTのポインタだけを進める(Sに文字挿入)
        if S[sp]!=T[tp]: #不一致なら
            if DEBUG==1:print('comp',S[sp],T[tp])
            if T[tp]==T[tp-1]:
                if flag==1:
                    if DEBUG==1:print('tp++')
                    tp=tp+1
                else: #同じ文字が続いてなかったらNo
                    if DEBUG==1:print('flag=0')
                    print('No')
                    sys.exit()
            else:
                if DEBUG==1:print('TP[tp]!=TP[tp-1]')
                print('No')
                sys.exit()
        # SとPのそれぞれのポインタの文字が一致すれば、
        # 　SがPを追い越さなければ
        # 　　SとPのポインタを進める。
        #   SがPを追い越すのならNo
        # 　Sが最後の文字ならYes
        else: # 一致なら
            if (sp < lens): # spは最後じゃない
                if DEBUG==1:print('sp++,tp++')
                sp = sp + 1
                tp = tp + 1
            else:# Sが最後の文字なら
                if tp==lent-1: # Tが最後ならYES
                    if DEBUG==1:print('last S')
                    print('Yes')
                    sys.exit()
                else:
                    if DEBUG==1:print('last S')
                    print('No')
                    sys.exit()

if DEBUG==1:print('sp,tp,S,P',sp,tp,S[sp],T[tp])
if (tp==lent):
    print('Yes')
else:
    print('No')

sys.exit()

#YES
# abbaac
# abbbbaaac

#YES
# aabbcc
# aabbccc

#NO
# aabbcc
# aabbccd