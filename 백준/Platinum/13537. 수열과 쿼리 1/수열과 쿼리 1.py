import sys  

input = sys.stdin.readline 

n = int(input())  
arr = list(map(int, input().split()))  

values = []  

for index, value in enumerate(arr, start=1): 
    values.append((value, index))  

values.sort(reverse=True)  

m = int(input())
queries = []  

for query_id in range(m):
    left, right, k = map(int, input().split())  
    queries.append((k, left, right, query_id)) 

queries.sort(reverse=True) 

size = 1  
while size < n:
    size <<= 1 

tree = [0] * (size * 2)  

def point_update(position):
    node = size + position - 1  
    tree[node] = 1  

    node //= 2  

    while node >= 1: 
        tree[node] = tree[node * 2] + tree[node * 2 + 1]  
        node //= 2 


def range_sum(left, right):  
    left = size + left - 1  
    right = size + right - 1 

    result = 0  

    while left <= right:  
        if left % 2 == 1:  
            result += tree[left]
            left += 1 

        if right % 2 == 0:
            result += tree[right]
            right -= 1  

        left //= 2  
        right //= 2 

    return result  


answers = [0] * m  
value_index = 0  

for k, left, right, query_id in queries:  
    while value_index < n and values[value_index][0] > k:  
        _, position = values[value_index] 
        point_update(position)
        value_index += 1  

    answers[query_id] = range_sum(left, right) 

sys.stdout.write('\n'.join(map(str, answers)))