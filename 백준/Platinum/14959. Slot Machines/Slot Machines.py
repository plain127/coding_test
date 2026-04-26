import sys  

input = sys.stdin.buffer.readline 

n = int(input()) 
arr = list(map(int, input().split()))  

arr.reverse() 

pi = [0] * n  

best_k = n - 1 
best_p = 1  
best_sum = best_k + best_p

for i in range(1, n):  
    j = pi[i - 1]  

    while j > 0 and arr[i] != arr[j]: 
        j = pi[j - 1]  

    if arr[i] == arr[j]:  
        j += 1  

    pi[i] = j  

    length = i + 1
    p = length - pi[i]
    k = n - length  
    current_sum = k + p

    if current_sum < best_sum:
        best_sum = current_sum 
        best_k = k 
        best_p = p 
    elif current_sum == best_sum and p < best_p:
        best_k = k  
        best_p = p  

print(best_k, best_p)