# -*- coding: utf-8 -*-
# PyPy3
# ACx16, TLEx1

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

def myindex(l,x,default=-1):
    if x in l:
        return l.index(x)
    else:
        return default

N,Q = input_list()

dat=[]
dat = input_list_2d(N,Q)

# dprint('N',N)
# dprint('Q',Q)
# dprint('dat',dat) # dat[ii]=[T,A,B]

# follow = [[] for i in range(N)]
follow={}
# for ii in range(N):
#     follow[ii]=[]
# dprint('follow',follow)
for ii in range(Q):
    if dat[ii][0] == 1:
        if not dat[ii][1] in follow:
            follow[dat[ii][1]]=[dat[ii][2]]
            # dprint('follow:add',follow)
        elif not dat[ii][2] in follow[dat[ii][1]]:
            follow[dat[ii][1]].append(dat[ii][2])
            # follow.setdefault(dat[ii][1],dat[ii][2])
            # follow[dat[ii][1]].append(dat[ii][2])
            # dprint('follow:add',follow)
    elif dat[ii][0] == 2:
        # idx = follow[dat[ii][1]-1].index(dat[ii][2])
        if dat[ii][1] in follow:
            # dprint('follow[dat[ii][1]]',follow[dat[ii][1]])
            # dprint('dat[ii][2]',dat[ii][2])
            idx = myindex(follow[dat[ii][1]],dat[ii][2])
            # dprint('idx',idx)
            if idx >= 0:
                # dprint('follow:del',follow)
                del follow[dat[ii][1]][idx]
    elif dat[ii][0] == 3:
        # dprint('dat[ii]',dat[ii])
        # if DEBUG:
        #     if dat[ii][1] in follow:
        #         dprint('follow[dat[ii][1]]',follow[dat[ii][1]])
        #     if dat[ii][2] in follow:
        #         dprint('follow[dat[ii][2]]',follow[dat[ii][2]])
        if dat[ii][1] in follow and dat[ii][2] in follow:
            if dat[ii][1] in follow[dat[ii][2]] and dat[ii][2] in follow[dat[ii][1]]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
