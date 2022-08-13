# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)

def xy(x,y,width):
    return((x)+(y)*(width))

# def line_search(line):
#     kk=0
#     columns=[]
#     while(kk<H1):
#         for ii in range(H2):
#             for jj in range(W2):
#                 if A[xy(jj,ii,H1)] == B[xy(line,kk,H2)]:
#                     columns.append(kk)
#                     kk = kk + 1
#                     if kk == H1:

DEBUG=False
# DEBUG=True

#input
H1,W1 = map(int,input().split())
A=[]
for ii in range(H1):
    tmp = input().split()
    for jj in range(W1):
        A.append(int(tmp[jj]))

H2,W2 = map(int,input().split())

B=[]
for ii in range(H2):
    tmp = input().split()
    for jj in range(W2):
        B.append(int(tmp[jj]))

if DEBUG:
    print(A)
    for ii in range(H1):
        tmp = ''
        for jj in range(W1):
            tmp = tmp + ' ' + str(A[xy(jj,ii,W1)])
        print(tmp)
    print(B)
    for ii in range(H2):
        tmp = ''
        for jj in range(W2):
            tmp = tmp + ' ' + str(B[xy(jj,ii,W2)])
        print(tmp)

# C=[]
# cw = H1
# ch = W1
# for ii in range(H2):
#     line_search(ii)
#     for jj in range(W2):

brow = 0 # H2
bcol = 0 # W2
columns = range(W1)
new_columns = []
while(True):
    for ii in range(H1):
        bcol = 0
        if DEBUG: print('columns=',columns)
        for jj in columns:
            if bcol < W2: 
                if DEBUG: print('ii,jj,A = ',ii,jj,A[xy(jj,ii,W1)])
                if DEBUG: print('bcol,brow,B =',bcol,brow,B[xy(bcol,brow,W2)])
                if A[xy(jj,ii,W1)] == B[xy(bcol,brow,W2)]:
                    if DEBUG: print('Match')
                    if brow == 0:
                        new_columns.append(jj)
                        if DEBUG: print('new_columns = ',new_columns)
                    bcol = bcol + 1
        if bcol == W2: 
            if DEBUG: print('Match LINE')
            brow = brow + 1
            if brow == H2:
                print('Yes')
                sys.exit()
            columns = new_columns
    print('No')
    sys.exit()

# if DEBUG: print(B)



# sys.exit()
