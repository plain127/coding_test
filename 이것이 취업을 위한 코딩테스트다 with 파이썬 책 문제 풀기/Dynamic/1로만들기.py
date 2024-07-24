# 내가 푼 풀이
x = int(input())

cnt = 0

while True:
    if x % 5 == 0:
        x = x // 5
        cnt += 1
    
    elif x % 3 == 0:
        x = x // 3
        cnt += 1
    
    elif x % 2 == 0:
        x = x // 2
        cnt += 1
    
    else:
        x -= 1
        cnt += 1
    
    if x == 1:
        break
    
print(cnt)