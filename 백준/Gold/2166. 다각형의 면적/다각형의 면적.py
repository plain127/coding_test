import sys

input = sys.stdin.readline

n = int(input())
cord = []

for _ in range(n):
    x, y = map(int, input().split())
    cord.append((x,y))

s = 0
for i in range(1, n):
    s += cord[i-1][0] * cord[i][1] - cord[i-1][1] * cord[i][0]

s += cord[n-1][0] * cord[0][1] - cord[n-1][1] * cord[0][0]
s = abs(s) / 2

print(f"{s:.1f}")