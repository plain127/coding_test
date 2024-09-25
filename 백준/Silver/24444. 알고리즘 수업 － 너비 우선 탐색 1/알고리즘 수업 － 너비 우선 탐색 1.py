import sys
from collections import deque

input = sys.stdin.readline
#in_file = open('input.txt', 'r')

def bfs(graph, start, visited):
    global count
    queue = deque([start])

    visited[start] = count
    count+=1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = count
                count+=1

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

count = 1

bfs(graph, r, visited)

for i in range(1,n+1):
    print(visited[i])