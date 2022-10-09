# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
DEBUG=True

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

S = input()
lenS = len(S)
N = int(input())
N,M = input_list()
dat=[]
dat = input_list_2d(N,M)

if DEBUG : print(dat)