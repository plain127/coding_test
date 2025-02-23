import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
max_range = max(2*k, n)

graph = [[] for _ in range(max_range+1)]
times = [INF]*(max_range+1)

for i in range(max_range+1):
    if i+1 <= max_range:
        graph[i].append((i+1,1))
    if i-1 >= 0:
        graph[i].append((i-1,1))
    if i*2 <= max_range:
        graph[i].append((i*2, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    times[start] = 0

    while q:
        time, now = heapq.heappop(q)

        if times[now] < time:
            continue

        for next, cost in graph[now]:
            new = time + cost

            if new < times[next]:
                times[next] = new
                heapq.heappush(q, (new, next))

dijkstra(n)

print(times[k])