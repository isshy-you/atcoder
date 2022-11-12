# -*- coding: utf-8 -*-

import sys
import math

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

N,X = input().split()
P = input_list()
dprint('N',N)
dprint('X',X)
dprint('P',P)

for ii in range(int(N)):
    if int(X) == P[ii]:
        print(ii+1)
        exit()
