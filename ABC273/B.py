# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

def func(val,n):
    aa = (val + 10**n/2 ) // 10**n
    bb = aa * 10**n
    return(bb)

X,K = input_list()
if DEBUG : dprint('X',X)
if DEBUG : dprint('K',K)

tmp = X
for ii in range(K):
    tmp = func(tmp,ii+1)
    dprint('tmp',tmp)

print(int(tmp))