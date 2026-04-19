import sys

input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))

left = 0
length = float('inf')
total = 0

for right in range(n):
    total += seq[right]

    while total >= s:
        length = min(length, right-left+1)
        total -= seq[left]
        left += 1

if length == float('inf'):
    print(0)
else:
    print(length)