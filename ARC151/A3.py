# -*- coding: utf-8 -*-
# ACx13
# WAx14

import sys
import math

sys.setrecursionlimit(1000000)

AINP=False
DEBUG=False
AINP=True
# DEBUG=True

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))

def stringindex(text):
    tmp = []
    for ii in range(len(text)):
        tmp.append(text[ii])
    return(tmp)

if AINP:
    # N = 5
    # S='00100'
    # T='10011'
    N = 8
    S='00000011'
    T='00111100'
else:
    N = int(input()) # 文字数
    S = input()
    T = input()

dprint('N',N)
dprint('S',S)
dprint('T',T)
zero = '0' * N
ds = hamming_distance(zero,S)
dt = hamming_distance(zero,T)
dprint('ds',ds)
dprint('dt',dt)

suuji = ['0' for i in range(N)]
for jj in range(2**N-1):
    ll = jj
    for ii in range(N,0,-1):
        kk = ll % 2
        ll = ll // 2
        if kk==0 :suuji[ii-1]='0'
        else: suuji[ii-1]='1'
    tmp=''
    for ii in range(N):
        tmp += suuji[ii]
    distanceS = hamming_distance(tmp,S)
    distanceT = hamming_distance(tmp,T)
    if distanceS==distanceT:
        print(tmp)
        exit()
print(tmp)
exit()
