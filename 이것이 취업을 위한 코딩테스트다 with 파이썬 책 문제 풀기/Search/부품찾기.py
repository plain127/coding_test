# 내가 푼 풀이
import sys

n = int(input())

items = list(map(int, sys.stdin.readline().split()))
    
m = int(input())

targets = list(map(int, sys.stdin.readline().split()))
    
def binary_search(items, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        if items[mid] == target:
            return 'yes'
        elif items[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 'no'

for target in targets:
    print(binary_search(items, target, 0, n-1), end = ' ')
    
# 이진탐색 외 책 풀이
# 계수정렬
n = int(input())
items = [0] * 1000001

for i in input().split():
    items[int(i)] = 1
    
m = int(input())

targets = list(map(int, input().split()))

for target in targets:
    if items[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
        
# 집합 자료형
n = int(input())

items = set(map(int, input().split()))

m = int(input()) 

targets = list(map(int, input().split()))

for target in targets:
    if target in items:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')