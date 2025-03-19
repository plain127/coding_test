import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

distance = [-1]*100001
pre = [-1]*100001

q = deque([])
q.append(n)
distance[n] = 0

while q:
    v = q.popleft()

    if v == k:
        break
    
    for i in (v-1, v+1, v*2):
        if 0<= i <= 100000 and distance[i] == -1:
            q.append(i)
            distance[i] = distance[v] + 1
            pre[i] = v

print(distance[k])

path = []
cur = k
while cur != -1:
    path.append(cur)
    cur = pre[cur]

print(' '.join(map(str, path[::-1])))