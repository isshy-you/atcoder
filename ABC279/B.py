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

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

inp = input()
T = inp[:-1]
lenT = len(T)
t = list(T)
dprintn('len(T)',lenT)
dprint('t',t)

a = T in S

if a : printYes()
else: printNo()