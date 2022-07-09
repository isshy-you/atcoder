# -*- coding: utf-8 -*-
# ACx28
# WAx4
import sys
import math

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

S = sys.stdin.readline()
T = sys.stdin.readline()

if DEBUG==1:
    # print('{}N歳のとき{}Tcmになった'.format(N,T))
    # print('{}M歳の身長cmは？'.format(M))
    # print('{}X歳まで身長が毎年{}Dcm伸びた'.format(X,D))
    print('S:',S[:-1])
    print('T:',T[:-1])
start=[]
goal=[]
if S[0]==T[0] and S[1]==T[1]: #最初は同じなら
    flag = 0
    sp = 2
    for tp,ss in enumerate(T[:-1]):
        if tp>=2:
            if S[sp-1]==S[sp-2]:
                flag = 1
                if DEBUG==1:print('flagON',sp,tp,ss)
            else:
                flag = 0
                if DEBUG==1:print('flagOFF',sp,tp,ss)
            if S[sp]!=T[tp]:
                if DEBUG==1:print(S[sp],T[tp])
                if flag!=1:
                    if DEBUG==1:print('flag',flag)
                    print('No')
                    sys.exit()
                if sp==len(S)-2 and S[sp]!=T[tp+1]:
                    if DEBUG==1:print('last sp is differ')
                    print('No')
                    sys.exit()
            else: #文字が同じなら次の文字へ
                if (sp < len(S)-2):
                    if DEBUG==1:print('sp++')
                    sp = sp + 1

        # if DEBUG==1:
        #     print('sp,tp,ss',sp-1,tp,ss)

else:
    print('No')
    sys.exit()
print('Yes')    

sys.exit()
