# -*- coding: utf-8 -*-
import sys
n,a,b = sys.stdin.readline().split()
sum=0
for ii in range(1,int(n)+1):
    ketasum=0
    for keta in range(len(str(ii))):
        ketasum = ketasum + int(str(ii)[keta])
    if (ketasum>=int(a)) and (ketasum<=int(b)):
        sum = sum + ii
print(sum)