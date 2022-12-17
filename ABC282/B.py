# -*- coding: utf-8 -*-
# AC

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False

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

def check(a,b):
    for jj in range(M):
        if a[jj]=='x' and b[jj]=='x':
            return(False)
    return(True)

# DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N) # N:i
dprint('M',M)  # M:j

S=[]
for ii in range(N):
    S.append(input()[:-1]) 
    
dprint('S',S)

cnt = 0
for ii in range(N):
    for kk in range(ii+1,N,1):
        chk = check(S[ii],S[kk])
        if chk :
            dprintn('ii',ii)
            dprint('kk',kk)
            cnt = cnt + 1

print(cnt)
