# -*- coding: utf-8 -*-
# ACx26

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

S = input()
T = input()

if DEBUG : print('input=',S)
if DEBUG : print('input=',T)

lens = len(S)
lent = len(T)

if DEBUG : print('S=',lens)
if DEBUG : print('T=',lent)

if lens == 0 : 
    print('Yes')
    exit()

if S==T :
    print('Yes')
    exit()

if lens > lent :
    print('No')
    exit()


for ii in range(lens):
    if S[ii] != T[ii]:
        print('No')
        exit()

print('Yes')
exit()

