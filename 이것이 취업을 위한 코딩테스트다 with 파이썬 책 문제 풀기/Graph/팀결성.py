#내 풀이
n, m = map(int, input().split())
parent = [0] * (n + 1)

def find_parent(parent, a, b):
    if parent[a] == b or parent[b] == a:
        return print('YES')
    return print('NO')

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(0, n+1):
    parent[i] = i

for _ in range(m):
    calc = input().split(' ')

    if calc[0] == '0':
        union_parent(parent, int(calc[1]), int(calc[2]))
    elif calc[0] == '1':
        find_parent(parent, int(calc[1]), int(calc[2]))
