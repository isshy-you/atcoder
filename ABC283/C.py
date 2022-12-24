# -*- coding: utf-8 -*-

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
# DEBUG=True

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

cnt = 0
ii = 0
while (ii < lenS):
    if s[ii] != '0':
        cnt = cnt + 1
        ii = ii + 1
    elif s[ii] == '0' and ii == lenS-1:
        cnt = cnt + 1
        ii = ii + 1
    elif s[ii] == '0' and s[ii+1] == '0':
        cnt = cnt + 1
        ii = ii + 2
    else:
        cnt = cnt + 1
        ii = ii + 1
    dprintn('ii',ii)
    dprint('cnt',cnt)

print(cnt)

