import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
tree = []

def dfs():
    if len(tree) == m:
        print(' '.join(map(str, tree)))
        return

    for i in range(1, n+1):
        tree.append(i)
        dfs()
        tree.pop()

dfs()