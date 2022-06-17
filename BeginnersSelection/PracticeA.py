# -*- coding: utf-8 -*-
import sys

data = sys.stdin.readline()
a = int(data)
data = sys.stdin.readline()
data1,data2 = data.split()
b = int(data1)
c = int(data2)
sum = a + b + c
data = sys.stdin.readline()
s = data

print("{} {}".format(sum,s))
