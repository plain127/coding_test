#내가 푼 풀이
n, m = map(int, input().split())
y, x, dir = map(int, input().split())

steps = [(-1,0), (1, 0), (0, -1), (0, 1)]
map = []
went = []
count = 0

for _ in range(n):
    map.append(list(map(int, input().split())))

while True:
     if dir == 0:
        if (y, x) not in went:
            x = x + steps[0]
            if map[y][x] == 0:
                dir = 3
                went.append((y, x))
                count += 1
            
        

#책 풀이
n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
            
        else:
            break
        turn_time = 0
        
print(count)