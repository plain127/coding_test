#내가 맨 처음 푼 풀이
N = int(input())
M = int(input())
K = int(input())
data = []
result = 0

for i in range(N):
    number = int(input())
    data.append(number)
            
    data.sort()

for i in range(M):
    count = (i+1)%K
    if count == 0:
        result += data[N-2]
    else: 
        result += data[N-1]
                

print(result)



#단순한 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
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

count = int(m/(k+1))*K
count += m % (k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)
