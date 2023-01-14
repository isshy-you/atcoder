# -*- coding: utf-8 -*-
# AC

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

DIGITP = '1234567890'

inp = int(input())
N = inp
dprint('N',N)

def cntup(s):
    dprint('s0',s)
    if s[1] == '9':
        s[1] = '0'
        if s[0] == '9':
            s[0] = '0'
            s[2] = '0'
            if s[3] == '9':
                s[3] = '0'
                s[4] = '0'
                if s[5] == '9':
                    s[5] = '0'
                    if s[6] == '9':
                        s[6] = '0'
                        if s[7] == '9':
                            s[7] = '0'
                            s[8] = DIGITP[int(s[8])]
                        else:
                            s[7] = DIGITP[int(s[7])]
                            s[8] = s[7]
                    else:
                        s[6] = DIGITP[int(s[6])]
                else:
                    s[5] = DIGITP[int(s[5])]
            else:
                s[3] = DIGITP[int(s[3])]
                s[4] = s[3]
        else:
            s[0] = DIGITP[int(s[0])]
            s[2] = s[0]
    else:
        s[1] = DIGITP[int(s[1])]
    dprint('s1',s)
    return(s)


S = list('0 0 0 0 0 0 0 1 1'.split())
dprint('S',S)
cnt = 0
while(cnt != N-1):
    S = cntup(S)
    cnt = cnt + 1

for ii in range(8,-1,-1):
    print(S[ii],end='')
print('')
