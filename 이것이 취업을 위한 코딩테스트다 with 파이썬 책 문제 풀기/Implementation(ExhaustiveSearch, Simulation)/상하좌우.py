#내가 푼 풀이
n = int(input())
direction = list(map(str,input().split()))

x = 1
y = 1

for dir in direction:
    if dir == 'L':
        if x > 1:
            x -= 1
    elif dir == 'R':
        if x < n:
            x += 1
    elif dir == 'U':
        if y > 1:
            y -= 1
    elif dir == 'D':
        if y < n:
            y += 1

print(f'{y} {x}')

#책 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = x + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)