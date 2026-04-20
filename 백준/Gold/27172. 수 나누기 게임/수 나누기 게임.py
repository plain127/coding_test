import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

max_card = max(cards)

exist = [False]*(max_card+1)
for x in cards:
    exist[x] = True

score = [0]*(max_card+1)

for x in cards:
    for multiple in range(2*x, max_card+1, x):
        if exist[multiple]:
            score[x] += 1
            score[multiple] -= 1

print(*[score[x] for x in cards])