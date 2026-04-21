import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jw = [tuple(map(int, input().split())) for _ in range(n)]
c = [int(input()) for _ in range(k)]

jw.sort(key=lambda x: x[0])

c.sort()

pq = []
result = 0
idx = 0

for bag in c:
    while idx < n and jw[idx][0] <= bag:
        heapq.heappush(pq, -jw[idx][1])
        idx += 1

    if pq:
        result += -heapq.heappop(pq)

print(result)