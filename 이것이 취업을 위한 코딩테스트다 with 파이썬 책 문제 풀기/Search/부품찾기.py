# 내 풀이
import sys

input = sys.stdin.readline

n = int(input())
products = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == products[mid]:
            return 'yes'
        elif target > products[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 'no'

for target in targets:
    print(binary_search(target, 0, n-1), end=' ')

#책 풀이(이진탐색)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())

array = list(map(int, input().split()))
array.sort()

m = int(input())

x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#책 풀이(계수정렬)
n = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#책 풀이(집합 자료형 이용)
n = int(input())

array = set(int, input().split())

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')