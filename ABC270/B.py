# -*- coding: utf-8 -*-
# ACx27

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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

# S = input()
X,Y,Z = input_list()
# dat=[]
# dat = input_list_2d(N,M)

if DEBUG : print(X,Y,Z)

if X > 0  :
    if (Y > X or Y < 0): # 0_X_Y or Y_0_X
        print(X) # 壁がなければ直接
        exit()
    elif (Y < X and Y > 0): 
        if Z < 0: # Z_0_Y_X
            print(-Z*2+X) 
            exit()
        elif Z < Y: # 0_Z_Y_X
            print(X)
            exit()
        elif Z > Y: # 0_Y_Z_X or 0_Y_X_Z
            print(-1)
            exit()
if X < 0  :
    if (Y < X or Y > 0):
        print(-X) # 壁がなければ直接
        exit()
    elif (Y > X and Y<0):
        if Z > 0:
            print(Z*2-X)
            exit()
        elif Z > Y :
            print(-X)
            exit()
        elif Z < Y:
            print(-1)
            exit()
    