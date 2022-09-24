# -*- coding: utf-8 -*-
# ACx3
# TLEx24

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
DEBUG=True

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

def connect(node,last,goal): # last -> node -> goal
    for ii in range(N-1):
        if flag[ii]==False:
            if dat[ii][0]==node:
                next = dat[ii][1]
                if DEBUG: print('node,next=',node,next)
                if last != next: # loop check
                    if next != goal: # not goal
                        flag[ii]=True
                        if DEBUG: print('*node,next=',node,next,flag)
                        result = connect(next,node,goal)
                        if result:
                            if DEBUG: print('**node,next=',node,next)
                            line.append(next)
                            return(True)
                    else: # goal
                        if DEBUG: print('**node,next=',node,next)
                        line.append(next)
                        return(True)
                else:
                    if DEBUG : print('loop')
            if dat[ii][1]==node:
                next = dat[ii][0]
                if DEBUG: print('node,next=',node,next)
                if last != next:
                    if next != goal:
                        flag[ii]=True
                        if DEBUG: print('*node,next=',node,next,flag)
                        result = connect(next,node,goal)
                        if result:
                            if DEBUG: print('**node,next=',node,next)
                            line.append(next)
                            return(True)
                    else:
                        if DEBUG: print('**node,next=',node,next)
                        line.append(next)
                        return(True)
                else:
                    if DEBUG : print('loop')
    return(False)

# S = input()
N,X,Y = input_list()
dat=[]
dat = input_list_2d(2,N-1)

if DEBUG : print(N,X,Y)
if DEBUG : print(dat)

flag= [False for i in range(N)]
line=[]
# line.append(X)
next = connect(X,0,Y)
if DEBUG: print('final=',next)

if DEBUG : print(line)

ans = ''
for ii in range(len(line)-1,-1,-1):
    val = line[ii]
    if DEBUG : print(val)
    ans += str(val)+' '

print(str(X)+' '+ans)
