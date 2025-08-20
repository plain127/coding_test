import sys

input = sys.stdin.readline

k, n = map(int, input().split())    
lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)

while start <= end:
    mid = (start + end)//2

    cnt = sum(l//mid for l in lines)
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)