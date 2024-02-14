#내가 푼 풀이
n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

for i in range(k):
    if(a[i] < b[n-i-1]):
        a[i] = b[n-i-1]
    else:
        break

sum = 0
for i in a:
    sum += i

print(sum)

#책 풀이
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))