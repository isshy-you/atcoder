# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc277/tasks/abc277_c
# ACx8 TLEx10

import sys
import math
import copy

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

input = sys.stdin.readline

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(x,y):
    dat=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

N = int(input())

dprint('N',N)

RADDER = []
for ii in range(N):
    a,b = input_list()
    RADDER.append((a,b))
    RADDER.append((b,a))

dprint('RADDER',RADDER)
floor = [1] # スタートは１階
ptr = 0
while(True):
    dprint('ptr',ptr)
    dprint('now',floor[ptr]) # 探索する階
    delptr = []
    for ii,val in enumerate(RADDER): # 階段全探索
        if val[0] == floor[ptr] : # 階段あり
            dprint('floor[ptr]',floor[ptr])
            dprint('RADDER[ii]',RADDER[ii])
            if not val[1] in floor: # 階段の先は行ったことがない階なら
                floor.append(val[1]) # 行ったことのある階として記録
                dprint('add floor',floor)
                delptr.append(ii) # 使った階段を削除メモ
                dprint('del radder',RADDER[ii])
            else: # 階段の先は行ったことがある階なら
                delptr.append(ii) # 使った階段を削除メモ
                dprint('del radder',RADDER[ii])
    for ii,jj in enumerate(delptr): # 使った階段を削除
        del RADDER[jj-ii]
    dprint('RADDER',RADDER)
    ptr = ptr + 1 # 次の行ったことのある階をチェック
    if len(floor) <= ptr: # 行ったことのある階がなくなったら終わる。
        print(max(floor))
        exit()
