n = int(input())

dis = list(map(int, input().split()))
price = list(map(int, input().split()))

result = dis[0]*price[0]

min_price = price[0]

for i in range(1, n-1):
    if price[i] < min_price:
        min_price = price[i]
    result += min_price * dis[i]

print(result)