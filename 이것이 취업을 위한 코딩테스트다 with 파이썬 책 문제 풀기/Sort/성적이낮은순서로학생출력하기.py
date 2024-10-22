#내가 푼 풀이
n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((int(score), name))

array.sort()

for i in array:
    print(i[1], end=' ')