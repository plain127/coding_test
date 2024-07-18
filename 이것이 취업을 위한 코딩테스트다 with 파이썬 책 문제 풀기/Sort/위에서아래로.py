# 내가 푼 풀이
n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

for i in arr:
    print(i, end = ' ')