#내가 푼 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0

for i in range(1, k + 1):
    result += data[0]
             
m_num = int(m // k)
k_num = int(m % k)

result = m_num * result
result += data[1] * k_num

print(result)

# 책 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1) * k)
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)