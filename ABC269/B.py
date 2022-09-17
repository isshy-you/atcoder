# -*- coding: utf-8 -*-
# ACx28

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

S=[]
for ii in range(10):
    s = input()
    S.append(s)

if DEBUG : print('input=',S)

A=0
B=0
C=0
D=0
for ii in range(10): # ii : 行 下
    for jj in range(10): # jj : 列　右
        if DEBUG : print(ii,jj,S[ii][jj])
        if S[ii][jj]=='#' and A==0:
            A=ii+1
            if DEBUG:print('###A=',A)
        if S[ii][jj]=='#' and C==0:
            C=jj+1
            if DEBUG:print('###C=',C)
        if S[ii][jj]=='#' and A!=0:
            B=ii+1
            if DEBUG:print('###B=',B)
        if S[ii][jj]=='#' and B!=0:
            D=jj+1
            if DEBUG:print('###D=',D)

print(A,B)
print(C,D)

