# -*- coding: utf-8 -*-
# ACx4 TLEx16 REx1

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

inp = input_list()
N = inp[0]
M = inp[1]
K = inp[2]
dprintn('N',N)
dprintn('M',M)
dprint('K',K)

inp = input_list()
A = inp
dprint('A',A)
B = sorted(A[:M+K]) # 加算対象(シフトする分含む)
C = A[M:M+N-M+1] # 右シフト分の数字
ans = []
sub = 0
for ii in range(N-M+1):
    dprint('B',B)
    dprint('C',C)
    tmp = 0
    cnt = 0
    jj = 0
    while (cnt < K):
        if not (B[jj] in C): # Cにないやつだけ足す
            tmp = tmp + B[jj]
            cnt = cnt + 1
            dprintn('cnt',cnt)
            dprint('B',B[jj])
        jj = jj + 1
    ans.append(tmp)
    if len(C)>0:
        B.remove(A[ii]) # 最初の数字を順番にBから消す
        # C.remove(C[0]) # 右にシフトする分一つ消す
        aa = C.pop(0)

print(*ans)

'''
A = [12, 2, 17, 11, 19, 8, 4, 3, 6, 20]
B = [2, 8, 11, 12, 17, 19]
B = [2, 4, 8, 11, 17, 19]
B = [3, 4, 8, 11, 17, 19]
B = [3, 4, 6, 8, 11, 19]
B = [3, 4, 6, 8, 19, 20]
'''