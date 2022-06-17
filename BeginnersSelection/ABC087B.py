# -*- coding: utf-8 -*-
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
x = int(sys.stdin.readline())
num = 0
for ii in range(int(a)+1):
    for jj in range(int(b)+1):
        for kk in range(int(c)+1):
            if ((ii)*500+(jj)*100+(kk)*50==int(x)):
                num = num+1
print(num)