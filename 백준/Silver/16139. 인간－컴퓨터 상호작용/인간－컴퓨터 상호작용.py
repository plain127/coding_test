import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

pref = [[0]*26 for _ in range(n+1)]
for i, ch in enumerate(s, 1):
    row = pref[i-1].copy()            
    row[ord(ch) - 97] += 1
    pref[i] = row

q = int(input())
out = []
for _ in range(q):
    a, l, r = input().split()
    c = ord(a) - 97
    l = int(l); r = int(r)
    out.append(str(pref[r+1][c] - pref[l][c]))
sys.stdout.write("\n".join(out))
