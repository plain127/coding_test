#내 풀이
n = int(input())
houses = list(map(int, input().split()))
dis = []

for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(houses[i] - houses[j])
    dis.append((houses[i], sum))

dis.sort(key = lambda x : x[1])

print(dis[0][0])

#책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])