# -*- coding: utf-8 -*-
# ACx9 WAx8
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

inp = input_list()
N = inp[0]
A = inp[1]
B = inp[2]
dprintn('N',N)
dprintn('A',A)
dprintn('B',B)

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

max = lenS//2 * B
dprint('max',max)
min = max

for ii in range(lenS//2):
    cnt = lenS//2
    for jj in range(lenS//2):
        if s[ii+jj] == s[N-1-ii-jj]:
            cnt = cnt -1
    tmp = ii * A + cnt * B
    if min > tmp :
        min = tmp

print(min) 