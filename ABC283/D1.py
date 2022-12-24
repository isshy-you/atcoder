# -*- coding: utf-8 -*-
# ACx24 REx4

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

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
digit = '0123456789'
hex = '0123456789ABCDEF'

DEBUG=False
DEBUG=True

inp = input()
S = inp[:-1]
lenS = len(S)
s = list(S)
dprintn('len(S)',lenS)
dprint('s',s)

def check(ptr,box):
    box2 = set()
    ii = ptr
    while(True):
        dprintn('ii',ii)
        dprint('box',box)
        if s[ii] == '(':
            ii = check(ii+1,box2)
        elif s[ii] in alphabet:
            if s[ii] in box:
                printNo()
                exit()
            else:
                box2.add(s[ii])
                dprint('box2',box2)
        elif s[ii] == ')':
            dprint('ii',ii)
            return(ii)
        ii = ii + 1

box=set()
ii = 0
while(ii < lenS):
    if s[ii] == '(':
        ii = check(ii+1,box)
    elif s[ii] in alphabet:
        if s[ii] in box:
            printNo()
            exit()
        else:
            box.add(s[ii])
            dprint('box',box)
    ii = ii + 1

printYes()           