# -*- coding: utf-8 -*-
# ACx6 TLEx15

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
DEBUG=True

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

inp = input_list()
N = inp[0]
M = inp[1]
K = inp[2]
dprintn('N',N)
dprint('M',M)
dprint('K',K)

inp = input_list()
A = inp
dprint('A',A)

ans = []
for ii in range(N-M+1):
    B = sorted(A[ii:ii+M])
    dprint('B',B)
    ans.append(sum(B[:K]))

print(*ans)