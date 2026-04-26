import sys 

sys.setrecursionlimit(10 ** 6) 
input = sys.stdin.readline  

n, m, k = map(int, input().split())  
graph = [[] for _ in range(n + 1)]

for worker in range(1, n + 1):
    data = list(map(int, input().split()))  
    graph[worker] = data[1:]

owner = [0] * (m + 1) 

def dfs(worker): 
    for work in graph[worker]: 
        if visited[work]:  
            continue  

        visited[work] = True  

        if owner[work] == 0:  
            owner[work] = worker
            return True  

        previous_worker = owner[work]  

        if dfs(previous_worker):
            owner[work] = worker
            return True  

    return False 


answer = 0  

for worker in range(1, n + 1):  
    visited = [False] * (m + 1) 

    if dfs(worker):  
        answer += 1  

extra = 0 

for worker in range(1, n + 1):
    if extra == k: 
        break  

    visited = [False] * (m + 1)

    if dfs(worker):  
        answer += 1  
        extra += 1  

print(answer)  