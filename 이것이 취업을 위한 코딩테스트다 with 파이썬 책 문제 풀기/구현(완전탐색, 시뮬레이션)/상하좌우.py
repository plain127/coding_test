#나의 풀이법
n = int(input())
x, y = 1, 1
plans = list(input().split())

for i in plans:
    if i == 'R':
        if y<n:
            y+=1
    elif i== 'L':
        if y>1:
            y-=1
    elif i == 'U':
        if x>1:
            x-=1
    elif i == 'D':
        if x<n:
            x+=1

print(x, y)

#책 풀이법
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)