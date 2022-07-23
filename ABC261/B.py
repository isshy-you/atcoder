# -*- coding: utf-8 -*-
# 

import sys
import math

sys.setrecursionlimit(1000000)

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

DEBUG=False
# DEBUG=True

N = int(input())

A=[]
for nn in range(N):
    tmp = input().split()[0]
    val = []
    for kk in range(N):
        if tmp[kk]=='W':
            val.append(1)
        elif tmp[kk]=='L':
            val.append(-1)
        else:
            val.append(0)
    A.append(val)

if (DEBUG):
    for ii in range(N):
        for jj in range(N):
            print(ii,jj,A[ii][jj])

for ii in range(N):
    for jj in range(N):
        if A[ii][jj] != (-A[jj][ii]):
            print('incorrect')
            sys.exit()

print('correct')
sys.exit()
