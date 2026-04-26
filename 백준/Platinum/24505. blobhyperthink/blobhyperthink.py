import sys 
input = sys.stdin.readline  

MOD = 1_000_000_007
TARGET = 11  

n = int(input())
arr = list(map(int, input().split()))  

size = 1  
while size < n: 
    size <<= 1

trees = [[0] * (size * 2) for _ in range(TARGET + 1)]


def point_add(tree, pos, value): 
    if value == 0:  
        return  

    index = size + pos  

    while index > 0: 
        tree[index] += value 

        if tree[index] >= MOD:
            tree[index] -= MOD 

        index >>= 1  

def range_sum(tree, left, right):
    result = 0  

    left += size 
    right += size

    while left < right:
        if left & 1:  
            result += tree[left]  
            left += 1  

        if right & 1:  
            right -= 1 
            result += tree[right]

        left >>= 1 
        right >>= 1  

    return result % MOD 


answer = 0 

for x in arr:
    pos = x - 1 

    ways = [0] * (TARGET + 1) 
    ways[1] = 1 

    for length in range(2, TARGET + 1):
        ways[length] = range_sum(trees[length - 1], 0, pos) 

    for length in range(1, TARGET + 1):
        point_add(trees[length], pos, ways[length])

    answer += ways[TARGET]
    answer %= MOD  

print(answer)  