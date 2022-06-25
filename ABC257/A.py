# -*- coding: utf-8 -*-
import sys
str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,x = sys.stdin.readline().split()

moji=''
for ii in range(26):
    for jj in range(int(n)):
        moji = moji + str[ii]

print(moji[int(x)-1])
