# -*- coding: utf-8 -*-
# ACx2 TLEx27

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

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
        dat.append(values)
    return(dat)

def input_list_2d1(x,y):
    datx=[]
    daty=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        datx.append(values[0])
        daty.append(values[1])
    return(datx,daty)

def input_list_2d2(x,y):
    dat=[]
    for yy in range(y):
        values = list(input().split())
        dat.append([values[0],int(values[1])])
    return(dat)

def checkwall(r,c):
    for ii in range(N):
        if wall[ii][0]==r and wall[ii][1]==c:
            # if DEBUG : print('wall',ii,r,c)
            return(True)
    return(False)

def move(dir,dis):
    for ii in range(dis):
        if dir == 'U' and pos[0] > 1:
            if not checkwall(pos[0]-1,pos[1]):
                pos[0] = pos[0]-1
        elif dir == 'D' and pos[0] < H:
            if not checkwall(pos[0]+1,pos[1]):
                pos[0] = pos[0]+1
        elif dir == 'L' and pos[1] > 1:
            if not checkwall(pos[0],pos[1]-1):
                pos[1] = pos[1]-1
        elif dir == 'R' and pos[1] < W:
            if not checkwall(pos[0],pos[1]+1):
                pos[1] = pos[1]+1


H,W,RS,CS = input_list()
N = int(input())
wall = input_list_2d(N,N)
Q = int(input())
shiji = input_list_2d2(Q,Q)

pos = [RS,CS]
for ii in range(Q):
    move(shiji[ii][0],shiji[ii][1])
    print(pos[0],pos[1])
