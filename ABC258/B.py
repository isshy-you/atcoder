# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

def search(mas,pos,xp,yp):
    ii=pos[0]
    jj=pos[1]
    buffer=''
    for kk in range (N):
        # print('ii,jj,yp,xp,buffer=',ii,jj,yp,xp,buffer)
        buffer = buffer + mas[ii][jj]
        if (ii==N-1) and yp>0:
            ii=0
        elif (ii==0) and yp<0:
            ii=N-1
        else:
            ii=ii+yp
        if (jj==N-1) and xp>0:
            jj=0
        elif (jj==0) and xp<0:
            jj=N-1
        else:
            jj=jj+xp

    # print(buffer)
    return(int(buffer))

def check(mas,pos):

    max = 0
    val0=search(mas,pos,1,0)
    if max<val0: max = val0
    val1=search(mas,pos,0,1)
    if max<val1: max = val1
    val2=search(mas,pos,1,1)
    if max<val2: max = val2
    val3=search(mas,pos,-1,0)
    if max<val3: max = val3
    val4=search(mas,pos,0,-1)
    if max<val4: max = val4
    val5=search(mas,pos,-1,-1)
    if max<val5: max = val5
    val6=search(mas,pos,-1,1)
    if max<val6: max = val6
    val7=search(mas,pos,1,-1)
    if max<val7: max = val7

    # print(val0,val1,val2,val3,val4,val5,val6,val7,max)
    return(max)

#input
N = int(sys.stdin.readline())
A=[]
for kk in range(N):
    A.append(sys.stdin.readline())

#2D配列 mas[y][x]
mas = [[0 for i in range(N)] for j in range(N)]
max = 0
for ii in range(N):
    for jj in range(N):
        mas[ii][jj]=A[ii][jj]
        if max < int(mas[ii][jj]):
            max = int(mas[ii][jj])
maxval = []
for ii in range(N):
    for jj in range(N):
        if int(mas[ii][jj])==max:
            maxval.append([ii,jj])

# print(mas)
# print(maxval)
# print(len(maxval))

valmax = 0
for kk in range(len(maxval)):
    val=check(mas,maxval[kk])
    if valmax < val:
        valmax = val

print(valmax)