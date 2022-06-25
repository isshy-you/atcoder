# -*- coding: utf-8 -*-
# AC  x5
# TLE x28
# RE  x2
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
S = sys.stdin.readline()
str = sys.stdin.readline().split()

W=[]
for ii in range(N):
    W.append(int(str[ii]))

adult = []
child = []
num = 0
# for ii in range(N):
#     num = num + int(S[ii])

for ii in range(N):
    if S[ii]=='1':
        adult.append(W[ii])
    else:
        child.append(W[ii])
adult.sort()
child.sort()
adultn = len(adult)
childn = len(child)

# print(adult)
# print(child)
nummax = 0
if len(adult)==0:
    nummax = N
elif len(child)==0 and child[childn-1]!=10**9:
    nummax = N
else:
    for ii in range(adultn):
        for jj in range(childn):
            # print('adult[ii],child[jj]=',ii,jj,adult[ii],child[jj])
            if adult[ii] > child[jj]:
                num = adultn-ii + jj +1
                # print('adult',num)
            elif adult[ii] <= child[jj]:
                num = adultn-ii-1 + jj
                # print('child',num)
            if num >= nummax:
                nummax = num

print(nummax)
