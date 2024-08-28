#내 풀이
n, m = map(int, input().split())
k = list(map(int, input().split()))

arr = [0] * 11
count = 0

for i in k:
    arr[i] += 1
    
for i in range(11):
    for j in arr:
        if arr[i] != j:
            count += arr[i] * j
        
print(count)

#책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1
    
result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n
    
print(result)