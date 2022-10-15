# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

N = int(input())
A = input_list()

dprint('N',N)
dprint('A',A)

a = list(set(A))
a.sort()
dprint('a',a)
A.sort()
dprint('A',A)

ans = [0]*N
ans2 = [0]*N
ii = 0
jj = 0
while (ii < N):
    while(A[ii] > a[jj]):
        jj = jj + 1
    num = len(a) - (jj + 1)
    dprint('num',num)
    ans2[num]+=1
    ii = ii + 1

for ii in range(N):
    if DEBUG:
        print(ii,ans2[ii])
    else:
        print(ans2[ii])
