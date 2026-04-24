import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

root = {}

n = int(input())

for _ in range(n):
    data = input().split()
    foods = data[1:]

    cur = root

    for food in foods:
        if food not in cur:
            cur[food] = {}
        cur = cur[food]

def dfs(node, depth):
    for food in sorted(node.keys()):
        print("--"*depth+food)
        dfs(node[food], depth+1)

dfs(root, 0)