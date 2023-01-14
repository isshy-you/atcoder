# -*- coding: utf-8 -*-
# ACx12 TLEx20

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

# 2次元リスト型標準入力
def input_list_2dt(lines):
    dat=[]
    for yy in range(lines):
        values = list(input()[:-1])
        # if len(values)==x:
        dat.append(values)
    return(dat)

DEBUG=False
# DEBUG=True

inp = input_list()
H = inp[0]
W = inp[1]
dprintn('H',H)
dprint('W',W)

A=[]
A = input_list_2dt(H) # dat[row][column]
dprint('A',A)

inp = int(input())
Q = inp
dprint('Q',Q)

a=[]
a = input_list_2d(Q) # dat[row][column]
dprint('a',a)

def rotate(a,b,h,w):
    dprintn('a',a)
    dprintn('b',b)
    dprintn('h',h)
    dprint('w',w)
    if h != 1:
        for jj in range(0,h-1,1):
            for kk in range(0,w-jj,1):
                dprintn('a+jj',a+jj)
                dprintn('b+kk',b+kk)
                dprintn('~a+jj',a+h-jj-1)
                dprintn('~b+kk',b+w-kk-1)
                dprintn('A',A[a+jj][b+kk])
                dprint('~A',A[a+h-jj-1][b+w-kk-1])
                tmp = A[a+jj][b+kk]
                A[a+jj][b+kk] = A[a+h-jj-1][b+w-kk-1]
                A[a+h-jj-1][b+w-kk-1] = tmp
    else:
        jj = 0
        for kk in range(0,int(w/2),1):
            dprintn('a+jj',a+jj)
            dprintn('b+kk',b+kk)
            dprintn('~a+jj',a+h-jj-1)
            dprintn('~b+kk',b+w-kk-1)
            dprintn('A',A[a+jj][b+kk])
            dprint('~A',A[a+h-jj-1][b+w-kk-1])
            tmp = A[a+jj][b+kk]
            A[a+jj][b+kk] = A[a+h-jj-1][b+w-kk-1]
            A[a+h-jj-1][b+w-kk-1] = tmp

for ii in range(Q):
    rotate(      0 ,       0,  a[ii][0],  a[ii][1])
    dprint('A0',A)

    rotate(a[ii][0],       0,H-a[ii][0],  a[ii][1])
    dprint('A1',A)

    rotate(      0 ,a[ii][1],  a[ii][0],W-a[ii][1])
    dprint('A2',A)

    rotate(a[ii][0],a[ii][1],H-a[ii][0],W-a[ii][1])
    dprint('A3',A)

for ii in range(H):
    for jj in range(W):
        print(A[ii][jj],end='')
    print('')