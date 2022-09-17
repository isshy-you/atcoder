# -*- coding: utf-8 -*-
# AC x7
# WA x57
# RE x3

from site import abs_paths
import sys
import math

# sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

N=int(input())
# if DEBUG : print('input=',N)


max = 0
min = 99999
x=[]
y=[]
for ii in range(N):
    S = input().split()
    X = int(S[0])
    Y = int(S[1])
    # if DEBUG : print('X,Y=',X,Y)
    if Y>=1 : X=X-1
    if max < X+1 :
        max = X+1
    if max < Y+1 :
        max = Y+1
    if min > X+1:
        min = X+1
    if min > Y+1:
        min = Y+1
    x.append(X)
    y.append(Y)

if DEBUG : print(x)
if DEBUG : print(y)

size = max - min + 1


# dat=[[0]*size]*size
dat = [[0]*size for i in range(size)]

if DEBUG : print(dat)
for ii in range(N):
    dat[y[ii]+1][x[ii]+1] = 1
    if DEBUG : print('dat=',x[ii]+1,y[ii]+1,dat[y[ii]+1][x[ii]+1])

if DEBUG : print(dat)

ans = 0
num = 10
for ii in range(max):
    for jj in range(max):
        if dat[jj][ii]==1:
            dat[jj][ii]=num # checked
            if dat[jj+1][ii]==1:
                dat[jj+1][ii]=num # checked
            if dat[jj][ii+1]==1:
                dat[jj][ii+1]=num # checked
            if dat[jj+1][ii+1]==1:
                dat[jj+1][ii+1]=num # checked
            num += 10
        elif dat[jj][ii]!=0:
            if dat[jj+1][ii]!=dat[jj][ii]:
                dat[jj+1][ii]=dat[jj][ii] # checked
            if dat[jj][ii+1]!=dat[jj][ii]:
                dat[jj][ii+1]=dat[jj][ii] # checked
            if dat[jj+1][ii+1]!=dat[jj][ii]:
                dat[jj+1][ii+1]=dat[jj][ii] # checked

if DEBUG : 
    for ii in range(4):
        print('dat=',dat[3-ii])

print(int(num/10-1))






