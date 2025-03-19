import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
results = []

for _ in range(n):
    x = int(input())
    
    if x > 0:
        heapq.heappush(q,(-x,x))
    elif x==0:
        if q:
            _, val = heapq.heappop(q)
            results.append(val)
        else:
            results.append(0)

for result in results:
    print(result)