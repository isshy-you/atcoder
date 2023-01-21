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
dprintn('N',N)

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

A = ''
flag = False
for ii in range(lenS):
    if S[ii]!='n' and S[ii]!='a':
        A = A + S[ii]
        flag = False
    elif S[ii]=='n':
        A = A + S[ii]
        flag = True
    elif S[ii]=='a' and flag == True:
        A = A + 'y' + S[ii]
        flag = False
    else:
        A = A + S[ii]

print(A)