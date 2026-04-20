import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0]+list(map(int, input().split()))

    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    dp = [0]*(n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            dp[nxt] = max(dp[nxt], dp[cur]+cost[nxt])
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)
    
    print(dp[w])