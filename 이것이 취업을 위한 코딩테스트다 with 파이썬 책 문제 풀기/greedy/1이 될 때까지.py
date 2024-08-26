# 내가 푼풀이
n, k = map(int, input().split())

count = n%k

while True:
    n = n//k
    count += 1
    if n == 1:
        break

print(count) 

# 책 풀이
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k)*k
    result += (n - target)
    n = target
    
    if n < k:
        break
    
    result += 1
    n //= k
    
result += (n - 1)
print(result)