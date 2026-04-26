import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

heap = []
answer = 0

for i in range(n):
    x = arr[i] - i

    heapq.heappush(heap, -x)

    if -heap[0] > x:
        answer += -heap[0] - x
        heapq.heappop(heap)
        heapq.heappush(heap, -x)

print(answer)