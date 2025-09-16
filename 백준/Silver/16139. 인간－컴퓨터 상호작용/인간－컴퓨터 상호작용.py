import sys

input = sys.stdin.readline

s = input().strip()

results = []
p_sum = [0]*2000

q = int(input())
for _ in range(q):
    a, l, r = input().strip().split()
    l, r = int(l), int(r)
    
    for i in range(len(s)):
        if s[i] == a:
            p_sum[i] = p_sum[i-1] + 1
        else:
            p_sum[i] = p_sum[i-1]
            
    results.append(p_sum[r] - p_sum[l-1])

for r in results:
    print(r)