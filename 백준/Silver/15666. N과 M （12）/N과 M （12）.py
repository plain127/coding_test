import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
results = []

def dfs(start, seq):
    if len(seq) == m:
        print(*seq)
        return
    
    for i in range(start, len(nums)):
        dfs(i, seq+[nums[i]])

dfs(0, [])