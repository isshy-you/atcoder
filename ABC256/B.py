# -*- coding: utf-8 -*-
import sys

def calc(point,pos,move):
#    print('*****',point,pos,move)
    if pos[3]==1:
        pos[3]=0
        point = point+1

    if pos[2]==1:
        pos[2]=0
        if (move > 1):
            point = point+1
        else:
            pos[2+1]=1

    if pos[1]==1:
        pos[1]=0
        if (move > 2):
            point = point+1
        else:
            pos[1+move]=1

    if (move > 3):
        point = point+1
    else:
        pos[move]=1
    
    return (point,pos)

sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
a = input().split()

#[0][1][2][3]
point = 0
pos = [0,0,0,0]

for ii in range(n):
    a[ii]=int(a[ii])

for ii in range (n):
    point,pos = calc(point,pos,a[ii])

print(point)