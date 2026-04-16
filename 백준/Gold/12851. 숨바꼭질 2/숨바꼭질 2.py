import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1]*100001
method = [0]*100001
q = deque([n])

dist[n] = 0
method[n] = 1


while q:
    x = q.popleft()

    for nx in x-1, x+1, 2*x:
        if 0 <= nx < 100001:
            if dist[nx] == -1:
                dist[nx] = dist[x]+1
                q.append(nx)
                method[nx] = method[x]
            elif dist[nx] == dist[x]+1:
                method[nx] += method[x]

print(dist[k])
print(method[k])