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
M = inp[1]
dprintn('N',N)
dprintn('M',M)

S = []
for ii in range(N):
    inp = int(input())
    tmp = inp - (inp//1000 * 1000)
    S.append(tmp)
dprintn('S',S)

T = []
for ii in range(M):
    inp = int(input())
    T.append(inp)
dprint('T',T)

cnt = 0
for ii in range(N):
    for jj in range(M):
        if S[ii] == T[jj]:
            cnt = cnt + 1
            break        

print(cnt)