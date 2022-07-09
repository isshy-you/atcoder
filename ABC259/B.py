# -*- coding: utf-8 -*-
import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=0

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

a,b,d = map(int,input().split())
if DEBUG==1:
    # print('{}N歳のとき{}Tcmになった'.format(N,T))
    # print('{}M歳の身長cmは？'.format(M))
    # print('{}X歳まで身長が毎年{}Dcm伸びた'.format(X,D))
    print(a,b,d)

dist = (a**2+b**2)**0.5
angle = math.atan2(b,a)
if DEBUG==1:
    print('dist',dist)
    print('angle',angle,angle/math.pi*180)
    print('ans',d/180*math.pi,d)
x = dist*math.cos(angle+d/180*math.pi)
y = dist*math.sin(angle+d/180*math.pi)

print(x,y)

sys.exit()
