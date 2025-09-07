import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []

for row in range(n):
    for col in range(n):
        if graph[row][col] == 2:
            chicken.append((row, col))

min_dis = int(10**9)
comb = list(combinations(chicken, m))

for c in comb:
    c = list(c)
    total = 0
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 1:
                dis = int(10**9)     
    
                for i in c:
                    ro, co = i
                    dis = min((abs(row-ro) + abs(col-co)), dis)
                total+=dis

    min_dis = min(min_dis, total)


print(min_dis)