# -*- coding: utf-8 -*-
# ACx14
# TLEx16
# 全探索はやはりTLE。

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

N=int(input())
A=[]
B=[]
C=[]
IN = input().split()
length = 0
for ii in range(N):
    A.append([IN[ii],int(IN[ii])])

A.sort(reverse=True)

if DEBUG : print('input:',N,A,length)

maxval = 0
maxid = 0,0,0
ans = ''
num = 0

ia=-1
ib=-1
ic=-1
for ia in range(N):
    tmpa = A[ia][0]
    for ib in range(N):
        if ib != ia and ib != ic:
            tmpb = A[ib][0]
            for ic in range(N):
                if ic != ia and ic != ib:
                    tmpc = A[ic][0]
                    if DEBUG:print(ia,ib,ic,tmpa,tmpb,tmpc)
                    if maxval < int(tmpa+tmpb+tmpc):
                        maxval = int(tmpa+tmpb+tmpc)
                        maxid = ia,ib,ic

a,b,c = maxid
print(A[a][0]+A[b][0]+A[c][0])
exit()
