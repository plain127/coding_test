# 내가 푼 풀이 == 책 풀이
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + 2 * d[i - 2]
    
result = d[n] % 796796

print(result)


