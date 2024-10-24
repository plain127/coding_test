# 내가 푼 풀이
n = int(input())

stages = list(map(int, input().split()))
fails = []
result = []

for i in range(1, n+1):
    nc = 0
    c = 0
    for stage in stages:
        if stage >= i :
            c += 1
        if stage == i:
            nc += 1
    
    if c == 0:
        fail = 0
    else:
        fail = nc / c
        
    fails.append((i, fail))
    
fails.sort(key=lambda x : -x[1])

for fail in fails:
    result.append(fail[0])

print(result)

#책 풀이
def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        answer.append((i, fail))
        length -= count
    
    answer = sorted(answer, key = lambda t : t[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer