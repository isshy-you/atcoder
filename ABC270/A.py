# -*- coding: utf-8 -*-
# ACx10

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
A,B = input_list()
# dat=[]
# dat = input_list_2d(N,M)

if DEBUG : print(A,B)

point=[1,2,4]
a=[]
b=[]
for ii in range(3):
    a1 = A % 2
    if a1!=0:a.append(1)
    else:a.append(0)
    A = A // 2

    b1 = B % 2
    if b1!=0:b.append(1)
    else:b.append(0)
    B = B // 2

if DEBUG : print(a)
if DEBUG : print(b)

C=0
if a[0]==1 or b[0]==1:
    C=C+1
if a[1]==1 or b[1]==1:
    C=C+2
if a[2]==1 or b[2]==1:
    C=C+4

print(C)