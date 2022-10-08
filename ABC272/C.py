# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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
A = input_list()

if DEBUG : print(A)

# 偶数は偶数＋偶数か奇数＋奇数
# 最大値を求めるから、最大の偶数か奇数になる
# 偶数 2n
# 奇数 2m+1
# 最大から偶数と偶数または奇数と奇数を探せばよい。

A.sort(reverse=True)
if DEBUG: print(A)

gusu1=-1
gusu2=-1
kisu1=-1
kisu2=-1
max = -1
for ii in range(N):
    if A[ii] % 2 == 0:
        if gusu1 == -1:
            gusu1=A[ii]
            if DEBUG: print('gusu1=',gusu1)
        else:
            gusu2=A[ii]
            if max < gusu1+gusu2:
                max = gusu1+gusu2
    elif A[ii] % 2 == 1:
        if kisu1 == -1:
            kisu1=A[ii]
            if DEBUG: print('kisu1=',kisu1)
        else:
            kisu2=A[ii]
            if max < kisu1+kisu2:
                max = kisu1+kisu2


print(max)

'''
5
1 2 7 4 0

'''