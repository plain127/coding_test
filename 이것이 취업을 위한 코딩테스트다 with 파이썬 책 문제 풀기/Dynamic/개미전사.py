# 내가 푼 풀이
n = int(input())

food = list(map(int, input().split()))

d = [0] * 100

for i in range(n):
    if i == 0 or i == 1:
        d[i] = food[i]
    
    d[i] = max(d[i - 1], d[i - 2] + food[i])
               
    
print(d[n-1])

#책 풀이
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = array[1]
for i in range(2,n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    
print(d[n - 1])