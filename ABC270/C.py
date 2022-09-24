# -*- coding: utf-8 -*-
# ACx3
# TLEx24

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

def connect(node,goal,flag): # last -> node -> goal
    for ii in flag:
        if DEBUG: print('ii=',ii,dat[ii],node)
        if dat[ii][0]==node:
            next = dat[ii][1]
            if DEBUG: print('node,next=',node,next)
            if next != goal: # not goal
                # flag[ii]=True # 使ったノードはフラグを立てる
                flag.remove(ii) # 使ったノードは探索しない
                if DEBUG: print('*node,next=',node,next,flag)
                result = connect(next,goal,flag)
                if result:
                    if DEBUG: print('**node,next=',node,next)
                    line.append(next)
                    return(True)
                else:
                    flag.append(ii)
                    if DEBUG: print('-node,next=',node,next,flag)
            else: # goal
                if DEBUG: print('***node,next=',node,next)
                line.append(next)
                return(True)
        elif dat[ii][1]==node:
            next = dat[ii][0]
            if DEBUG: print('node,next=',node,next)
            if next != goal:
                # flag[ii]=True
                flag.remove(ii) # 使ったノードは探索しない
                if DEBUG: print('*node,next=',node,next,flag)
                result = connect(next,goal,flag)
                if result:
                    if DEBUG: print('**node,next=',node,next)
                    line.append(next)
                    return(True)
                else:
                    flag.append(ii)
                    if DEBUG: print('^node,next=',node,next,flag)
            else:
                if DEBUG: print('***node,next=',node,next)
                line.append(next)
                return(True)
    return(False)

# S = input()
N,X,Y = input_list()
dat=[]
dat = input_list_2d(2,N-1)

if DEBUG : print(N,X,Y)
if DEBUG : print(dat)

# flag= [False for i in range(N)]
# flag = [False] * N
flag = list(range(N-1))
line=[]
# line.append(X)
next = connect(X,Y,flag)
if DEBUG: print('final=',next)

if DEBUG : print(line)

ans = ''
for ii in range(len(line)-1,-1,-1):
    val = line[ii]
    if DEBUG : print(val)
    ans += str(val)+' '

print(str(X)+' '+ans)
exit()

'''
6 5 4
3 1
2 5
1 2
4 1
2 6

'''
