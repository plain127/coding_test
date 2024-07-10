#내가 푼 풀이
n, m = map(int, input().split())

result = []
for i in range(n):
    num = list(map(int, input().split()))
    num.sort()
    result.append(num[0])

print(max(result))

#책 풀이
#min() 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

#2중 반복문
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)
print(result)