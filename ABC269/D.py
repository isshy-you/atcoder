# -*- coding: utf-8 -*-
# AC x32
# WA x35

import sys
import math

# sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

def rep(a,b):
    for ii in range(sizey):
        for jj in range(sizex):
            if dat[jj][ii]==b:
                dat[jj][ii]=a

N=int(input())
# if DEBUG : print('input=',N)


maxx = -1000
maxy = -1000
minx = 1000
miny = 1000
x=[]
y=[]
for ii in range(N):
    S = input().split()
    X = int(S[0])
    Y = int(S[1])
    # if DEBUG : print('X,Y=',X,Y)
    # if Y>=1 : X=X-1
    if maxx < X :
        maxx = X
    if maxy < Y :
        maxy = Y
    if minx > X:
        minx = X
    if miny > Y:
        miny = Y
    x.append(X)
    y.append(Y)

if DEBUG : print(x)
if DEBUG : print(y)

sizex = maxx - minx + 1
sizey = maxy - miny + 1
if DEBUG : print('minx,sizex=',minx,sizex)
if DEBUG : print('miny,sizey=',miny,sizey)

# dat=[[0]*size]*size
dat = [[0]*(sizex+1) for i in range(sizey+1)]
# if DEBUG : print(dat)

for ii in range(N): # ii : line(y)
    # if DEBUG : print('x,y=',x[ii]-minx,y[ii]-miny)
    xx = x[ii]-minx
    yy = y[ii]-miny
    dat[yy][xx] = -1
    if DEBUG : print('dat=',xx,yy,dat[yy][xx])

if DEBUG : 
    for ii in range(sizey):
        print('dat=',ii,dat[ii])
if DEBUG : print('')
ans = 0
num = 1
minus = 0
for jj in range(sizey):
    for ii in range(sizex):
        if dat[jj][ii]==-1:
            dat[jj][ii]=num # checked
            if  dat[jj+1][ii  ]==-1:
                dat[jj+1][ii  ] =num # checked
            if  dat[jj  ][ii+1]==-1:
                dat[jj  ][ii+1] =num # checked
            if  dat[jj+1][ii+1]==-1:
                dat[jj+1][ii+1] =num # checked
            num += 1
        elif dat[jj][ii]!=0:
            if  dat[jj+1][ii  ]==-1:
                dat[jj+1][ii  ] =dat[jj][ii] # checked
            elif dat[jj+1][ii  ]!=0 and dat[jj][ii]!=dat[jj+1][ii  ]:
                if DEBUG : print('minus y+1',ii,jj,dat[jj+1][ii  ])
                rep(dat[jj][ii],dat[jj+1][ii  ])
                minus += 1           
            if  dat[jj  ][ii+1]==-1:
                dat[jj  ][ii+1] =dat[jj][ii] # checked
            elif dat[jj  ][ii+1]!=0 and dat[jj][ii]!=dat[jj  ][ii+1]:
                if DEBUG : print('minus x+1',ii,jj,dat[jj  ][ii+1])
                rep(dat[jj][ii],dat[jj  ][ii+1])
                minus += 1           
            if  dat[jj+1][ii+1]==-1:
                dat[jj+1][ii+1] =dat[jj][ii] # checked
            elif dat[jj+1][ii+1]!=0 and dat[jj][ii]!=dat[jj+1][ii+1]:
                if DEBUG : print('minus x+1,y+1',ii,jj,dat[jj+1][ii+1])
                rep(dat[jj][ii],dat[jj+1][ii+1])
                minus += 1           
        if DEBUG : 
            for ii in range(sizey):
                print('dat=',ii,dat[ii])
        if DEBUG :
            print('num,minus=',num,minus)
        if DEBUG :
            print('')

if DEBUG : 
    for ii in range(sizey):
        print('dat=',ii,dat[ii])

print(num-1-minus)
