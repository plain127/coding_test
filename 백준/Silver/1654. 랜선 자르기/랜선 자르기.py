import sys

input = sys.stdin.readline

k, n = map(int,input().split())

lines = []

for _ in range(k):
    lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    lans = 0
    for line in lines:
        lans += line // mid

    if lans >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
