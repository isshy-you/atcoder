# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

AINP=False
AINP=True
DEBUG=False
DEBUG=True

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(x,y):
    dat=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

if AINP:
    N = 4 # 個数
    M = 2 # 最大数
    P = [4,1,3,2]
    M  = 20
    N = 100000
    P = [11, 15, 3, 20, 17, 6, 1, 9, 5, 19, 10, 16, 7, 8, 12, 2, 18, 14, 4, 13]
else:
    N,M = input_list()
    P = input_list()

dprint('N',N)
dprint('M',M)
dprint('P',P)

# suuji = ['0' for i in range(N)]
# if DEBUG:
#     dcount = 0
#     for jj in range(M**N):
#         ll = jj
#         for ii in range(N,0,-1):
#             kk = ll % M
#             # ll = ll // M
#             suuji[ii-1]=str(kk+1)
#         A=''
#         for ii in range(N):
#             A += suuji[ii]
#         # dprint('A',A)
#         B=''
#         for ii in range(N):
#             B = B + A[P[ii]-1]
#         # dprint('B',B)
#         if (A < B):
#             dprint('ans',A)
#             dcount = dcount + 1

#     dans = dcount % 998244353
#     dprint('dans',dans)

count = M**(N-1)

dprint('count',count)

dmax = max(P)

minus = 2 **(N - P.index(1) - 1)
dprint('minus',minus)

minus2 = 2 **(N - P[0] + 1)
dprint('minus2',minus2)

ans = (count - minus + minus2) % 998244353

print(ans)

# for ii,val in enumerate(P):
#     for jj in range(M,0.-1):
            
