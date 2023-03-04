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
K = inp[1]
dprintn('N',N)
dprint('K',K)

ss = []
for ii in range(N):
    inp = input()
    if ii < K :
        # S = inp
        S = inp[:-1]
        lenS = len(S)
        s = list(S)
        ss.append(s)
        dprintn('len(S)',lenS)
        dprint('s',s)

dprint('ss',ss)

ss.sort()
dprint('ss',ss)

for ii in range(K):
    print(''.join(ss[ii]))
