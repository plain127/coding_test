import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [-1]*100001

def bfs(n, k):
    q = deque()
    q.append(n)
    graph[n] = 0

    while q:
        v = q.popleft()

        if v == k :
            break

        for i in (v-1), (v+1), (2*v):
            if 0<=i<=100000 and graph[i] == -1:
                if i == 2*v:
                    graph[i] = graph[v]
                    q.appendleft(i)
                else:
                    graph[i] = graph[v] + 1
                    q.append(i)

bfs(n, k)
print(graph[k])