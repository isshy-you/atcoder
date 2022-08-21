# -*- coding: utf-8 -*-
# ACx14 time over 

def move(h,w):
    if DEBUG : print('move():',h,w)
    if h <= H and h >= 1 and w <= W and w>=1:
        dir = line[h-1][w-1]
        move = True
        if DEBUG : print('dir=',dir)
        if (dir == 'U') and h!=1 :
            if DEBUG : print('U:h-1')
            newh = h-1
            neww = w
        elif (dir == 'D') and h!=H :
            if DEBUG : print('D:h+1')
            newh = h+1
            neww = w
        elif (dir == 'L') and w!=1:
            if DEBUG : print('L:w-1')
            newh = h
            neww = w-1
        elif (dir == 'R') and w!=W:
            if DEBUG : print('R:w+1')
            newh = h
            neww = w+1
        else:
            if DEBUG : print('no peration')
            move = False
            newh = h
            neww = w
    else:
        if DEBUG : print('no peration???')
        move = False
        newh = h
        neww = w
    return(move,newh,neww)

DEBUG=False
# DEBUG=True

# 1 <= X <= Y <= 100
# 1 <= N <= 100
H,W = map(int,input().split())

if DEBUG : print('INPUT = ',H,W)

line = []
for ii in range(H):
    line.append(input())

flg = [0]*W*H

if DEBUG : 
    for ii in range(H):
        l = ''
        for jj in range(W):
            l = l + str(flg[ii*W+jj])
        print(ii,l)

# for ii in range(H):
#     if DEBUG : print('H',ii,line[ii])        

posh = 1
posw = 1
success = True
while (success == True):
    flg[(posw-1)+(posh-1)*W] = 1
    if DEBUG : 
        for ii in range(H):
            l = ''
            for jj in range(W):
                l = l + str(flg[ii*W+jj])
            print(ii,l)
    success,posh,posw = move(posh,posw)
    if DEBUG : print('posh,posw =',success,posh,posw)
    if success:
        if flg[(posw-1)+(posh-1)*W]==1:
            print(-1)
            exit()
    else:
        print(posh,posw)
        exit()

print(posw,posh)




exit()

