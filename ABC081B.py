# -*- coding: utf-8 -*-
import sys
def check(list,num):
    jj=0
    for ii in range(len_):
        if int(list[ii])%(2**num)!=0:
            jj=jj+1
    if jj==0:
        num=num+1
        return(check(list,num))
    return(num)

len_ = int(sys.stdin.readline())
list = sys.stdin.readline().split()
print(check(list,1)-1)
