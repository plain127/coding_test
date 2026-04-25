import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)

def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += i & -i

def prefix_sum(i):
    total = 0

    while i > 0:
        total += tree[i]
        i -= i & -i

    return total

for i in range(1,n+1):
    value = int(input())
    arr[i] = value
    update(i, value)

ans = []

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)

    else:
        result = prefix_sum(c) - prefix_sum(b-1)
        ans.append(str(result))

print("\n".join(ans))