import sys

s = sys.stdin.readline().strip()
n = len(s)

d = [0] * n
ans = 0

l, r = 0, -1

for i in range(n):
    if i <= r:
        k = d[l + r - i]
        limit = r - i + 1
        if k > limit:
            k = limit
    else:
        k = 1

    a = i - k
    b = i + k

    while a >= 0 and b < n and s[a] == s[b]:
        k += 1
        a -= 1
        b += 1

    d[i] = k
    ans += k

    b -= 1
    if b > r:
        l = i - k + 1
        r = b

l, r = 0, -1

for i in range(n):
    if i <= r:
        k = d[l + r - i + 1]
        limit = r - i + 1
        if k > limit:
            k = limit
    else:
        k = 0

    a = i - k - 1
    b = i + k

    while a >= 0 and b < n and s[a] == s[b]:
        k += 1
        a -= 1
        b += 1

    d[i] = k
    ans += k

    b -= 1
    if b > r:
        l = i - k
        r = b

print(ans)