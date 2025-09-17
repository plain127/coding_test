import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
seq.sort()
x =  int(input())

left = 0
right = n-1

cnt = 0

while left < right:
    k = seq[left] + seq[right]
    if k == x:
        right -= 1
        left += 1
        cnt += 1
    elif k < x:
        left += 1
    else:
        right -= 1

print(cnt)