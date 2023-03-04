# -*- coding: utf-8 -*-
# ACx30 WAx6

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

def input_list_2d_dict(lines):
    dat=[]
    datlist=set()
    for yy in range(lines):
        values = list(map(int,input().split()))
        dat.append(values)
        datlist.add(values[0])
        datlist.add(values[1])

    return(dat,datlist)

DEBUG=False
DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N)
dprint('M',M)

dat = [[]*(N) for i in range(N)]
dprint('dat',dat)
datlist=set()
datdict={}
for yy in range(M):
    values = list(map(int,input().split()))
    if len(dat[values[0]-1])>=2:
        printNo()
    elif values[1] in dat[values[0]-1]:
        printNo()        
    else:
        dat[values[0]-1].append(values[1])
        dat[values[1]-1].append(values[0])
    datlist.add(values[0])
    datlist.add(values[1])

dprint('dat',dat)
dprint('datlist',datlist)

if M == 0:
    printNo()

if N == M:
    printNo()

if N != M+1:
    printNo()

cnt = 0
hashi = []
for ii in range(N):
    dprintn('ii',ii)
    if len(dat[ii]) == 1: # 端っこは2個だけ
        cnt = cnt + 1
        hashi.append(ii+1)
        dprintn('hashi',hashi)
        if cnt >= 3: # 端っこは2個だけ
            printNo()
        dprintn('cnt',cnt)
dprint('',0)
ptr = hashi[0]
for ii in range(N):
    dprintn('ii',ii)
    dprintn('ptr',ptr)
    datlist.remove(ptr)
    flag=False
    if len(dat[ptr-1]) == 1:
        break
    for jj in range(len(dat[ptr-1])):
        if dat[ptr-1][jj] in datlist:
            nptr = dat[ptr-1][jj]
            dprint('nptr',nptr)
            flag = True
            break
    if not flag and len(dat[ptr-1])==2:
        printNo()
    ptr = nptr

if len(datlist)==0:
    printYes()
else:
    printNo()