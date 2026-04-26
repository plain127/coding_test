import sys  

sys.setrecursionlimit(10 ** 6) 
input = sys.stdin.readline  

n, m = map(int, input().split())  
graph = [[] for _ in range(n + 1)] 

for employee in range(1, n + 1):
    data = list(map(int, input().split()))
    graph[employee] = data[1:]  

owner = [0] * (m + 1)  


def dfs(employee):
    for work in graph[employee]:
        if visited[work]: 
            continue  

        visited[work] = True  

        if owner[work] == 0:
            owner[work] = employee  
            return True 

        previous_employee = owner[work]

        if dfs(previous_employee): 
            owner[work] = employee  
            return True  

    return False  


answer = 0  

for employee in range(1, n + 1):  
    visited = [False] * (m + 1)  
    
    if dfs(employee):  
        answer += 1  

print(answer)  