# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

N = int(input())
A = input_list()

if DEBUG : print(N)
if DEBUG : print(A)

sum=0
for ii in range(N):
    sum+=A[ii]

print(sum)