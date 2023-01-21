# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')
    exit()

def printNo():
    print('No')
    exit()

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(lines):
    dat=[]
    for yy in range(lines):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

DEBUG=False
# DEBUG=True

def swap(a,b):
    return(b,a)

inp = input_list()
N = inp[0]
P = inp[1]
Q = inp[2]
R = inp[3]
S = inp[4]
dprintn('N',N)
dprintn('P',P)
dprintn('Q',Q)
dprintn('R',R)
dprintn('S',S)

inp = input_list()
A = inp

dprint('A',A)

for ii in range(Q-P+1):
    dprint('A[P+ii+1]',A[P+ii-1])
    dprint('A[R+ii+1]',A[R+ii-1])
    A[P+ii-1],A[R+ii-1]=swap(A[P+ii-1],A[R+ii-1])

print(*A)