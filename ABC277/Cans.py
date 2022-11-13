import sys
from collections import defaultdict, deque

DEBUG=False
DEBUG=True

input = sys.stdin.readline

def dprint(str,val):
    if DEBUG : print(str,'=',val)

n = int(input())
graph = defaultdict(list)
for _ in range(n) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

dprint('graph',graph)
que = deque()
que.append(1)
S = {1}
cnt = 0
while que:
    dprint('que',que)
    dprint('S',S)
    v = que.popleft()
    dprint('v',v)
    for i in graph[v]:
        if DEBUG : cnt = cnt + 1
        dprint('i',i)
        if not i in S:
            que.append(i)
            S.add(i)
print(max(S))
dprint('cnt',cnt)