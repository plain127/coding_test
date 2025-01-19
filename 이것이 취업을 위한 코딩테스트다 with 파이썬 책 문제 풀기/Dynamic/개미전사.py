#내 풀이
import sys

input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))

count = [0]*1001
count[0] = k[0]
count[1] = k[1]
for i in range(2, n):
    count[i] = k[i] + count[i-2]
    
print(max(count))

#책 풀이
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])