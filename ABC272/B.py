# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

# S = input()
N,M = input_list()
tmp=0
K=[]
X=[]
for ii in range(M):
    tmp = input_list()
    K.append(tmp[0])
    X.append(tmp[1:])

if DEBUG : print('N=',N)
if DEBUG : print('M=',M)
if DEBUG : print('K=',K)
if DEBUG : print('X=',X)

flag = [[0]*(N) for i in range(N)]
for ii in range(N):
    for jj in range(N):
        if ii>=jj:flag[ii][jj]=1

for mm in range(M):
    X[mm].sort()
    for kk in range(K[mm]):
        for jj in range(kk+1,K[mm],1):
            flag[X[mm][kk]-1][X[mm][jj]-1]=1

if DEBUG : print('flag=',flag)

for ii in range(N):
    for jj in range(N):
        if flag[ii][jj]==0:
            print('No')
            exit()

print('Yes')