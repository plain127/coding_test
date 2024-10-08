import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
time = [-1]*100001

def bfs(n, k):
    q = deque()
    q.append(n)
    time[n] += 1

    while q:
        v = q.popleft()

        if v == k:
            break

        for i in (v-1), (v+1), (2*v):
            if 0 <= i <= 100000 and time[i] == -1:
                time[i] = time[v] + 1
                q.append(i)

bfs(n, k)
print(time[k])