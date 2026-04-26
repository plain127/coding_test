import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
w = int(input())

events = [(0,0)]

for _ in range(w):
    x, y = map(int, input().split())
    events.append((x,y))

dp = [[-1]*(w+1) for _ in range(w+1)]

def get_dist(car, last, next_case):
    if last == 0:
        if car == 1:
            x1, y1 = 1, 1
        else:
            x1, y1 = n, n
    else:
        x1, y1 = events[last]
    
    x2, y2 = events[next_case]

    return abs(x1-x2)+abs(y1-y2)

def solve(a, b):
    next_case = max(a,b)+1

    if next_case > w:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    cost1 = get_dist(1, a, next_case) + solve(next_case, b)
    cost2 = get_dist(2, b, next_case) + solve(a, next_case)

    dp[a][b] = min(cost1, cost2)

    return dp[a][b]

min_distance = solve(0,0)

path = []

a = 0
b = 0

while max(a,b) < w:
    next_case = max(a,b)+1
    cost1 = get_dist(1, a, next_case) + solve(next_case, b)
    cost2 = get_dist(2, b, next_case) + solve(a, next_case)

    if cost1 <= cost2:
        path.append('1')
        a = next_case
    else:
        path.append('2')
        b = next_case

print(min_distance)
print('\n'.join(path))