# -*- coding: utf-8 -*-

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

N,Q = map(int,input().split())

val=[]
for ii in range(N):
    tmp=input_list()
    L=tmp[0]
    tmp.remove(L)
    val.append(tmp)

query=[]
for ii in range(Q):
    tmp=input_list()
    query.append(tmp)

if DEBUG : print(val)
if DEBUG : print(query)


for ii in range(Q):
    if DEBUG : print(query[ii][0],query[ii][1])
    print(val[query[ii][0]-1][query[ii][1]-1])