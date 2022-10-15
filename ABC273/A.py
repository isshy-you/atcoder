# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# 2次元リスト型標準入力
def input_list_2d(x,y):
    dat=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

def func(n):
    if DEBUG : print(n)
    if n==0:
        f = 1
    elif n>0 and n<=10:
        f = n*func(n-1)
    else:
        f=1
    return(f)

N = int(input())

if DEBUG : dprint('N',N)

print(func(N))


