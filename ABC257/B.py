# -*- coding: utf-8 -*-
import sys

def move(ii):
    for jj in range(ii+1,k,1):
        if q[ii]+1 != q[jj]:
            q[ii] = q[ii] + 1


n,k,q = map(int,input().split())
# a = map(int,input().split())
# l = map(int,input().split())
a_str=input().split()
l_str=input().split()

a=[]
for ii in range(k):
    a.append(int(a_str[ii]))
l=[]
for ii in range(q):
    l.append(int(l_str[ii]))

for ii in range(q):
    # print('ii',ii)
    # print('l[ii]',l[ii])
    a_ptr = l[ii]-1
    # print('ii,a_ptr,a[a_ptr]',ii,a_ptr,a[a_ptr])
    if a[a_ptr] != n: #一番右じゃない
        if l[ii] == k: #一番最後のコマ
            if a[a_ptr]+1 <= n: #右があいている
                a[a_ptr] = a[a_ptr] + 1            
        if l[ii] < k: #一番最後のコマじゃない
            if a[a_ptr]+1 != a[a_ptr+1]: #すぐ右にコマがな
                a[a_ptr] = a[a_ptr] + 1
    # print(a)

ans = ''
for ii in range(k):
    ans=ans+str(a[ii])+' '

print(ans)