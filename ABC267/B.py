# -*- coding: utf-8 -*-

DEBUG=False
# DEBUG=True

S = input()

if DEBUG : print('INPUT = ',S)

pin=[]
for ii in range(len(S)):
    pin.append(int(S[ii]))

for ii in range(len(S)):
    if DEBUG : print(ii,pin[ii])

blank=[False,False,False,False,False,False,False]

if pin[7-1]==0:
    blank[0]=True
if pin[4-1]==0:
    blank[1]=True
if pin[2-1]==0 and pin[8-1]==0:
    blank[2]=True
if pin[1-1]==0 and pin[5-1]==0:
    blank[3]=True
if pin[3-1]==0 and pin[9-1]==0:
    blank[4]=True
if pin[6-1]==0:
    blank[5]=True
if pin[10-1]==0:
    blank[6]=True

if DEBUG:print(blank)

if pin[1-1]==0:
    if blank[1]==1:
        if not blank[0] and (not blank[2] or not blank[3] or not blank[4] or not blank[5] or not blank[6]):
            print('Yes')
            exit()
    if blank[2]==1:
        if (not blank[0] or not blank[1]) and (not blank[3] or not blank[4] or not blank[5] or not blank[6]):
            print('Yes')
            exit()
    if blank[3]==1:
        if (not blank[0] or not blank[1] or not blank[2]) and (not blank[4] or not blank[5] or not blank[6]):
            print('Yes')
            exit()
    if blank[4]==1:
        if (not blank[0] or not blank[1] or not blank[2] or not blank[3]) and (not blank[5] or not blank[6]):
            print('Yes')
            exit()
    if blank[5]==1:
        if (not blank[0] or not blank[1] or not blank[2] or not blank[3] or not blank[4]) and (not blank[6]):
            print('Yes')
            exit()
print('No')