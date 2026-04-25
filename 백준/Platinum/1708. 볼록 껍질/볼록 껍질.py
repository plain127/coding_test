import sys

input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x,y))
points.sort()

def ccw(a,b,c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    return (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)

lower = []
for point in points:
    while len(lower) >= 2:
        a = lower[-2]
        b = lower[-1]
        c = point

        if ccw(a,b,c) <= 0:
            lower.pop()
        else:
            break
    lower.append(point)

upper = []
for point in reversed(points):
    while len(upper) >= 2:
        a = upper[-2]
        b = upper[-1]
        c = point

        if ccw(a,b,c) <= 0:
            upper.pop()
        else:
            break
    upper.append(point)

hull = lower[:-1] + upper[:-1]
print(len(hull))