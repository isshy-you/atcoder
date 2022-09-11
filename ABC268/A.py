# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

A,B,C,D,E = map(int,input().split())

if DEBUG : print('input=',A,B,C,D,E)

dat = [A,B,C,D,E]
dat.sort()

if DEBUG : print('dat=',dat)

num = 1
for ii in range(4):
    if dat[ii]!=dat[ii+1]:
        num = num + 1

print(num)