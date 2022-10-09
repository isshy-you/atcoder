# -*- coding: utf-8 -*-
# ACx8 WAx14 TLEx4

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

KMAX = 300000
T = int(input())
if DEBUG : print('T=',T)

# 最初の１から最後の１までの幅がKより大きかったらNo
# 最初の１から最後の１までの間に０があったらNo
# 
# 
# 


for ii in range(T):
    result = False
    N,K = input_list()
    S = input()
    lenS = len(S)
    if DEBUG : print('N,K =',N,K)
    if DEBUG : print('S =','<'+S+'>('+str(lenS)+')')
    num1 = 0
    start1 = -1
    end1 = KMAX
    startq = -1
    endq = KMAX
    for jj in range(lenS):
        if S[jj]=='1':
            num1 += 1
            if start1 == -1:
                start1 = jj
            elif end1 < jj or end1 == KMAX:
                end1 = jj
        if S[jj]=='?':
            if startq == -1:
                startq = jj
            elif endq < jj or endq == KMAX:
                endq = jj
        if S[jj]=='0':
            if start1 != -1 and end1 !=1 and start1+K>jj: # 1が始まっていて1の終わりの前に0があったらNo
                if DEBUG:print('1と1の間に0')
                print('No')
                result = True

    if not result:
        if num1 == 1:
            end1 = start1

        if DEBUG : print('mum1 =',num1)
        if DEBUG : print('start1,end1 =',start1,end1)
        if DEBUG : print('startq,endq =',startq,endq)

        width1 = end1 - start1 + 1 # 最初の1から最後の1まで
        if end1 != KMAX and width1 > K:
            if DEBUG:print('1と1の間が長い')
            print('No')
            result = True
        elif width1 == K:
            if DEBUG: print('幅がKと同じ')
            print('Yes')
            result = True
        elif start1 < startq:
            count = 0
            pos = start1
            while(pos < N and (not result)):
                if S[pos]=='1' or S[pos]=='?':
                    count += 1
                    if count == K:
                        if pos+1 < N:
                            if S[pos+1]=='0' or S[pos+1]=='?':
                                if DEBUG:print('1開始で判断',count)
                                print('Yes')
                                result = True
                        else:
                            if DEBUG:print('1開始で判断',count)
                            print('No')
                            result = True
        else:
            # start1とend1の間に0は無い
            # start1から左へ?がいくつ連即するか:front
            count = 0
            countq = 0
            pos = startq
            yes = 0
            front = 0
            frontcnt = 0
            rear = 0
            rearcnt = 0
            while(pos < N and (not result)):
                if front == 0:
                    if S[pos] == '?':
                        frontcnt = frontcnt+1
                    elif S[pos] == '1':
                        front = frontcnt
                        pos = end1
                    elif S[pos] == '0':
                        frontcnt = 0
                elif rear == 0:
                    if S[pos] == '?':
                        rearcnt = rearcnt+1
                    else:
                        rear = rearcnt
                else:
                    break
                pos = pos+1

            if front > 0 and rear > 0:
                if DEBUG:print('?開始で判断:前後に?がある',width1,front,rear)
                print('No')
                result = True
            elif width1 + front <= K or width1 + rear <= K:
                if DEBUG:print('?開始で判断',width1,front,rear)
                print('Yes')
                result = True




# test case
'''
1
6 3
?1?0?1

1
9 3
01?1??1?0


1
3 1
10?

1
3 1
01?

1
3 1
0?1

1
3 2
1??

1
4 2
?1?0

1
6 3
011?1?

1
10 5
00?1???10?


4
3 2
1??
4 2
?1?0
6 3
011?1?
10 5
00?1???10?

'''