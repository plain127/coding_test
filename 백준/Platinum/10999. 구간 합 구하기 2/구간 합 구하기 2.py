import sys  

input = sys.stdin.buffer.readline 

n, m, k = map(int, input().split())

bit1 = [0] * (n + 1)
bit2 = [0] * (n + 1)

prev = 0  

for i in range(1, n + 1):
    current = int(input())
    diff = current - prev 

    bit1[i] = diff  
    bit2[i] = diff * (i - 1)  

    prev = current 

for i in range(1, n + 1):
    next_i = i + (i & -i)

    if next_i <= n:  
        bit1[next_i] += bit1[i]  
        bit2[next_i] += bit2[i]  


def add(bit, index, value):  
    while index <= n:  
        bit[index] += value 
        index += index & -index 

def sum_bit(bit, index):  
    total = 0  

    while index > 0:
        total += bit[index]
        index -= index & -index

    return total  


def prefix_sum(index):
    s1 = sum_bit(bit1, index) 
    s2 = sum_bit(bit2, index) 
    return s1 * index - s2  


def range_add(left, right, value):
    add(bit1, left, value)  
    add(bit2, left, value * (left - 1))

    if right + 1 <= n: 
        add(bit1, right + 1, -value) 
        add(bit2, right + 1, -value * right) 

answer = []  

for _ in range(m + k):
    query = list(map(int, input().split()))  

    if query[0] == 1:  
        _, b, c, d = query  
        range_add(b, c, d)  

    else:  
        _, b, c = query  
        result = prefix_sum(c) - prefix_sum(b - 1)  
        answer.append(str(result)) 

sys.stdout.write('\n'.join(answer))  