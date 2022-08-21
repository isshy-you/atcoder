# -*- coding: utf-8 -*-
# ACx28
# after_contest AC

DEBUG=False
# DEBUG=True

N=int(input())
A=[]
B=[]
C=[]
IN = input().split()
length = 0
for ii in range(N):
    A.append([int(IN[ii]),IN[ii]])

I = 0
S = 1
A.sort(reverse=True)

if DEBUG : print('input:',N,A,length)

maxval = 0
maxid = 0,0,0

ia=-1
ib=-1
ic=-1
for ia in range(3):
    for ib in range(3):
        if ib != ia:
            for ic in range(3):
                if ic != ia and ic != ib:
                    if DEBUG:print(ia,ib,ic,A[ia][S],A[ib][S],A[ic][S])
                    tmp = int(A[ia][S]+A[ib][S]+A[ic][S])
                    if maxval <= tmp:
                        maxval = tmp
                        maxid = ia,ib,ic

a,b,c = maxid
print(A[a][S]+A[b][S]+A[c][S])
exit()
