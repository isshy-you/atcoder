# -*- coding: utf-8 -*-
# ACx8 TLEx10

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

input = sys.stdin.readline

def dprint(str,val):
    if DEBUG : print(str,'=',val)

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

def updown(A,B,F,now,max):
    if DEBUG : print('now,max,RADDER=',now,max,F,len(F))
    for ii in [i for i, x in enumerate(F) if x == False]:
        if DEBUG : print('ii=',ii)
        if not F[ii]:
            if A[ii] == now:
                next = B[ii]
                F[ii]=True
                # del RADDER[ii]
                if next > max:
                    max = next
                max = updown(A,B,F,next,max)
                if max == maxab :break
                if DEBUG : print('next,max,RADDER0=',next,max,F,len(F))
            elif B[ii] == now:
                next = A[ii]
                F[ii]=True
                # del RADDER[ii]
                if next > max:
                    max = next
                max = updown(A,B,F,next,max)
                if max == maxab :break
                if DEBUG : print('next,max,RADDER1=',next,max,F,len(F))
        # if ii >= len(RADDER)-1: break
    return(max)

N = int(input())

dprint('N',N)

# RADDER = []
A = []
B = []
F = []
for ii in range(N):
    a,b = input_list()
    A.append(a)
    B.append(b)
    F.append(False)
    # RADDER.append([a,b,False])

maxa = max(A)
maxb = max(B)
maxab = max(maxa,maxb)

# dprint('RADDER',RADDER)
dprint('A',A)
dprint('B',B)
dprint('F',F)

max = updown(A,B,F,1,1)
print(max)
