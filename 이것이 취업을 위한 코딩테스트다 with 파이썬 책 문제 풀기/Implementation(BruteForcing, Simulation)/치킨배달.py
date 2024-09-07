#내 풀이
n, m = map(int, input().split())

district = []
for _ in range(n):
    district.append(list(map(int, input().split())))

def distance(home, chicken):
    x_dis = abs(home[1] - chicken[1])
    y_dis = abs(home[0] - chicken[0])
    return x_dis + y_dis

homes = []
chickens = []

for row in range(n):
    for col in range(n):
        if district[row][col] == 1:
            homes.append((row, col))
        elif district[row][col] == 2:
            chickens.append((row, col))



home2chicken = []
chicken_name = {}

for home in homes:
    result = 0
    i = 0
    while True:
        dist = distance(home, chickens[i])
        if result > dist:
            result = dist
            chick = i
        i += 1
        if i > len(chickens):
            home2chicken.append(result)
            chicken_name.add(chicken_name)

# 책 풀이
from itertools import combinations

n, m = map(int,input().split())
chicken, house = [], [] 

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))
            
candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e-9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result) 

