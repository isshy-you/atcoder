# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc277/tasks/abc277_c
# ACx8 TLEx10

import sys
import math
import copy

sys.setrecursionlimit(1000000)

DEBUG=False
DEBUG=True

input = sys.stdin.readline

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

N = int(input())

dprint('N',N)

RADDER = {}
for ii in range(N):
    a,b = input_list()
    if a in RADDER:
        RADDER[a].append(b)
    else:
        RADDER[a]=[b]
    if b in RADDER:
        RADDER[b].append(a)
    else:
        RADDER[b]=[a]

dprint('RADDER',RADDER)
floor = [1] # スタートは１階
ptr = 0
cnt = 0 
while(RADDER):
    if floor[ptr] in RADDER:
        lst = RADDER.pop(floor[ptr])
        dprint('lst',lst)
        for ii in lst:
            if DEBUG : cnt = cnt + 1
            dprint('ii',ii)
            if not ii in floor:
                floor.append(ii)
            dprint('floor',floor)
        dprint('RADDER',RADDER)
    else:
        break
    ptr = ptr + 1
    if len(floor) <= ptr:
        break

print(max(floor))
dprint('cnt',cnt)