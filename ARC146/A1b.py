# -*- coding: utf-8 -*-
# ACx28
# WAx0
# after_contestx1 
#  3
#  326 32 3
#  ans =326323 => 332326

DEBUG=False
# DEBUG=True

N=int(input())
A=[]
B=[]
C=[]
IN = input().split()
length = 0
for ii in range(N):
    # A.append(int(IN[ii]))
    # A.append([int(IN[ii]),IN[ii]])
    length = length + len(IN[ii])
    A.append([int(IN[ii]),IN[ii]])
    # B.append([len(IN[ii]),IN[ii],int(IN[ii])])

# A.sort()
A.sort(reverse=True)
# B.sort(reverse=True)
if DEBUG : print('input:',N,A,length)
# if DEBUG : print('input:',N,B,length)

I = 0
S = 1

max = 0
ans = ''
num = 0

lena = len(A[0][S])
lenb = len(A[1][S])
lenc = len(A[2][S])
ansid = [-1,-1,-1]
if lena == lenb : # 0>=1 ans0xx=x0x1x
    if lenb == lenc: # 0>=1 and 1>=2 ans00x=012
        ansid[0]=0
        ansid[1]=1
        ansid[2]=2
        if DEBUG: print('ans000=012')
    else: # 0>=1 and (1)!=(2) ans01x=x01x
        if DEBUG: print('比較桁01x:',A[0][S][:lenc])
        if int(A[0][S][:lenc]) >= A[2][I]: # 0>=2 ans010=012
            ansid[0]=0
            ansid[1]=1
            ansid[2]=2
            if DEBUG: print('ans010=012')
        else: # 0<2 ans011=201
            ansid[0]=2
            ansid[1]=0
            ansid[2]=1
            if DEBUG: print('ans011=201')
else: # (0)!=(1) ans1xx
    if lenb == lenc: #(1)==(2) 1>=2 ans10x=x1x2x
        if DEBUG: print('比較桁10x:',A[0][S][:lenb])
        if int(A[0][S][:lenb]) >= A[1][I]: # 1>=2 and 0>=1 ans100=012
            ansid[0]=0
            ansid[1]=1
            ansid[2]=2
            if DEBUG: print('ans100=012')
        else: # 1>=2 and 0<1 ans101x=1x2x
            if DEBUG: print('比較桁101x:',A[0][S][:lenc])
            if int(A[0][S][:lenc]) >= A[2][I]: # 1>=2 and 0<1 and 0>=2 ans1010=102
                ansid[0]=1
                ansid[1]=0
                ansid[2]=2
                if DEBUG: print('ans110=102')
            else: # 1>=2 and 0<1 and 0<2 ans1011=120
                ansid[0]=1
                ansid[1]=2
                ansid[2]=0
                if DEBUG: print('ans111=120')
    else: #(0)!=(1) and (1)!=(2) ans11xx
        if DEBUG: print('比較桁11xx:',A[0][S][:lenb])
        if int(A[0][S][:lenb]) >= A[1][I]: # 0>=1 ans110x=x0x1x
            if DEBUG: print('比較桁110x:',A[1][S][:lenc])
            if int(A[1][S][:lenc]) >= A[2][I]: # 0>=1 and 1>=2 ans1100=012
                ansid[0]=0
                ansid[1]=1
                ansid[2]=2
                if DEBUG: print('ans1100=012')
            else: # 0>=1 and 0>=2 and 1<2  ans1101x = x0x1
                if DEBUG: print('比較桁1101:',A[0][S][:lenc])
                if int(A[0][S][:lenc]) >= A[2][I]: # 0>=1 and 1>=2 and 0>=2 ans11010=021
                    ansid[0]=0
                    ansid[1]=2
                    ansid[2]=1
                    if DEBUG: print('ans11010=021')
                else: # 0>=1 and 1>=2 and 0<2 ans11011=201
                    ansid[0]=2
                    ansid[1]=0
                    ansid[2]=1
                    if DEBUG: print('ans11011=201')
        else:  # 0<1 ans111xx=x1x0x
            if DEBUG: print('比較桁111xx:',A[1][S][:lenc])
            if int(A[1][S][:lenc]) >= A[2][I]: # 0<1 and 1>=2 ans1110x=1x0x
                if DEBUG: print('比較桁1110x:',A[0][S][:lenc])
                if int(A[0][S][:lenc]) >= A[2][I]: # 0<1 and 1>=2 and 0>=2 ans11100=102
                    ansid[0]=1
                    ansid[1]=0
                    ansid[2]=2
                    if DEBUG: print('ans11100=012')
                else: # 0<1 and 1>2 and 0<2 ans11101=120
                    ansid[0]=1
                    ansid[1]=2
                    ansid[2]=0
                    if DEBUG: print('ans11101=120')
            else: # 0<1 and 1<2 ans11110=210
                ansid[0]=2
                ansid[1]=1
                ansid[2]=0
                if DEBUG: print('ans11110=210')

if DEBUG: print(ansid)
print(A[ansid[0]][S]+A[ansid[1]][S]+A[ansid[2]][S])

exit()
