import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v = int(input())

tree = [[] for _ in range(v+1)]
visited = [-1]*(v+1)

for _ in range(v):
    nums = list(map(int, input().split()))
    root = nums[0]

    i = 1
    while nums[i] != -1:
        child = nums[i]
        weight = nums[i+1]
        tree[root].append((child, weight))
        i += 2

def backtracking(node, dist):
    for child, weight in tree[node]:
        if visited[child] == -1:
            visited[child] = dist + weight
            backtracking(child, dist+weight)

visited[1] = 0
backtracking(1, 0)


leaf = visited.index(max(visited))
visited = [-1]*(v+1)
visited[leaf] = 0
backtracking(leaf, 0)

print(max(visited))