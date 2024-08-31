n = int(input())
meeting = []
count = 1

for i in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x : (x[1], x[0]))

end = meeting[0][1]

for i in range(1,n):
    if meeting[i][0] >= end:
        end = meeting[i][1]
        count += 1
        
print(count)