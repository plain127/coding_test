# 내가 푼 풀이
n, m = map(int, input().split())
parent = [0] * (n + 1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def checking(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return 'YES'
    return 'NO'        
        
for i in range(1, n + 1):
    parent[i] = i
    
for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    elif x == 1:
        print(checking(parent, a, b))
        
# 책 풀이
def find(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(0, n+1):
    parent[i] = i
    
for i in range(m):
    oper, a, b = map(int, input().split())
    
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')