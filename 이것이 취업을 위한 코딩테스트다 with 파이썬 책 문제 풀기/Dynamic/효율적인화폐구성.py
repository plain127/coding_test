#내 풀이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

values = [0]*10001

for i in range(1,n+1):
    value = int(input())
    values[value] += 1

counts = [0]*(m+1)

for i in range(1, m+1):

    counts[i] = counts[i-1] + 1 

#책 풀이
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])