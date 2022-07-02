# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

DEBUG=1

#input
N,X = map(int,input().split())
stage=[]
for kk in range(N):
    a,b = map(int,input().split())
    stage.append([a,b])

if DEBUG==1:
    print(stage)

#最初は必ず実行
time = stage[0][0]+stage[0][1]
# stage[0][1]より、stage[ii][0]+stage[ii][1] が小さければこっちのほうが速い
# stage[0][1]*(X-1)より、stage[ii][0]+stage[ii][1]*(X-1) が小さければこっちのほうが速い
# こうなるステージを探せばよい。


sys.exit()
