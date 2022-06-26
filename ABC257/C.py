# -*- coding: utf-8 -*-
# AC  x31
# WA  x4
import sys

DEBUG=0
N = int(sys.stdin.readline())
S = sys.stdin.readline()
str = sys.stdin.readline().split()

W=[]
tuples = []
sum=0
for ii in range(N):
    W.append(int(str[ii]))
    s=int(S[ii])
    tuples.append((s,W[ii]))
    sum=sum+int(s)

if sum==N:
    print(3)
    exit(0)
if sum==0:
    print(3)
    exit(0)

# print(tuples)
tuples_sorted = sorted(tuples, key=lambda aa: aa[1])
if (DEBUG==1):print(tuples_sorted)

nummax=sum
flag,last=tuples_sorted[0]
adult=sum
child=0
adult_l=adult
child_l=child
for ii in range(1,N,1):
    flag1,weight1=tuples_sorted[ii-1]
    if flag1 == 0:
        child = child + 1
    else:
        adult = adult - 1
    if last!=weight1:
        if nummax<(child_l+adult_l):
            nummax = child_l+adult_l
        if (DEBUG==1):print(ii-1,child_l,adult_l,nummax,'*')
    else:
        if (DEBUG==1):print(ii-1,child_l,adult_l,nummax)
    last = weight1
    adult_l=adult
    child_l=child
print(nummax)
