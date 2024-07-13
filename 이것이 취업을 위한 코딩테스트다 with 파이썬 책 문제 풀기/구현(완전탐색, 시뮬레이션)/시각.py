#내가 푼 풀이
n = int(input())

time = n*3600
hour = 0
min = 0
sec = 0

count = 0

while (hour*3600) <= time:
    sec += 1
    if sec == 60 :
        min += 1
        sec = 0
    if min == 60 :
        hour += 1
        min = 0
    if '3' in str(hour) + str(min) + str(sec):
        count += 1

print(count)

# 책 풀이

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
