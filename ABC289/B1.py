# -*- coding: utf-8 -*-

import sys
import math

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')
    exit()

def printNo():
    print('No')
    exit()

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(lines):
    dat=[]
    for yy in range(lines):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

DEBUG=False
# DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N)
dprint('M',M)

dat = input_list()

dprint('dat',dat)

    

ans = []
pntr = 1
ii = 0

if M==0:
    for ii in range(N):
        ans.append(ii+1)
else:
    while (pntr <= N):
        tmp = []
        dprintn('ii',ii)
        dprintn('dat[ii]',dat[ii])
        while(True):
            dprint('pntr',pntr)
            tmp.append(pntr)
            dprint('tmp',tmp)
            if pntr == dat[ii]:
                pntr = pntr + 1
                if ii < M-1 :
                    ii = ii + 1
            else:
                pntr = pntr + 1
                break
        for jj in range(len(tmp)):
            ans.append(tmp[len(tmp)-1-jj])
        dprint('ans',ans)


# for ii in range(len(dat)):
#     tmp = []
#     dprintn('dat[ii]',dat[ii])
#     while(True):
#         dprint('pntr',pntr)
#         tmp.append(pntr)
#         dprint('tmp',tmp)
#         if pntr != dat[ii]:
#             pntr = pntr + 1
#             break
#         pntr = pntr + 1
#     for jj in range(len(tmp)):
#         ans.append(tmp[len(tmp)-1-jj])
#     dprint('ans',ans)

print(*ans)