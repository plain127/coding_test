import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

white, blue = 0, 0

def cut(x, y, n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0,0,n)
print(white, blue, sep='\n')