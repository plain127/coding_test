import sys  

input = sys.stdin.buffer.readline

n = int(input())

bit = [0] * (n + 1)


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

def range_sum(left, right):  
    return prefix_sum(right) - prefix_sum(left - 1)  

arr = [0] + list(map(int, input().split()))

for index in range(1, n + 1):  
    add(index, arr[index])

m = int(input())

updates = [] 
questions = []
query_id = 0 

for _ in range(m): 
    query = list(map(int, input().split()))  

    if query[0] == 1:
        _, index, value = query 
        updates.append((index, value)) 

    else:  
        _, k, left, right = query
        questions.append((k, left, right, query_id))  
        query_id += 1  

questions.sort()
answers = [0] * query_id  

applied = 0 

for k, left, right, original_id in questions:  
    while applied < k:  
        index, value = updates[applied]  
        diff = value - arr[index]
        arr[index] = value  
        add(index, diff)  
        applied += 1 

    answers[original_id] = range_sum(left, right)  

sys.stdout.write('\n'.join(map(str, answers)))