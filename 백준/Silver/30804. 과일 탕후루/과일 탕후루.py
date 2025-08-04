import sys
from collections import Counter 

input = sys.stdin.readline

n = int(input())
fruit = list(map(int, input().split()))
max_length = 0
left = 0
count = Counter()

for right in range(n):
    count[fruit[right]] += 1
    
    while len(count) > 2:
        count[fruit[left]] -= 1
        
        if count[fruit[left]] == 0:
            del count[fruit[left]]
        left+=1
    
    max_length = max(max_length, right-left+1)

print(max_length)