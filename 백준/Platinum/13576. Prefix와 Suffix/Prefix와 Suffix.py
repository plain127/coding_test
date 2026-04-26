import sys

input = sys.stdin.readline

s = input().strip()
n = len(s)

pi = [0] * n

for i in range(1, n):
    j = pi[i - 1]

    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]

    if s[i] == s[j]:
        j += 1

    pi[i] = j

cnt = [0] * (n + 1)

for value in pi:
    cnt[value] += 1

for length in range(n, 0, -1):
    cnt[pi[length - 1]] += cnt[length]

for length in range(1, n + 1):
    cnt[length] += 1

borders = []

length = n

while length > 0:
    borders.append(length)
    length = pi[length - 1]

borders.reverse()

print(len(borders))

for length in borders:
    print(length, cnt[length])