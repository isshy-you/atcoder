# -*- coding: utf-8 -*-
# ACx17
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
min = max
dprint('min',min)

for ii in range(lenS//2):
    cnt = lenS//2
    dprintn('ii',ii)
    for jj in range(lenS//2):
        m = ii+jj
        n = lenS-1+ii-jj
        if n >= lenS:
            n = n-lenS
        dprintn('s[m]',s[m])
        dprintn('s[n]',s[n])
        if s[m] == s[n]:
            cnt = cnt -1
    dprintn('cnt',cnt)
    tmp = ii * A + cnt * B
    dprintn('tmp',tmp)
    if min > tmp :
        min = tmp
    dprint('min',min)

print(min) 