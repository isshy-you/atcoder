# -*- coding: utf-8 -*-
# ACx18

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

N = int(input())
A = input_list()

dprint('N',N)
dprint('A',A)

sedai=[0]*(2*N+1)
dprint('sedai',sedai)

print(0)
print(1)
print(1)
sedai[1]=1
sedai[2]=1
for ii in range(1,N,1):
    dprint('index',(ii+1)*2-1)
    sedai[(ii+1)*2-1] = sedai[A[ii]-1]+1       
    sedai[(ii+1)*2+1-1] = sedai[A[ii]-1]+1
    print(sedai[(ii+1)*2-1])
    print(sedai[(ii+1)*2+1-1])
    dprint('sedai',sedai)

