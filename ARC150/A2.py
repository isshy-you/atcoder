# -*- coding: utf-8 -*-
# ACx6 WAx20

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
# if DEBUG : print('T=',T)

# 最初の１から最後の１までの間に０があったらNo             xx1xx0xx1xx
# 最初の１から最後の１までの[幅]がKより大きかったらNo        1234567    K]=7 
# 最初の１から[前]の連続する？を見る。                     xxx???1xxxx1????   front=3 , width=6
# 最後の１から[後]の連続する？を見る。                     xxx???1xxxx1????   rear=4   
#   [幅]+[前]+[後] = K なら、Yes
#   [前]>0 かつ [後]>0 なら、２通り以上あるから、No
#   [幅]+[前] >= K なら、Yes
#   [幅]+[後] >= K なら、Yes


for ii in range(T):
    result = False
    N,K = input_list()
    S = input()
    lenS = len(S)
    if DEBUG : print('N,K =',N,K)
    if DEBUG : print('S =',''+S+'>('+str(lenS)+')')
    num1 = 0
    start1 = -1
    end1 = KMAX
    startq = -1
    endq = KMAX
    zero = False
    for jj in range(lenS):
        if S[jj]=='1':
            num1 += 1
            if start1 == -1:
                start1 = jj
            elif end1 < jj or end1 == KMAX:
                end1 = jj
                if zero: # 1が始まっていて1の終わりの前に0があったらNo
                    if DEBUG:print('1と1の間に0')
                    print('No')
                    result = True
        if S[jj]=='?':
            if startq == -1:
                startq = jj
            elif endq < jj or endq == KMAX:
                endq = jj
        if S[jj]=='0':
            if start1 != -1 and end1 == -1: # 1が始まっていて0があったら True
                zero = True

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
        else:
            # start1とend1の間に0は無い
            # start1から左へ?がいくつ連即するか:front
            # end1から右へ?がいくつ連即するか:rear
            if startq < start1: # 前に？があれば
                front = -1
                frontcnt = 0
                pos = startq
                count = 0
                while(pos < N and (not result)):
                    if front == -1:
                        if S[pos] == '?':
                            frontcnt = frontcnt+1
                        elif S[pos] == '1':
                            front = frontcnt
                            pos = end1
                        elif S[pos] == '0':
                            frontcnt = 0
                    pos = pos+1
                front = frontcnt
            else:
                front = 0

            if endq > end1:
                rear = -1
                rearcnt = 0
                pos = end1 + 1
                while(pos < N and (not result)):
                    if rear == -1:
                        if S[pos] == '?':
                            rearcnt = rearcnt + 1
                        elif S[pos] == '0':
                            rear = rearcnt
                    pos = pos+1
                rear = rearcnt
            else:
                rear = 0

            if DEBUG: print('front,rear=',front,rear)
            if front + rear + width1 == K:
                if DEBUG:print('幅＋前＋後=K',width1,front,rear)
                print('Yes')
                result = True
            elif front > 0 and rear > 0:
                if DEBUG:print('前後に?がある',width1,front,rear)
                print('No')
                result = True
            elif width1 + front >= K or width1 + rear >= K:
                if DEBUG:print('前か後ろのどちらかと幅がK以上',width1,front,rear)
                print('Yes')
                result = True
            else:
                print('No')
                result = True




# test case
'''
1
10 10
0?11?11?10

No

1
10 9
0?11?11?10

No

1
10 8
0?11?11?10

Yes

1
10 8
0?11?11??0

Yes

1
6 3
?1?0?1

No

1
9 3
01?1??1?0

No

1
3 1
10?

Yes

1
3 1
01?

Yes

1
3 1
0?1

Yes

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