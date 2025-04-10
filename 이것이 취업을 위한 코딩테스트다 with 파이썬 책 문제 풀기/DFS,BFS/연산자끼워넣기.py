#내 풀이
from collections import deque

n = int(input())
a = list(map(int, input().split()))
x = list(map(int, input().split()))
results = []

def bfs(x):
    q = deque()
    q.append(x)


#책 풀이
n = int(input())
#연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
#더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

#최솟값과 최댓값 초기화
min_value = -1e9
max_value = 1e9

#dfs
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    #모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        #각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i +1, int(now / data[i]))
            div += 1
            
dfs(1, data[0])

print(max_value)
print(min_value)
    