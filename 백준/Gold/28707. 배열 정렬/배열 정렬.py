import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
operations = []

for _ in range(m):
    l, r, cost = map(int, input().split())
    operations.append((l-1,r-1,cost))

start = tuple(arr)
target = tuple(sorted(arr))

heap = [(0, start)]
dist = {start: 0}

while heap:
    cur_cost, state = heapq.heappop(heap)

    if cur_cost > dist[state]:
        continue

    if state == target:
        print(cur_cost)
        sys.exit(0)

    for l, r, add_cost in operations:
        next_state = list(state)
        next_state[l], next_state[r] = next_state[r], next_state[l]

        next_state = tuple(next_state)
        next_cost = cur_cost + add_cost

        if next_state not in dist or next_cost < dist[next_state]:
            dist[next_state] = next_cost
            heapq.heappush(heap, (next_cost, next_state))

print(-1)