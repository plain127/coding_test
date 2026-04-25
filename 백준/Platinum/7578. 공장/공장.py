import sys

input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

pos = {}

for idx, machine in enumerate(first, 1):
    pos[machine] = idx

tree = [0]*(n+1)

def add(idx, value):
    while idx <= n:
        tree[idx] += value
        idx += idx & -idx

def prefix_sum(idx):
    total = 0

    while idx > 0:
        total += tree[idx]
        idx -= idx & -idx
    
    return total

ans = 0
seen = 0

for machine in second:
    idx = pos[machine]
    ans += seen - prefix_sum(idx)

    add(idx, 1)
    seen += 1

print(ans)