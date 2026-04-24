import sys
from bisect import bisect_right

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, k = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()

ch_card = list(map(int, input().split()))

parent = list(range(m+1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

ans = []

for x in ch_card:
    idx = bisect_right(cards, x)
    real_idx = find(idx)

    ans.append(str(cards[real_idx]))

    parent[real_idx] = find(real_idx+1)

print("\n".join(ans))