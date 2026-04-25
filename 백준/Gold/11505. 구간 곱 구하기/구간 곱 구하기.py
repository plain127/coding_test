import sys

input = sys.stdin.readline
MOD = 1000000007

n, m, k = map(int, input().split())

size = 1
while size < n:
    size*=2

tree = [1]*(size*2)

for i in range(n):
    tree[size+i] = int(input())

for i in range(size-1, 0, -1):
    tree[i] = (tree[i*2]*tree[i*2+1])%MOD

def update(index, value):
    pos = size + index -1
    tree[pos] = value

    pos //= 2
    while pos >= 1:
        tree[pos] = (tree[pos*2]*tree[pos*2+1])%MOD
        pos //= 2

def query(left, right):
    left = size + left - 1
    right= size + right - 1

    result = 1

    while left <= right:
        if left%2 == 1:
            result = (result*tree[left])%MOD
            left += 1

        if right%2 == 0:
            result = (result*tree[right])%MOD
            right -= 1
        
        left //= 2
        right //= 2
    
    return result

ans = []

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b,c)
    else:
        ans.append(str(query(b,c)))

print('\n'.join(ans))