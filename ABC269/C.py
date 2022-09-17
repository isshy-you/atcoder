# -*- coding: utf-8 -*-
# ACx33

from site import abs_paths
import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

N=int(input())

if DEBUG : print('input=',N)

bit=[]
val=[]
print(0)
val.append(0)
for ii in range(0,60,1):
    a = N % 2
    if DEBUG : print('N % 2 =',a )
    bit.append(a)
    if a==1:
        for jj in range(len(val)):
            ans = val[jj]+2**ii
            print(ans)
            val.append(ans)
    if N==0:break
    N = N // 2
    if DEBUG : print('val=',val)

if DEBUG : print('bit=',bit)