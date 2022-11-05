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

# 2次元配列の初期化
def init_2d_list(sizex,sizey,value):
    dat = [[value]*(sizex) for i in range(sizey)]
    # if DEBUG : print('dat=',dat)
    # if DEBUG : print('x y #')
    # for xx in range(sizex):
    #     for yy in range(sizey):
    #         if DEBUG : print(xx,yy,dat[yy][xx])
    return(dat)

N,M = input_list()
dat=[]
dat = input_list_2d(N,M)
dat.sort()

dprint('dat',dat)

ans = [[]*M for i in range(N)]
dprint('ans',ans)

for ii in range(M): # 10^5
    ans[dat[ii][0]-1].append(dat[ii][1])
    ans[dat[ii][1]-1].append(dat[ii][0])

for ii in range(N): # 10^5
    print(len(ans[ii]),('{:d} '*len(ans[ii])).format(*ans[ii]))
   
dprint('ans',ans)
