# -*- coding: utf-8 -*-
import sys
def otoshidama(a,b,c):
    return(10*a+5*b+1*c)

n,y = list(map(int,sys.stdin.readline().split()))
flag = 0
for kk in range(n+1):
    for jj in range(n+1-kk):
            ii = n-jj-kk
            if otoshidama(ii,jj,kk)==y/1000:
                print("{} {} {}".format(ii,jj,kk))
                quit()
print("-1 -1 -1")
