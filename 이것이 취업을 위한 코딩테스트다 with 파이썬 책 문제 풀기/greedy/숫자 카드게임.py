#내가 푼 풀이법
n, m = map(int,input().split())

mat = []

for i in range(n):
    data = list(map(int,input().split()))
    data.sort()
    if len(data) == m:
        mat.append(data)

num = mat[0][0]

for i in range(1,n):
    if mat[i][0] > mat[i-1][0]:
        num = mat[i][0]

print(num)

#min() 함수를 이용한 답안
n, m = map(int, input.split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

#반복문 구조를 이용한 답안
n, m = map(int, input().split)

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)