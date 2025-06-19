import sys

input = sys.stdin.readline

n = input().strip()

sum = 0
k = 1
for i in range(12):
    if n[i] != "*":
        if i % 2 == 0:
            sum += int(n[i])
        else:
            sum += 3*int(n[i])
    else:
        if i % 2 == 0:
            k = 1
        else:
            k = 3

sum += int(n[-1])
m = 0
for i in range(10):
    if k == 3:
        t = 3*i
    elif k == 1:
        t = i

    if (sum+t) % 10 == 0:
            m = i
            break

print(m)