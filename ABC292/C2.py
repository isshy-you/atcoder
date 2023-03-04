# -*- coding: utf-8 -*-
# ACx11,TLEx15

import sys

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

DEBUG=False
# DEBUG=True

inp = input_list()
N = inp[0]
dprintn('N',N)

def calc(n):
    ans = 0
    tmp = 0
    for ii in range(1,n+1,1):
        if ii == tmp:
            break
        if n%ii==0:
           dprintn('pair',[ii,n//ii])
           tmp = n//ii
           if ii == tmp:
               ans = ans + 1
               break
           else:
               ans = ans + 2
    return(ans)

ans = []
num = 0
dprint('ans',ans)
for ii in range(1,(N)//2+1,1): ### 半分だけ回す
    tmp2 = calc(ii) ### A*B の数
    dprint('tmp2',tmp2)
    tmp3 = calc(N-ii) ### C*D の数
    dprint('tmp3',tmp3)
    if ii == N-ii: ### A*B == C*D 両方同じなら1倍
        num = num + tmp2*tmp3
    else:
        num = num + tmp2*tmp3*2
    dprint('num',num)

print(num)

