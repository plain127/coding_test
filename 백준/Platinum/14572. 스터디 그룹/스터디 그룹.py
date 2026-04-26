import sys

input = sys.stdin.readline


def update_count(mask, delta): 
    bit = mask 

    while bit: 
        low_bit = bit & -bit  
        algorithm_index = low_bit.bit_length() - 1  
        algorithm_count[algorithm_index] += delta  
        bit -= low_bit  

def calculate_efficiency(group_size):  
    union_count = 0  
    common_count = 0 
    
    for known_count in algorithm_count:  
        if known_count > 0:  
            union_count += 1 

        if known_count == group_size:  
            common_count += 1  
    return (union_count - common_count) * group_size 

N, K, D = map(int, input().split())  
students = []  

for _ in range(N):
    known_algorithm_count, skill = map(int, input().split()) 
    algorithms = list(map(int, input().split()))  
    mask = 0 

    for algorithm in algorithms:  
        mask |= 1 << (algorithm - 1) 

    students.append((skill, mask))  

students.sort() 
algorithm_count = [0] * K 
answer = 0  
left = 0

for right in range(N):  
    right_skill, right_mask = students[right]  
    update_count(right_mask, 1)  

    while right_skill - students[left][0] > D:  
        left_mask = students[left][1]  
        update_count(left_mask, -1)  
        left += 1  

    group_size = right - left + 1  
    efficiency = calculate_efficiency(group_size)  

    if efficiency > answer:  
        answer = efficiency  

print(answer)  