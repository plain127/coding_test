import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(float, input().split()))
scores.sort(reverse=True)
new_scores = []

for i in range(n):
    new_score = (scores[i]/scores[0])*100
    new_scores.append(new_score)

avg = sum(new_scores)/n

print(avg)        
