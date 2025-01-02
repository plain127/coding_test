#내 풀이
import sys

input = sys.stdin.readline

n = int(input())
arrs = list(map(int, input().split()))

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if arrs[mid] == mid:
            return mid
        elif arrs[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

print(binary_search(0, n-1))

#책 풀이
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)
    
n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index==None:
    print(-1)
else:
    print(index)