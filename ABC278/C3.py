# -*- coding: utf-8 -*-
# ACx17

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

follow={}
for ii in range(Q):
    if dat[ii][0] == 1:
        if not dat[ii][1] in follow:
            follow[dat[ii][1]]=set()
            follow[dat[ii][1]].add(dat[ii][2])
            dprint('follow:add',follow)
        elif not dat[ii][2] in follow[dat[ii][1]]:
            follow[dat[ii][1]].add(dat[ii][2])
            dprint('follow:add',follow)
    elif dat[ii][0] == 2:
        if dat[ii][1] in follow:
            if dat[ii][2] in follow[dat[ii][1]]:
                follow[dat[ii][1]].remove(dat[ii][2])
                dprint('follow:del',follow)
    elif dat[ii][0] == 3:
        dprint('dat[ii]',dat[ii])
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
