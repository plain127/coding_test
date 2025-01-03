#내 풀이
import sys

input = sys.stdin.readline

n, c = map(int,input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()

def binary_search(houses, start, end):
    mid = (start + end) // 2

    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]
    
    if count >= c:
        global result
        start = mid + 1
        result = mid
    else:
        end = mid - 1

start = 1
end = houses[-1] - houses[0]
result = 0

binary_search(houses, start, end)
print(result)

#책 풀이
n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[i]
    count = 1

    for i in range(1,n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)