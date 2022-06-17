# -*- coding: utf-8 -*-
import sys
def check(p):
    if (s[p:(p+key_l[0])])==key[0]: #dream
        p2=check(p+key_l[0])
        if len_s==p2:
            return(p2) 
    if (s[p:(p+key_l[1])])==key[1]: #dreamer
        p2=check(p+key_l[1])
        if len_s==p2:
            return(p2) 
    if (s[p:(p+key_l[2])])==key[2]: #erase
        p2=check(p+key_l[2])
        if len_s==p2:
            return(p2) 
    if (s[p:(p+key_l[3])])==key[3]: #eraser
        p2=check(p+key_l[3])
        if len_s==p2:
            return(p2) 
    return(p)

sys.setrecursionlimit(100000)
s = sys.stdin.readline()
key = ['dream','dreamer','erase','eraser']
# key_l = [len(key[0]),len(key[1]),len(key[2]),len(key[3])]
key_l = [5,7,5,6]
len_s = len(s)-1
p=check(0)
if len_s == p:
    print('YES')
else:
    print('NO')