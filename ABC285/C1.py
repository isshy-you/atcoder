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

DEBUG=False
# DEBUG=True
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_dict = {ALPHABET[ii]:ii for ii in range(26)}

# dprint('ALPHABET_dict',ALPHABET_dict)

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

value = 0
for ii in range(lenS-1,-1,-1):
    dprint('ii',ii)
    dprint(S[ii],ALPHABET_dict[S[ii]])
    if ii == lenS-1:
        value = ALPHABET_dict[S[ii]] + 1
    else:
        value = value + (ALPHABET_dict[S[ii]]+1)*(26**(lenS-1-ii))

    dprint('value',value)

print(value)