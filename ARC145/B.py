# -*- coding: utf-8 -*-
# Python/PyPy3
# AC x4
# WA x11
# TLE x7

import sys

sys.setrecursionlimit(1000000)

def checkb(nn,alice):
    lmax = int(nn/B)
    if DEBUG:print('nn,lmax,alice:',nn,lmax,alice)
    for ll in range(1,lmax+1,1):
        if DEBUG:print('ll:',ll)
        mm = nn-B*ll
        if mm >= A:
            alice = checka(mm,alice)
        else:
            return(alice+1)

def checka(nn,alice):
    kmax = int(nn/A)
    if DEBUG:print('nn,kmax,alice:',nn,kmax,alice)
    for kk in range(1,kmax+1,1):
        if DEBUG:print('kk:',kk)
        mm = nn-A*kk
        if mm >= B:
            alice = checkb(mm,alice)
        else:
            return(alice+1)

# DEBUG=True
DEBUG=False

N,A,B = map(int,input().split())

if DEBUG: print(N,A,B)

alice = checka(N,0)

print(alice)

sys.exit()

