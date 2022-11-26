# -*- coding: utf-8 -*-
# ACx50, WAx6, TLEx18

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
H = inp[0]
W = inp[1]
dprintn('H',H)
dprint('W',W)

# 行列を入れ替える

s = [''*(W) for i in range(W)]
for ii in range(H):
    inp = input()
    for jj in range(W):
        s[jj] = str(s[jj]) + str(inp[jj])

t = [''*(W) for i in range(W)]
for ii in range(H):
    inp = input()
    for jj in range(W):
        t[jj] = str(t[jj]) + str(inp[jj])

dprint('s',s)
dprint('t',t)

cnt = 0
for jj in range(W):
    if s[jj] in t:
        dprint('s[jj]',s[jj])
        cnt = cnt + 1

if cnt == W : printYes()
else : printNo()
