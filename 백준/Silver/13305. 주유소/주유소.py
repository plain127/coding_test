n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

result = dis[0]*price[0]

group = []

for i in range(1, n-1):
    a = [price[i], dis[i]]
    group.append(a)
    
group.sort()

result += group[0][0] * (sum(dis)- dis[0])

print(result)