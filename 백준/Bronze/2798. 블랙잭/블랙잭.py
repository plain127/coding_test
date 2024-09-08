import sys

input = sys.stdin.readline

N,M=map(int,input().split())
card_num = list(map(int,input().split()))
max_sum = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res = card_num[i] + card_num[j] + card_num[k]
            if res <= M:
                max_sum = max(max_sum,res)

print(max_sum)