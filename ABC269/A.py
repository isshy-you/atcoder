# -*- coding: utf-8 -*-
# ACx10

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

a,b,c,d = map(int,input().split())

if DEBUG : print('input=',a,b,c,d)

print((a+b)*(c-d))
print('Takahashi')
