import sys
import heapq

input = sys.stdin.readline

n = int(input())
intervals = []

for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    intervals.append((a, b))

d = int(input())

intervals.sort(key=lambda x: x[1])

heap = []
ans = 0

for start, end in intervals:
    if end-start > d:
        continue

    heapq.heappush(heap,start)

    left = end - d

    while heap and heap[0] < left:
        heapq.heappop(heap)

    ans = max(ans, len(heap))

print(ans)