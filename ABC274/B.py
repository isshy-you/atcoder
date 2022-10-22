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
        values = input()
        # if len(values)==x:
        dat.append(values)
    return(dat)

H,W = input_list()
dat = input_list_2d(W,H)


dprint('H',H)
dprint('W',W)

dprint('dat',dat)

ans = ''
for ii in range(W):
    count = 0
    for jj in range(H):
        if dat[jj][ii]=='#':
            count = count + 1
    ans += str(count)+' '

print(ans)
