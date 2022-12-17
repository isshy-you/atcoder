# -*- coding: utf-8 -*-
# Incomplete

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

def printNo():
    print('No')

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
DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N)
dprint('M',M)

dat=[]
dat = input_list_2d(M) # dat[row][column]
dprint('dat',dat)

A=set()
B=set()
a=[]
b=[]
lnk = [[]*(N+1) for i in range(N+1)]

for ii in range(M):
    if ((dat[ii][0] in A) and (dat[ii][1] in A)) or (dat[ii][0] in B) and (dat[ii][1] in B):
        dprint('ii',ii)
        dprint('A',A)
        dprint('B',B)
        if DEBUG:
            dprint('a',a)
            dprint('b',b)
        print(0)
        exit()
    elif (dat[ii][0] in A):
        A.add(dat[ii][0])
        B.add(dat[ii][1])
        if DEBUG:
            a.append(dat[ii][0])
            b.append(dat[ii][1])
        lnk[dat[ii][0]-1].append(dat[ii][1])
    elif (dat[ii][0] in B):
        B.add(dat[ii][0])
        A.add(dat[ii][1])
        if DEBUG:
            a.append(dat[ii][0])
            b.append(dat[ii][1])
        lnk[dat[ii][0]-1].append(dat[ii][1])
    elif (not dat[ii][0] in A) or (not dat[ii][1] in B):
        A.add(dat[ii][0])
        B.add(dat[ii][1])
        if DEBUG:
            a.append(dat[ii][0])
            b.append(dat[ii][1])
        lnk[dat[ii][0]-1].append(dat[ii][1])
    elif (not dat[ii][0] in B) or (not dat[ii][1] in A):
        A.add(dat[ii][1])
        B.add(dat[ii][0])
        if DEBUG:
            a.append(dat[ii][1])
            b.append(dat[ii][0])
        lnk[dat[ii][0]-1].append(dat[ii][1])

dprint('A',A)
dprint('B',B)
if DEBUG:
    dprint('a',a)
    dprint('b',b)
dprint('lnk',lnk)

cnt = 0
for ii in A:
    zz = set(lnk[ii-1])^set(range(N))
    for jj in zz:
        dprintn('ii',ii)
        dprintn('jj+1',jj+1)
        dprint('lnkii',lnk[ii-1])
        if ii in A:
            if jj in B:
                cnt = cnt+1

print(cnt)