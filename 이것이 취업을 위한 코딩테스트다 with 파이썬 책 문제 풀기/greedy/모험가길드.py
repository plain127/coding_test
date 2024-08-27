# 내가 푼 풀이
n = int(input())
x = list(map(int, input().split()))
x.sort(reverse=True)

count = 0
i = 0

while i < n:
    for j in range(1, n + 1):
        if x[i] == j:
            count += 1
            i = j               
        else:
            continue
        
print(count)    

# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)