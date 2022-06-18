# -*- coding: utf-8 -*-
#python:TLE
#pypy3:AC

import sys


def lmake(sum):
    sum_tmp=sum-3
    line_list = []
    for ii in range(sum_tmp+1):
        for jj in range(sum_tmp-ii+1):
            for kk in range(sum_tmp-ii-jj+1):
                if (ii+jj+kk==sum-3):
                    # print('*****',ii,jj,kk)
                    line_list.append([ii+1,jj+1,kk+1])
    if line_list==[]:
        line_list.append([0,0,0])
    return(line_list)

# def lcalc(sum):
#     lmap = [1,1,1]
#     for ii in range (1,sum-3+1,1):
        


# def check_line(line,sum):
#     if sum == line[0]+line[1]+line[2]:
#         return(1)
#     else:
#         return(0)

def check_map(map):
    # hsum1 = map[0]+map[1]+map[2]
    # hsum2 = map[3]+map[4]+map[5]
    # hsum3 = map[6]+map[7]+map[8]
    wsum1 = map[0]+map[3]+map[6]
    wsum2 = map[1]+map[4]+map[7]
    wsum3 = map[2]+map[5]+map[8]
    # if h1==hsum1 and h2==hsum2 and h3==hsum3 and w1==wsum1 and w2==wsum2 and w3==wsum3:
    if w1==wsum1 and w2==wsum2 and w3==wsum3:
        return(1)
    else:
        return(0)

sys.setrecursionlimit(1000000)
s = sys.stdin.readline().split()
h1=int(s[0])
h2=int(s[1])
h3=int(s[2])
w1=int(s[3])
w2=int(s[4])
w3=int(s[5])

#print('*****',h1,h2,h3,w1,w2,w3)

# hmax1 = h1 - 2
# hmax2 = h2 - 2
# hmax3 = h3 - 2
# wmax1 = w1 - 2
# wmax2 = w2 - 2
# wmax3 = w3 - 2

num = 0
map = [1,1,1,1,1,1,1,1,1]

h1_list = lmake(h1)
h2_list = lmake(h2)
h3_list = lmake(h3)
# w1_list = lmake(w1)
# w2_list = lmake(w2)
# w3_list = lmake(w3)
# print('*****',h1_list)
# print('*****',h2_list)
# print('*****',h3_list)
# print('*****',w1_list)
# print('*****',w2_list)
# print('*****',w3_list)

for num1,list1 in enumerate(h1_list):
    for num2,list2 in enumerate(h2_list):
        for num3,list3 in enumerate(h3_list):
            map=[list1[0],list1[1],list1[2],list2[0],list2[1],list2[2],list3[0],list3[1],list3[2]]
            num = num + check_map(map)
            # print ('*****',map)

print(num)