# -*- coding: utf-8 -*-
# ACx53, TLEx14

import sys
import math

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')
    exit()

def printNo():
    print('No')
    exit()

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(lines):
    dat=[]
    for yy in range(lines):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

DEBUG=False
# DEBUG=True

inp = input_list()
N = inp[0]
X = inp[1]

dat=[]
dat = input_list_2d(N) # dat[row][column]
# dprint('dat',dat)

dat.sort()

dprintn('N',N)
dprint('X',X)
dprint('dat',dat)

def funca(nokori,ii):
    maisu = nokori//dat[ii][0]
    if maisu > dat[ii][1]:
        maisu = dat[ii][1]
    for jj in range(maisu+1):
        val = nokori - dat[ii][0] * (maisu-jj)
        dprintn('dat[ii][0]',dat[ii][0])
        dprintn('maisu',maisu-jj)
        dprint('val',val)
        if val == 0:
            return(True)
        elif ii==0:
            return(False)
        else:
            m = funca(val,ii-1)
            if m : return(m)

sum = []
for ii in range(N):
    if ii == 0:
        sum.append(dat[ii][0]*dat[ii][1])
    else:
        sum.append(dat[ii][0]*dat[ii][1]+sum[ii-1])

for ii in range(N):
    m = funca(X,N-1-ii)
    if m :
        printYes()
printNo()

'''
3 18
5 2
3 1
2 4

'''