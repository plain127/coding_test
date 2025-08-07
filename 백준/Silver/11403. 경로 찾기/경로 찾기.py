import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    m = list(map(int, input().split()))
    for j in range(n):
        if m[j] == 0:
            continue
        elif m[j] == 1:
            graph[i].append(j)

def bfs(start):
    q = deque([start])
    visited = [0]*n
    road = [0]*n

    while q:
        d = q.popleft()
        for i in graph[d]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                road[i] = 1

    return road

result = []
for i in range(n):
    result.append(bfs(i))

for row in result:
    print(*row)