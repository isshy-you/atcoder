# -*- coding: utf-8 -*-
import sys

def light(x,y,lx,ly):
    tmp = ((x-lx)**2+(y-ly)**2)**0.5
    # print(tmp)
    return(tmp)


sys.setrecursionlimit(100000)
n,k = map(int,sys.stdin.readline().split())
a=[] #light man
x=[]
y=[]
l=[] #lum
ss = sys.stdin.readline().split()
for kk in range (k):
    a.append(int(ss[kk]))

for nn in range(n):
    xx,yy = sys.stdin.readline().split()
    x.append(int(xx))
    y.append(int(yy))
    l.append(9999999999)

# print('a=',a)
# for nn in range(int(n)):
#     print('nn,x,y',nn,x[nn],y[nn])

for ii in range(k): #light
    for jj in range(n):
        # print(light(x[jj],y[jj],x[a[ii]],y[a[ii]]))
        # print(x[jj],y[jj],x[a[ii]-1],y[a[ii]-1])
        tmp = light(x[jj],y[jj],x[a[ii]-1],y[a[ii]-1])
        # print(x[a[ii]-1],y[a[ii]-1],'-',x[jj],y[jj],':',tmp)
        if (l[jj] > tmp):
            l[jj] = tmp

max = 0
for jj in range(n):
    if (l[jj]>max):
        max = l[jj]

print(max)

