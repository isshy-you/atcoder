# -*- coding: utf-8 -*-
# ACx11
# TLEx19

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

def search(ptr):
    num=0
    for ii in range(N): # iiは人
        for jj in range(-1,2,1): # 左右の料理
            kk = ii+jj+ptr # 回転したときの料理位置
            if kk>=N:
                kk = kk - N
            elif kk<0:
                kk = N-1
            if ii==p[kk]: # 人と料理がマッチ
                if DEBUG : print('ii,kk,p[kk]=',ii,kk,p[kk])
                num = num + 1
                break # マッチしたら次の人のチェック終了
    if DEBUG : print('num=',num)
    return(num)


N = int(input())
P = input().split()

if DEBUG : print('input=',N)
if DEBUG : print('input=',P)

p=[]
for ii in range(N):
    p.append(int(P[ii]))

if DEBUG : print('input=',p)

max = 0
for ii in range(N):
    tmp = search(ii)
    if tmp > max:
        max = tmp

if tmp>N:
    max = N

print(max)
