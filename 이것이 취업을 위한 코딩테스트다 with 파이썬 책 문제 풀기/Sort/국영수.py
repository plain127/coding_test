#내 풀이
n = int(input())
data = []

for _ in range(n):
    name, k, e, m = input().split()
    data.append((name, int(k), int(e), int(m)))

data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])

