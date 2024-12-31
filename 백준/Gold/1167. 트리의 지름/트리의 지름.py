import sys
from collections import deque
input = sys.stdin.readline

v = int(input())

tree = [[] for _ in range(v+1)]

for _ in range(v):
    t = list(map(int, input().split()))
    root = t[0]
    for i in range(1, len(t)-1):
        if i % 2 == 0:
            continue
        tree[root].append((t[i], t[i+1]))


def bfs(start, v, tree):
    far = start
    max_dia = 0
    visited = [False]*(v+1)
    visited[start] = True
    q = deque()
    q.append((start, 0))

    while q:
        s, d = q.popleft()
        
        if d > max_dia:
            max_dia = d
            far = s

        for n, w in tree[s]:
            if not visited[n]:
                visited[n] = True
                q.append((n, d+w))
    
    return far, max_dia

a, _ = bfs(1, v, tree)
b, diameter = bfs(a, v, tree)

print(diameter)