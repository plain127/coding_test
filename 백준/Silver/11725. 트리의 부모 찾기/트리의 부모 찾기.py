import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

for i in range(1, n+1):
    tree[i].sort()

visited = [0]*(n+1)

q = deque()
q.append(1)
visited[1] = -1

while q : 
    s = q.popleft()
    for i in tree[s]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = s

for i in range(2, n+1):
    print(visited[i])