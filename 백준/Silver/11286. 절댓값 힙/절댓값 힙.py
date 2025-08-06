import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
result = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            result.append(0)
            continue
        t = heapq.heappop(heap)
        result.append(t[1])
        continue
    
    heapq.heappush(heap, (abs(x), x))

for r in result:
    print(r)