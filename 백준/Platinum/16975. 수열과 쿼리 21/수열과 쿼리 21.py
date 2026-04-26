import sys

input = sys.stdin.buffer.readline 

n = int(input())  
arr = [0] + list(map(int, input().split()))  

bit = [0] * (n + 2)


def add(index, value):  
    while index <= n:  
        bit[index] += value 
        index += index & -index  

def prefix_sum(index):
    total = 0  

    while index > 0: 
        total += bit[index] 
        index -= index & -index  

    return total  

m = int(input())
answer = []  

for _ in range(m): 
    query = list(map(int, input().split()))

    if query[0] == 1: 
        _, i, j, value = query  
        add(i, value)  
        add(j + 1, -value)

    else:  
        _, x = query 
        current_value = arr[x] + prefix_sum(x) 
        answer.append(str(current_value))

sys.stdout.write('\n'.join(answer))