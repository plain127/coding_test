#내 풀이
n = int(input())
change = list(map(int, input().split()))
change.sort()


#책 풀이
n = int(input())
data = list(map(int, input().split()))

target = 1
for x in data:
    if target < x:
        break
    target += x
    

print(target)