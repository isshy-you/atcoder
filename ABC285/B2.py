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

inp = int(input())
N = inp
dprint('N',N)

inp = input()
S = inp[:-1]

for ii in range(1,N,1):
    cnt = 0
    jj = 1
    while(True):
        if S[jj-1] != S[jj+ii-1]:
            cnt = cnt + 1
        else:
            break
        jj = jj + 1
        if (jj+ii) > N:
            break
    print(cnt)
