# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')

def printNo():
    print('No')

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

inp = input_list()
N = inp[0]
T = inp[1]
dprintn('N',N)
dprint('T',T)

inp = input_list()
A = inp
dprint('A',A)

sumA = sum(A)
dprint('sumA',sumA)

m1 = T % sumA # 最初から m1 秒
dprint('m1',m1)

B = [A[0]]
for ii in range(1,N,1):
    B.append(B[ii-1]+A[ii])
dprint('B',B)

for ii in range(N):
    if B[ii] > m1:
        if ii == 0:
            print(1,m1)
            exit()
        else:
            print(ii+1,m1-B[ii-1])
            exit()

