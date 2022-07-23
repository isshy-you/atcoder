# -*- coding: utf-8 -*-
# 

import sys
import math

sys.setrecursionlimit(1000000)

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

DEBUG=False
# DEBUG=True

L1,R1,L2,R2 = map(int,input().split())

if (DEBUG):
    print(L1,R1,L2,R2)

if (R1<L2) or (L1>R2):
    ans = 0
elif L1==L2:
    if R1==R2:
        ans = R1-L1
    elif (R1>R2):
        ans = R2-L2
    else:
        ans = R1-L1
elif L1<L2:
    if R1==R2:
        ans = R2-L2
    elif R1>R2:
        ans = R2-L2
    else:
        ans = R1-L2
else: #L1>L2
    if R1==R2:
        ans = R1-L1
    if R1>R2:
        ans = R2-L1
    else:
        ans = R1-L1

print(ans)
sys.exit()
