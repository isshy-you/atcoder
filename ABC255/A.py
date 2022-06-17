# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(100000)
a,b = sys.stdin.readline().split()
c,d = sys.stdin.readline().split()
e,f = sys.stdin.readline().split()
s = [c,d,e,f]

print(s[(int(a)-1)*2+int(b)-1])
