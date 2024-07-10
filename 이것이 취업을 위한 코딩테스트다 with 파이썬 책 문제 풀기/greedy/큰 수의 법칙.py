#내가 푼 풀이
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = 0
for i in range(1, m+1):
    if (i%(k+1) == 0):
        result += arr[1]
    else:
        result += arr[0]

print(result)

#책 풀이
#단순한 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
frist = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

#반복수열의 아이디어 반영

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)