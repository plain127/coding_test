#내 풀이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dduks = list(map(int, input().split()))

start, end = 0, max(dduks)

result = 0
while start <= end:
    mid = (start + end) // 2

    line = 0

    for dduk in dduks:
        if dduk > mid:
            line += dduk - mid

    if line >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

#책 풀이
n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start<=end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)