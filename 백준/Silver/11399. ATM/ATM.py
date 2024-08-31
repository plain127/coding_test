n = int(input())
time = list(map(int, input().split()))

time.sort()
timeline = 0

for i in range(n):
    timeline += time[i]*(n-i)
    
print(timeline)