# -*- coding: utf-8 -*-
# ACx16, WAx1, TLEx13

import sys
import math
import uu

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

def jump(ans,y,x,dy,dx):
    tmp = ans
    count=0
    yy = y + dy
    xx = x + dx
    if yy>=0 and yy<N and xx>=0 and xx<N  and tmp[yy][xx]==-1:
        tmp[yy][xx] = tmp[y][x]+1
        count+=1
    yy = y - dy
    xx = x - dx
    if yy>=0 and yy<N and xx>=0 and xx<N  and tmp[yy][xx]==-1:
        tmp[yy][xx] = tmp[y][x]+1
        count+=1
    yy = y + dy
    xx = x - dx
    if yy>=0 and yy<N and xx>=0 and xx<N  and tmp[yy][xx]==-1:
        tmp[yy][xx] = tmp[y][x]+1
        count+=1
    yy = y - dy
    xx = x + dx
    if yy>=0 and yy<N and xx>=0 and xx<N and tmp[yy][xx]==-1:
        tmp[yy][xx] = tmp[y][x]+1
        count+=1
    return(count,tmp)

N,M = map(int,input_list())

# if DEBUG : print(N,M)

ans = [[-1]*(N) for i in range(N)]
ans[0][0]=0

if DEBUG: print('ans=',ans)
if DEBUG:
    for i0 in range(N):
        ansstr=''
        for j0 in range(N):
            ansstr += str(ans[i0][j0])+' '
        print(ansstr)
    print('')

ii = 0
di = []
dj = []
while(True):
    ii += 1
    tmp1 = M - ii ** 2
    if tmp1<0:
        break
    tmp2 = tmp1 ** 0.5
    if DEBUG:print('ii,tmp2=',ii,tmp2)
    if tmp2 - int(tmp2) == 0:
        di.append(ii)
        dj.append(int(tmp2))

if DEBUG:print('di,dj=',di,dj)

num=0
while(True):
    if DEBUG:print('num=',num)
    flag = False
    for ii in range(N):
        for jj in range(N):
            if ans[jj][ii] == num:
                if DEBUG: print('ii,jj,num=',ii,jj,num)
                for kk in range(len(di)):
                    if DEBUG:print('jump:',kk,jj,ii,dj[kk],di[kk])
                    ret1,ans = jump(ans,jj,ii,dj[kk],di[kk])
                    if DEBUG:
                        for i0 in range(N):
                            ansstr=''
                            for j0 in range(N):
                                ansstr += str(ans[i0][j0])+' '
                            print(ansstr)
                        print('')
                    if DEBUG:print('jump:',kk,jj,ii,di[kk],dj[kk])
                    ret2,ans = jump(ans,jj,ii,di[kk],dj[kk])
                    if DEBUG:
                        for i0 in range(N):
                            ansstr=''
                            for j0 in range(N):
                                ansstr += str(ans[i0][j0])+' '
                            print(ansstr)
                        print('')
                    if DEBUG:print('ret=',ret1,ret2)
                    if ret1==1 or ret2==1:
                        flag = True
    if flag==False:
        for ii in range(N):
            ansstr=''
            for jj in range(N):
                ansstr += str(ans[ii][jj])+' '
            print(ansstr)
        exit()
    num += 1
