import sys  

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline  

MOD = 9901 

n, m = map(int, input().split())

if m > n:
    n, m = m, n 

total = n * m 
limit = 1 << m 

dp = [[-1] * limit for _ in range(total + 1)] 


def dfs(pos, mask):  
    if pos == total: 
        if mask == 0:
            return 1 
        return 0 

    if dp[pos][mask] != -1:  
        return dp[pos][mask] 

    result = 0  

    if mask & 1: 
        result = dfs(pos + 1, mask >> 1)  

    else:  
        row = pos // m
        col = pos % m 

        if row + 1 < n: 
            next_mask = (mask >> 1) | (1 << (m - 1))
            result += dfs(pos + 1, next_mask)  

        if col + 1 < m and (mask & 2) == 0:
            next_mask = mask >> 2 
            result += dfs(pos + 2, next_mask) 

    dp[pos][mask] = result % MOD  
    return dp[pos][mask]  


print(dfs(0, 0)) 