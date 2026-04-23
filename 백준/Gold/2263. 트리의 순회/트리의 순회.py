import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0]*(n+1)
for i,v in enumerate(inorder):
    pos[v] = i

ans = []

def preorder(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return

    root = postorder[post_r]
    ans.append(str(root))

    mid = pos[root]
    left_size = mid - in_l

    preorder(in_l, mid-1, post_l, post_l+left_size-1)
    preorder(mid+1, in_r, post_l+left_size, post_r-1)

preorder(0, n-1, 0, n-1)
print(' '.join(ans))