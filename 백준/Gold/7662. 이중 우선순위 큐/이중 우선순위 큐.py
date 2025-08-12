import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False]*k

    for i in range(k):
        s, n = input().strip().split()
        n = int(n)

        if s == 'I':
            heapq.heappush(min_heap, (n,i))
            heapq.heappush(max_heap, (-n,i))
            visited[i] = True

        elif s == 'D':
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            
            elif n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])