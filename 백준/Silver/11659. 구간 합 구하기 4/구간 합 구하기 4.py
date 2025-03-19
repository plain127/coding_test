import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0]
graph += list(map(int, input().split()))

for i, num in enumerate(graph):
    if i > 0:
        graph[i] = graph[i-1] + num

results = []

for _ in range(m):
    i, j = map(int, input().split())
    results.append(graph[j] - graph[i-1])

for result in results:
    print(result)