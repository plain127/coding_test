import sys

input = sys.stdin.readline

num = list(map(int, input().split()))

sum = 0

for i in range(5):
    sum += num[i] * num[i]

print(sum%10)