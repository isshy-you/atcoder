# -*- coding: utf-8 -*-
# ACx11

DEBUG=False
# DEBUG=True

# 1 <= X <= Y <= 100
# 1 <= N <= 100
X,Y,N = map(int,input().split())

if DEBUG : print('INPUT = ',X,Y,N)

min = 99999
for n in range(0,101,1): # n
    for m in range(0,101,1): # m
        if N==n+3*m:
            if DEBUG : print ('n,m=',n,m)
            sum = X*n+Y*m
            if sum < min:
                min = sum
                if DEBUG : print('min=',min)

print(min)
exit()