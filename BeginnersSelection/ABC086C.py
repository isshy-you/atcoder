# -*- coding: utf-8 -*-
# 1_010.txt
# 1_012.txt
import sys

def check2(idx,t1,x1,y1): #(t1,x1,y1)から(t[idx],x[idx],y[idx])のゴールに到達するか
    # print('check2:',idx,t1,x1,y1)
    if t[idx]==t1 and x[idx]==x1 and y[idx]==y1: # ゴールにいるか
        # print('t1,x1,y1=',t1,x1,y1)
        return(t1,x1,y1)
    else:
        t3,x3,y3=check(idx,t1,x1,y1) # 次の探索
        return(t3,x3,y3)

def check(idx,tt,xx,yy): #(tt,xx,yy)から(t[idx],x[idx],y[idx])へ向けて1歩進む
    # print('check :',idx,tt,xx,yy)
    t1=tt+1 # Time increment
    if (t1>t[idx]):return(0,0,0) # Time Over

    if (abs(x[idx]-xx) > abs(y[idx]-yy)): #ｘとｙの近い方を選択
        if (x[idx]==xx):
            # print('check(x+1):',idx,t1,xx+1,yy)
            t2,x2,y2=check2(idx,t1,xx+1,yy)
            if (t2!=0):return(t2,x2,y2)
        elif (x[idx]>xx):
            # print('check(x+1):',idx,t1,xx+1,yy)
            sub=x[idx]-xx
            t2,x2,y2=check2(idx,t1+sub-1,xx+sub,yy)
            if (t2!=0):return(t2,x2,y2)
        else:
            # print('check(x-1):',idx,t1,xx-1,yy)
            sub=xx-x[idx]
            t2,x2,y2=check2(idx,t1+sub-1,xx-sub,yy)
            if (t2!=0):return(t2,x2,y2)
        if (y[idx]==yy):
            t2,x2,y2=check2(idx,t1,xx,yy+1)
            if (t2!=0):return(t2,x2,y2)
        elif (y[idx]>=yy):
            # print('check(y+1):',idx,t1,xx,yy+1)
            sub=y[idx]-yy
            t2,x2,y2=check2(idx,t1+sub-1,xx,yy+sub)
            if (t2!=0):return(t2,x2,y2)
        else:
            # print('check(y-1):',idx,t1,xx,yy-1)
            sub=yy-y[idx]
            t2,x2,y2=check2(idx,t1+sub-1,xx,yy-sub)
            if (t2!=0):return(t2,x2,y2)
    else:
        if (y[idx]==yy):
            t2,x2,y2=check2(idx,t1,xx,yy+1)
            if (t2!=0):return(t2,x2,y2)
        elif (y[idx]>=yy):
            # print('check(y+1):',idx,t1,xx,yy+1)
            sub=y[idx]-yy
            t2,x2,y2=check2(idx,t1+sub-1,xx,yy+sub)
            if (t2!=0):return(t2,x2,y2)
        else:
            # print('check(y-1):',idx,t1,xx,yy-1)
            sub=yy-y[idx]
            t2,x2,y2=check2(idx,t1+sub-1,xx,yy-sub)
            if (t2!=0):return(t2,x2,y2)
        if (x[idx]==xx):
            t2,x2,y2=check2(idx,t1,xx+1,yy)
            if (t2!=0):return(t2,x2,y2)
        elif (x[idx]>=xx):
            # print('check(x+1):',idx,t1,xx+1,yy)
            sub=x[idx]-xx
            t2,x2,y2=check2(idx,t1+sub-1,xx+sub,yy)
            if (t2!=0):return(t2,x2,y2)
        else :
            # print('check(x-1):',idx,t1,xx-1,yy)
            sub=xx-x[idx]
            t2,x2,y2=check2(idx,t1+sub-1,xx-sub,yy)
            if (t2!=0):return(t2,x2,y2)

    return(0,0,0)

sys.setrecursionlimit(1000000000)
s = sys.stdin.readline()
t=[]
x=[]
y=[]
tt=0
xx=0
yy=0
for ii in range(int(s)):
    a,b,c = sys.stdin.readline().split()
    t.append(int(a))
    x.append(int(b))
    y.append(int(c))

for idex in range(int(s)):
    tt,xx,yy=check(idex,tt,xx,yy)
    # print('result=',tt,xx,yy)
    if tt==0:break

if (tt!=0):
    print('Yes')
else:
    print('No')
