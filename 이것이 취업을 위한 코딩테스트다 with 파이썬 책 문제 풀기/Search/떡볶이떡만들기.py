# 내가 푼 풀이
n, m = map(int,input().split())

dducks = list(map(int, input().split()))

dducks.sort(reverse=True)

result_box = []

for h in range(dducks[0]+1):
    result = 0
    
    for dduck in dducks:
        if dduck <= h:
            break
        result += dduck - h

    result_box.append(result)

def binary_search(result_box, m, start, end):
    while start <= end:
        mid = (start + end) // 2

        if result_box[mid] == m:
            return mid
        elif result_box[mid] < m:
            end = mid - 1
        else:
            start = mid + 1
    return mid

print(binary_search(result_box, m, 0, dducks[0]))

# 책 풀이
n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid +1

print(result)