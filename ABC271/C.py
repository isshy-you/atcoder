# -*- coding: utf-8 -*-
# ACx22
# WAx7

DEBUG=False
# DEBUG=True

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

N = int(input())
book = input_list()
book.sort()

if DEBUG : print(N,book)

# if N == 1:
#     if book[0]==1:
#         print(1)
#     else:
#         print(0)
#     exit()

ii = 0 # リストのポインタ
num = 1 # 読んでいる巻

while True: # 前から順番に読む 
    if book[ii] != num: # 違ったら、
        if N-2 >= ii: # 後ろ2冊を交換して読めたことにする
            N = N-2
            if DEBUG: print(ii,num,N,"ope")
        else:
            print(num-1)
            exit()
    else: # 一致していれば次
        if DEBUG: print(ii,num,N)
        ii += 1 # 次の本にする
    if ii >= N: break # 本がなくなったら終わり
    num += 1 # 読む巻を増やす

print(num)
exit()

'''
2
1 2
1 2

3
1 3 4
1 2

3
2 4 5
1 2

4
1 3 4 5
1 2 3

5
1 3 4 5 6
1 2 3 4

*
7
1 2 4 6 7 271 272
1 2 3 4 5

8
1 2 4 6 7 271 272 299
1 2 3 4 5 6

8
1 2 4 7 271 272 299 999
1 2 3 4 5 

8
1 4 9 11 13 14 17 55 
1 2 3 4 5
'''