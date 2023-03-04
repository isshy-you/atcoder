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

inp = input_list()
N = inp[0]
Q = inp[1]
dprintn('N',N)
dprint('Q',Q)

dat=[]
dat = input_list_2d(Q) # dat[row][column]
dprint('dat',dat)

card = [0 for i in range(N)]

dprint('card',card)

for ii in range(Q):
    if dat[ii][0] == 1:
        card[dat[ii][1]-1] = card[dat[ii][1]-1] + 1
        if card[dat[ii][1]-1] >=2:
            card[dat[ii][1]-1] = 2
    elif dat[ii][0] == 2:
        card[dat[ii][1]-1] = 2
    else:
        if card[dat[ii][1]-1]==2:
            print('Yes')
        else:
            print('No')
    dprint('card',card)


