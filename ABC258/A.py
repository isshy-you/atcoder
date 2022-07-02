# -*- coding: utf-8 -*-
import sys
# n,x = sys.stdin.readline().split()
# a = input().split()

K = int(sys.stdin.readline())

hour = 21 + K // 60
min = K % 60

print('{:d}'.format(hour)+':'+'{:02d}'.format(min))
