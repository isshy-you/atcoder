# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

DEBUG=0

#input
N,Q = map(int,input().split())
S = sys.stdin.readline()
query=[]
for kk in range(Q):
    a,b=map(int,input().split())
    query.append([a,b])
# if DEBUG==1:
    # print(N,Q)
    # print(S)
    # print(query)

#S->list
moji=[]
for kk in range(N):
    moji.append(S[kk])
if DEBUG==1:
    print(moji)

#QUERY
pointer=0
for kk in range(Q):
    if query[kk][0]==1:
        pointer = pointer + query[kk][1]
        pointer = pointer % N
        # for ii in range (query[kk][1]):
        #     buf = moji[N-1]
        #     moji.pop(N-1)
        #     moji.insert(0,buf)
        #     if DEBUG==1:
        #         print(moji)
        if DEBUG==1:
            print('pointer',pointer)
    elif query[kk][0]==2:
        pos = (query[kk][1]-1) - pointer
        if pos < 0:
            pos = pos + N
        if DEBUG==1:
            print('pos',pos)
        print(moji[pos])
    else:
        sys.exit(-1)

sys.exit()
