import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

def avg(arr):
    s = sum(arr)
    a = s / len(arr)
    return round(a)

def mid(arr):
    arr.sort()
    m = len(arr) // 2
    return arr[m]

def mode(arr):
    dp = [0]*4001
    mdp = [0]*4001
    for i in arr:
        if i >= 0:
            dp[i] += 1
        else:
            mdp[abs(i)] += 1

    m0 = max(dp)
    m1 = max(mdp)
    if m0 > m1:
        idx = [i for i, v in enumerate(dp) if v == m0]
        if len(idx) > 1:
            result = idx[1]
        else:
            result = idx[0]
    elif m1 > m0 :
        idx = [i for i, v in enumerate(mdp) if v == m1]
        if len(idx) > 1:
            result = idx[-2]*(-1)
        else:
            result = idx[-1]*(-1)
    else:
        idx0 = [i for i, v in enumerate(dp) if v == m0]
        idx1 = [i*(-1) for i, v in enumerate(mdp) if v == m1]
        if len(idx1) > 1:
            result = idx1[-2]
        else:
            result = idx0[0]
    return result

def range(arr):
    high = max(arr)
    row = min(arr)
    return high - row

print(avg(nums))
print(mid(nums))
print(mode(nums))    
print(range(nums))