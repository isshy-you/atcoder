# -*- coding: utf-8 -*-
DEBUG=False
# DEBUG=True

hex = '0123456789ABCDEF'
N = int(input())
if DEBUG : print(N)

a = N // 16
b = N % 16
c = a % 16
if DEBUG : print(a)
if DEBUG : print(b)
if DEBUG : print(c)

print(hex[c]+hex[b])
