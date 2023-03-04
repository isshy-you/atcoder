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

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

ans=[]
for ii in range(lenS):
    if s[ii] in alphabet:
        idx = alphabet.index(s[ii])
        ans.append(ALPHABET[idx])
        print(ALPHABET[idx],end='')

print('')