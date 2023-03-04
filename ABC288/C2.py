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
DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N)
dprint('M',M)

AB=[]
A=[]
B=[]
dat = [[]*(N) for i in range(N)]
dprint('dat',dat)
for ii in range(M):
    a,b =input_list()
    AB.append([a,b])
    A.append(a)
    B.append(b)
    dat[a-1].append(b)
    dat[b-1].append(a)

dprint('AB',AB)
dprint('A',A)
dprint('B',B)
cnt = 0
check = True
ptr = 1
trace = set()
trace.add(ptr)
loop = 0
while(True):
    dprintn('見る頂点の接続',dat)
    dprintn('今ptr',ptr)
    dprintn('行ったことある',trace)
    dprint('cnt',cnt)
    check = 0
    for ii in range(len(dat[ptr-1])):
        dprint('次ptr確認',dat[ptr-1][ii])
        if not dat[ptr-1][ii] in trace:
            nptr = dat[ptr-1][ii]
            trace.add(dat[ptr-1][ii])
        else:
            check = check + 1
        dprint('行ったことある数',check)
        dprint('今見ている行き先',dat[ptr-1])
        if check == len(dat[ptr-1]):
            cnt = cnt + 1
            if ptr < N:
                nptr = dat[ptr][0]
                trace.add(dat[ptr-1][ii])
        if len(trace)>=N:
            break
        ptr = nptr
    loop = loop + 1
    if loop > N:break

dprintn('見る頂点の接続',dat)
dprintn('今ptr',ptr)
dprintn('行ったことある',trace)
dprint('cnt',cnt)
dprint('nptr',nptr)

print(cnt)

# dprint('ten',ten)
# dprint('check',check)
# if ten == M: print(1)
# elif check : print(cnt)
# else : print(0)

