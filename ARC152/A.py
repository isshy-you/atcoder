# -*- coding: utf-8 -*-
# ACx28,WAx19

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
N = inp[0] # N 組
L = inp[1] # L 席
dprintn('N',N)
dprint('L',L)

inp = input_list()
a = inp

cnt2 = a.count(2)
dprint('cnt2',cnt2)

# 1が連続2回来たら2人組とみなす
ii=0
while(ii<N-1):
    if a[ii]==1 and a[ii+1]==1:
        cnt2 = cnt2 + 1
        ii = ii+2
    else:
        ii = ii+1

num2 = (L-1) // 3 # 1席ずつ空けて2組ずつ座るには
dprint('num2',num2)

if num2 >= cnt2: # 1席ずつ空けて2組ずつ座れれたら
    print('Yes')
elif num2 == cnt2-1: # 最後の2人の1組が3席空いてなくて、
    if L % 3 == 2: # 最後2席空きなら
        print('Yes')
    else:
        print('No')
else:
    print('No')

# 続きのメモ
# 1が来たら2席、2が来たら3席 で埋める

'''
3 5
2 2 1

00000
02222

3 6
2 2 2

000000
022022

5 8
1 1 2 2 2

000000000
011022022


'''