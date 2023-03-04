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

C = []
a = []
for ii in range(M):
    inp = input_list()
    C.append(inp[0])
    inp = input_list()
    a.append(set(inp))

dprint('C',C)
dprint('a',a)

# for ii in range(M-1):
#     all = all | a[ii]
# dprint('all',all)

def calc(jj,all,cnt,a):
    dprintn('jj',jj)
    dprintn('all',all)
    dprint('cnt',cnt)
    for ii in range(jj):
        all = all | a[ii]
        if len(all) == N:
            cnt = cnt + 1
        cnt = calc(ii,all,cnt,a)
    return(cnt)


def check(jj,sum,cnt,use):
    dprintn('jj',jj)
    dprintn('sum',sum)
    dprint('cnt',cnt)
    dprint('use',use)
    if len(sum) == N:
        cnt = cnt + 2**(M-len(use))
    else:
        for ii in range(jj+1,M,1):
            cnt = check(ii,sum,cnt,use)
            sum = sum | a[ii]
            use.add(ii)
            cnt = check(ii,sum,cnt,use)
    return(cnt)

cnt = 0
sum = set()
use = set()
for ii in range(M):
    cnt = check(ii,sum,cnt,use)
    sum = sum | a[ii]
    use.add(ii)
    cnt = check(ii,sum,cnt,use)

dprint('cnt',cnt)