# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(1000000)

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

#DEBUG=True
DEBUG=False

N = int(input())
S = input()

if DEBUG: print(N,S,len(S),int(len(S)))

length=len(S)

ss = []
for ii in range(length):
    ss.append(S[ii])

if DEBUG: print('Q:',ss)

# for ii in range(int(length/2)):
ii = 0
while (ii<int(length/2)):
    if DEBUG: print('compare:',ii,ss[ii],ss[length-1-ii])
    if ss[ii]!=ss[length-1-ii]:
        if ii==0:
            if ss[ii]=='A': #最初がA!=BならNO
                if DEBUG: print(ii,ss[ii])
                print("No")
                sys.exit()
            else:
                ss[ii]='A'
                ss[ii+1]='B'
        else:
            if ss[ii]=='A': #A!=B
                if DEBUG: print(ii,ss[ii])
                ss[length-1-ii]='A'
                ss[length-ii]='B'
            else:
                ss[ii]='A'
                ss[ii+1]='B'
    else:
        ii = ii+1
    if DEBUG:print(ii)
if DEBUG: print('ANS:',ss)
print('Yes')



sys.exit()
