# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

cnt = 0
if lenS == 8:
    if s[0] <= 'Z' and S[0] >= 'A':
        if s[1] <= '9' and S[1] >= '1':
            if s[7] <= 'Z' and S[7] >= 'A':
                for ii in range(2,7,1):
                    if s[ii] <= '9' and S[ii] >= '0':
                        cnt = cnt + 1

if cnt == 5 : printYes()
else : printNo()