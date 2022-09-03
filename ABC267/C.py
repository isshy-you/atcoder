# -*- coding: utf-8 -*-
# AC x29

def func(a,N,M):
    ans = 0
    val = 0
    for jj in range(M):
        ans = ans + a[jj]*(jj+1)
        val = val + a[jj]
        max = ans
    if DEBUG:print('val,ans=',val,ans)
    for ii in range(M,N,1):
        ans = ans + a[ii]*(M) - val
        val = val - a[ii-M] + a[ii]
        if DEBUG:print('ii,val,ans=',ii,val,ans)
        if max < ans :
            max = ans
            if DEBUG:print('ans,max=',ans,max)

    return(max)        

DEBUG=False
# DEBUG=True

N,M = map(int,input().split())
A = input().split()
if DEBUG : print('INPUT = ',N,M)

a=[]
for ii in range(N):
    a.append(int(A[ii]))

if DEBUG : print(a)

max = func(a,N,M)
print(max)