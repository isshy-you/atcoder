# -*- coding: utf-8 -*-
# ACx5 TLEx13
import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
DEBUG=True

def dprint(str,val):
    if DEBUG : print(str,'=',val)

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

def check(val):
    if val==1:return(1)
    for jj in range(len(tree)-1,-1,-1):
        dprint('tree',tree[jj])
        if val in tree[jj]:
            return(sedai[jj]+1)
    print('ERROR')
    exit()

N = int(input())
A = input_list()

dprint('N',N)
dprint('A',A)

tree=[]
sedai=[]
print(0)


for ii in range(N):
    num = check(A[ii])
    dprint('num',num)
    tree.append([A[ii],2*(ii+1),2*(ii+1)+1])
    sedai.append(num)
    print(sedai[ii])
    print(sedai[ii])
dprint('tree',tree)
dprint('sedai',sedai)

# print(0)
# for ii in range(2*N):
#     print(sedai[ii//2])

