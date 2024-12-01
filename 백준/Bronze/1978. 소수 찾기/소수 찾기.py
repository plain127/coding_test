import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
count = n
for num in nums:
    if num == 1:
        count -= 1
    i = 2
    while i < int(math.sqrt(num)) + 1:
        if num % i == 0:
            count -= 1
            break
        i+=1
        
print(count)