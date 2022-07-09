# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)

DEBUG=0

#input
# n,x = sys.stdin.readline().split()
# a = input().split()
# N,Q = map(int,input().split())
# S = sys.stdin.readline()
# N = int(sys.stdin.readline())
# A=[]
# for kk in range(N):
#     A.append(sys.stdin.readline())

N,M,X,T,D = map(int,input().split())
if DEBUG==1:
    print('{}N歳のとき{}Tcmになった'.format(N,T))
    print('{}M歳の身長cmは？'.format(M))
    print('{}X歳まで身長が毎年{}Dcm伸びた'.format(X,D))
    # print(N,M,X,T,D)
    # print(N,'year',T,'cm',D,'cm/year','~',X,'year')
    # print(M,'year = ?cm')


if N <= X:
    if (N>=M):
        tall = T - D*(N-M)
    elif (X>=M):
        tall = T + D*(M-N)
    else: # X<<
        tall = T + D*(X-N)
else: # N>X
    if (X>=M):
        tall = T - D*(X-M)
    elif (N>M):
        tall = T
    else:
        tall = T
print(tall)
sys.exit()

# if (M>N): #年齢が未来の場合
#     if (M>=X): #身長が止まったあとか
#         tall = T + D*(X-N)
#         if DEBUG==1:
#             print('M>N,M>=X',M,N,M,X,tall)
#     else: #M<X

# elif M==N:
#     tall = T
#     if DEBUG==1:
#         print('M==N',M,N,tall)
# else:# M<N
#     if (M>=X):
#         tall = T
#         if DEBUG==1:
#             print('M<N, M>=X',M,N,M,X,tall)
#     else:# M<X
#         tall = T + D*(M-N)
#         if DEBUG==1:
#             print('M<N, M<X',M,N,M,X,tall)

print(tall)
sys.exit()
