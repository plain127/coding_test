import sys, heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

def deijkstra(start, end):
    INF = int(1e9)
    distance = [INF]*(n+1)
    q = [(0, start)]
    distance[start] = 0

    while q:
        time, node = heapq.heappop(q)

        if time > distance[node]:
            continue

        for nxt, w in graph[node]:
            sums = time + w
            if sums < distance[nxt]:
                distance[nxt] = sums
                heapq.heappush(q, (sums, nxt))

    return distance[end]

s = 0
for i in range(1,n+1):
    a = deijkstra(i, x)
    b = deijkstra(x, i)
    s = max(s, a+b)

print(s)