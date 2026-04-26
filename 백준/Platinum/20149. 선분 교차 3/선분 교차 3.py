import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

def ccw(a,b,c):
    x1 = b[0] - a[0]
    y1 = b[1] - a[1]

    x2 = c[0] - a[0]
    y2 = c[1] - a[1]

    cross = x1*y2 - y1*x2

    if cross > 0:
        return 1
    
    if cross < 0:
        return -1
    
    return 0

def is_intersect(a,b,c,d):
    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)

    if ab == 0 and cd == 0:
        if b<a:
            a, b = b, a
        if d<c:
            c, d = d, c
        
        return a <= d and c <= b
    
    return ab<=0 and cd<=0

if not is_intersect(p1,p2,p3,p4):
    print(0)
    sys.exit()

print(1)

den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

if den == 0:
    a, b = sorted([p1,p2])
    c, d = sorted([p3,p4])

    start = max(a,c)
    end = min(b,d)

    if start == end:
        print(start[0], start[1])
    
    sys.exit()

a_value = x1*y2 - y1*x2
b_value = x3*y4 - y3*x4

px_num = a_value*(x3-x4) - (x1-x2)*b_value
py_num = a_value*(y3-y4) - (y1-y2)*b_value

px = px_num / den
py = py_num / den

if abs(px) < 1e-12:
    px = 0.0

if abs(py) < 1e-12:
    py = 0.0

print(f'{px:.10f} {py:.10f}')