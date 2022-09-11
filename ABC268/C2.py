# -*- coding: utf-8 -*-
# ACx11
# TLEx19

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

N = int(input())
P = input().split()

if DEBUG : print('input=',N)
if DEBUG : print('input=',P)

p=[]
for ii in range(N):
    p.append(int(P[ii]))

if DEBUG : print('input=',p)

max = 0
sum = 0
num = [0,0,0] # 左手 正面 右手
dat =[[],[],[]] # 左手[席] 中央[席] 右手[席]
datptr=[0,1,2]
for ptr in range(N):
    if DEBUG :
        txta = ' '
        txtb = ' '
        for xx in range(N):
            txta = txta + str(xx) + ' '
            yy = xx + ptr
            if yy >= N:
                yy = yy - N
            txtb = txtb + str(p[yy]) + ' '
        print(txta)
        print(txtb)
    if ptr==0 :
        for ii in range(N): # iiは人
            for jj in [0,1,2]: # 左右の料理
                kk = ii+(jj-1)+ptr # 回転したときの料理位置
                if kk>=N:
                    kk = kk - N
                elif kk<0:
                    kk = N-1
                if DEBUG : print('ii,kk,p[kk]=',ii,kk,p[kk])
                if ii==p[kk]: # 人と料理がマッチ
                    dat[datptr[jj]].append(True)
                    num[datptr[jj]] = num[datptr[jj]] + 1
                    sum = sum + 1
                else:
                    dat[datptr[jj]].append(False)
        max = sum
        if DEBUG :
            print('dat=',datptr[jj],dat)
            print('datptr=',datptr)
            print('num=',num)
            print('sum=',sum)
            print('max=',max)
    else:
        if   ptr%3==0:datptr=[0,1,2]
        elif ptr%3==1:datptr=[1,2,0]
        elif ptr%3==2:datptr=[2,0,1]
        jj = datptr[2]
        if DEBUG : print('sum,num =',sum,num[jj])
        sum = sum - num[jj]
        num[jj]=0
        for ii in range(N): # iiは人
            kk = ii+(jj-1)+ptr # 回転したときの料理位置
            if kk>=N:
                kk = kk - N
            elif kk<0:
                kk = N-1
            ll = ii+ptr+1 # 回転したときの料理位置
            if ll >= N:
                ll = ll - N
            elif ll<0:
                ll = N-1
            if DEBUG : print('ii,ll,p[ll]=',ii,ll,p[ll])
            if ii==p[ll]: # 人と料理がマッチ
                dat[jj][ii] = True
                num[jj] = num[jj] + 1
                sum = sum + 1
            else:
                dat[jj][ii] = False
        if DEBUG :
            print('dat=',datptr[jj],dat)
            print('datptr=',datptr)
            print('num=',num)
            print('sum=',sum)
            print('max=',max)

        if sum > max:
            max = sum


if max > N:
    max = N

print(max)
