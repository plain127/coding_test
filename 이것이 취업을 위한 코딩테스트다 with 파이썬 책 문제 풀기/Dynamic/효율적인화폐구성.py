# 내가 푼 풀이
import sys

n, m = map(int,input().split())

values = []

for i in range(n):
    values.append(int(sys.stdin.readline().rstrip()))
    
values.sort(reverse=True)

d = [0] * 10001

for val in values:
    if m % val == 0:
        d[m] = min(d[val], d[m // val] + 1)
        
# 책 풀이
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])