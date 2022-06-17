# -*- coding: utf-8 -*-
import sys



sys.setrecursionlimit(100000)
x,a,d,n = map(int,sys.stdin.readline().split())
# x : 整数 6
# a : 初項 2
# d : 公差 3
# n : 項数 3
# S : a + d*(n-1)
# S : 2,5,8 
# print(x,a,d,n)

start = a
end = a + d*(n-1)
# print('###',start,end,x)
if (start == end): # d==0
    if (start == x):
        print(0)
    elif (x > start):
        print(x-start)
    elif (x < start):
        print(start-x)
elif (start < end): # d>0
    if (x > start and x < end): # start < x < end
        low = ((x-start)//d)*d+a
        high = ((x-start)//d+1)*d+a
        # print(low,high)
        if (x-low < high-x):
            print(x-low)
        else:
            print(high-x)
    elif (x < start):
        print(start-x)
    elif (x > end):
        print(x-end)
    else:
        print(0)
elif (start > end): # d<0
    if ((x < start) and (x > end)): # start > x > end
        high = ((start-x)//(-d))*d+a
        low = ((start-x)//(-d)+1)*d+a
        # print(low,high)
        if ((x-low) < (high-x)):
            print(x-low)
        else:
            print(high-x)
    elif (x > start):
        print(x-start)
    elif (x < end):
        print(end-x)
    else:
        print(0)

else: # no operation
    print(0)