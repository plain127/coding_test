import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
results = []
for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(q, x)
    elif x == 0:
        if len(q) == 0:
            results.append(0)
            continue
        
        results.append(heapq.heappop(q))

for result in results:
    print(result)