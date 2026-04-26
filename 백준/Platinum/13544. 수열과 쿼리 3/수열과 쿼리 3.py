import sys  
from bisect import bisect_right 

input = sys.stdin.readline 

n = int(input())  
arr = list(map(int, input().split()))  

size = 1  

while size < n:
    size <<= 1 

tree = [[] for _ in range(size * 2)]  

for i in range(n): 
    tree[size + i] = [arr[i]] 

for node in range(size - 1, 0, -1): 
    left_list = tree[node * 2]  
    right_list = tree[node * 2 + 1]

    merged = [] 
    left_index = 0 
    right_index = 0 

    while left_index < len(left_list) and right_index < len(right_list):  
        if left_list[left_index] <= right_list[right_index]: 
            merged.append(left_list[left_index])  
            left_index += 1 
        else:  
            merged.append(right_list[right_index]) 
            right_index += 1 

    if left_index < len(left_list):  
        merged.extend(left_list[left_index:])  

    if right_index < len(right_list):  
        merged.extend(right_list[right_index:])  

    tree[node] = merged  


def query(left, right, k):
    left = size + left - 1 
    right = size + right - 1  

    count = 0  

    while left <= right:
        if left % 2 == 1: 
            node_list = tree[left]  
            count += len(node_list) - bisect_right(node_list, k)  
            left += 1  

        if right % 2 == 0: 
            node_list = tree[right]  
            count += len(node_list) - bisect_right(node_list, k)  
            right -= 1  

        left //= 2  
        right //= 2 

    return count  


m = int(input())  
last_ans = 0  
answers = []  

for _ in range(m):
    a, b, c = map(int, input().split())

    left = a ^ last_ans  
    right = b ^ last_ans 
    k = c ^ last_ans  

    last_ans = query(left, right, k) 
    answers.append(str(last_ans)) 

sys.stdout.write('\n'.join(answers)) 