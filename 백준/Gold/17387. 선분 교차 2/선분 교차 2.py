import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)

def ccw(p1,p2,p3):
    val = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

ab_c = ccw(a,b,c)
ab_d = ccw(a,b,d)
cd_a = ccw(c,d,a)
cd_b = ccw(c,d,b)

if ab_c == 0 and ab_d == 0 and cd_a == 0 and cd_b == 0:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    
    if c <= b and a <= d:
        print(1)
    else:
        print(0)

else:
    if ab_c*ab_d <=0 and cd_a*cd_b <= 0:
        print(1)
    else:
        print(0)
