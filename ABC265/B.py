# -*- coding: utf-8 -*-
# ACx26

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

# 2 <= N <= 10**5 : ゴール位置
# 0 <= M <= N-2   : ボーナス個数
# 1<= T <= 10**9  : 制限時間
# 1<= Ai <= 10**9 : 消費時間(1 <= i <= N-1)
# 1 < X1 < ... < XM < N : ボーナス部屋
# 1 < Yi <= 10**9       : ボーナス時間

N,M,T = map(int,input().split())
# if DEBUG : print('INPUT = ',N,M,T)
a = input().split()
A=[]
for ii in range(N-1):
   A.append(int(a[ii])) 

# if DEBUG : print('UseTime = ',A)
X=[]
Y=[]
for ii in range(M):
    a = input().split()
    X.append(int(a[0]))
    Y.append(int(a[1]))

# for ii in range(M):
#     if DEBUG : print('bonus = ',ii,X[ii],Y[ii])

# if DEBUG : print('------')

time = 0
bonus = 0
for ii in range(N-1):
    time = time + A[ii]
    if DEBUG : print('time,T =',ii+1,time,T)
    if M > bonus:
        if ii+1 == X[bonus]:
            T = T + Y[bonus]
            if DEBUG : print('bonus,T=',ii+1,bonus,T)
            bonus = bonus + 1
    if ii==N-2:  # 最後は超えてたら駄目
        if time >= T :
            print('No')
            exit()
    else:  # 最後以外ははピッタシでも駄目
        if time >= T:
            print('No')
            exit()
print('Yes')
exit()
