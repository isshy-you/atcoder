# -*- coding: utf-8 -*-
# ACx24
# WAx4
# after_contestx0 

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
if lena == lenb : #同じ長さならiaが答え
    if lenc == lena:
        ansid[0]=0
        ansid[1]=1
        ansid[2]=2
        if DEBUG: print('ans0=012')
    else:
        if DEBUG: print('比較桁:',A[0][S][:lenc])
        if int(A[0][S][:lenc]) >= A[2][I]: 
            ansid[0]=0
            ansid[1]=1
            ansid[2]=2
            if DEBUG: print('ans1=012')
        else:
            ansid[0]=2
            ansid[1]=0
            ansid[2]=1
            if DEBUG: print('ans2=201')
else: # 長さが異なれば、min桁で比較
    if DEBUG: print('比較桁:',A[0][S][:lenb])
    if int(A[0][S][:lenb]) >= A[1][I]: 
        if lenc == lenb:
            ansid[0]=0
            ansid[1]=1
            ansid[2]=2
            if DEBUG: print('ans3=012')
        else:
            if DEBUG: print('比較桁:',A[0][S][:lenc])
            if int(A[1][S][:lenc]) >= A[2][I]: 
                ansid[0]=0
                ansid[1]=1
                ansid[2]=2
                if DEBUG: print('ans4=012')
            else:
                ansid[0]=0
                ansid[1]=2
                ansid[2]=1
                if DEBUG: print('ans5=021')
    else:
        if lenc == lenb:
            ansid[0]=1
            ansid[1]=2
            ansid[2]=0
            if DEBUG: print('ans6=120')
        else:
            if DEBUG: print('比較桁:',A[0][S][:lenc])
            if int(A[1][S][:lenc]) >= A[2][I]: 
                ansid[0]=1
                ansid[1]=2
                ansid[2]=0
                if DEBUG: print('ans7=120')
            else:
                ansid[0]=2
                ansid[1]=1
                ansid[2]=0
                if DEBUG: print('ans8=210')

if DEBUG: print(ansid)
print(A[ansid[0]][S]+A[ansid[1]][S]+A[ansid[2]][S])

exit()
