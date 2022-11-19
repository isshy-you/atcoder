# -*- coding: utf-8 -*-

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

def calc(H,M):
    A = H // 10
    B = H % 10
    C = M // 10
    D = M % 10
    return(A,B,C,D)

H,M = input_list()
dprint('H',H)
dprint('M',M)

A,B,C,D = calc(H,M)

if DEBUG : print('A,B,C,D = ',A,B,C,D)

if A == 0 or A == 1:
    if B <= 5:
        if DEBUG : print('=1=')
        print(A*10+B,C*10+D)
    else:
        if DEBUG : print('=2=')
        A=A+1
        B=0
        C=0
        D=0
        print(A*10+B,C*10+D)
elif A == 2 :
    if B <= 5 and C <= 3:
        if DEBUG : print('=3=')
        print(A*10+B,C*10+D)
    else:
        if DEBUG : print('=4=')
        B = B + 1
        if B > 3:
            A = 0
            B = 0
        C = 0
        D = 0
        print(A*10+B,C*10+D)
    

