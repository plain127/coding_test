import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = []

pos_arr = [0] * n

for i in range(n):
    x = arr[i]

    pos = bisect_left(lis, x)

    if pos == len(lis):
        lis.append(x)
    else:
        lis[pos] = x

    pos_arr[i] = pos

length = len(lis)

answer = []
target_pos = length - 1
last_value = float('inf')

for i in range(n - 1, -1, -1):
    if pos_arr[i] == target_pos and arr[i] < last_value:
        answer.append(arr[i])
        last_value = arr[i]
        target_pos -= 1

        if target_pos < 0:
            break

answer.reverse()

print(length)
print(*answer)