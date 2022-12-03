# -*- coding: utf-8 -*-
# ACx48 TLEx15

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

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 素因数分解
def factorization2(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
                arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr


K = int(input())
dprint('K',K)

soinsu = factorization2(K)
dprint('soinsu',soinsu)

if len(soinsu) == 1:
    print(K)
    exit()

kaijo = 1
ii = 2
aa = []
while (True):
    aa = factorization2(ii)
    dprint('aa',aa)
    for jj in range(len(aa)):
        if aa[jj] in soinsu:
            soinsu.remove(aa[jj])
    dprint('soinsu',soinsu)
    if len(soinsu)==0:
        print(ii)
        exit()
    ii = ii + 1


'''
25
'''