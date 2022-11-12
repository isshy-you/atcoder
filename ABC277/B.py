# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

input = sys.stdin.readline

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(x,y):
    dat=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

N = int(input())

S=[]
for ii in range(N):
    tmp = input()
    S.append(tmp[:-1])



SECOND = 'A23456789TJQK'
S.sort()

if DEBUG :
    for ii in range(N):
        print(ii,':::'+S[ii])

result = True
for ii in range(N):
    if S[ii][0] == 'H' or S[ii][0] == 'D' or S[ii][0] == 'C' or S[ii][0] == 'S':
        if S[ii][1] in SECOND:
            if ii != 0 :
                if S[ii] == S[ii-1]:
                    result = False
        else:
            result = False
    else:
        result = False

if result:
    print('Yes')
else:
    print('No')


