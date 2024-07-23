# 내가 푼 풀이
x = int(input())

cnt = 0

def calc(x, cnt):
    cnt += 1
    if x % 5 == 0:
        x = x / 5
    elif x % 3 == 0:
        x = x / 3
    elif x % 2 == 0:
        x = x / 2
    else:
        x -= 1
    
    if x == 1:
        return cnt

print(cnt)

# 책 풀이 
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])