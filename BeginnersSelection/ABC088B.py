# -*- coding: utf-8 -*-
from posixpath import split
import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
a = list(map(int,a))
a.sort(reverse=True)
alice=0
bob=0
for ii,card in enumerate(a):
    if ii%2 ==0:
        alice = alice + card
    else:
        bob = bob + card
print(alice-bob)