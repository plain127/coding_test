import sys
import math

input = sys.stdin.readline

def cross(a, b, c):
    x1 = b[0] - a[0]
    y1 = b[1] - a[1]

    x2 = c[0] - a[0]
    y2 = c[1] - a[1]

    return x1 * y2 - y1 * x2

def convex_hull(points):
    sorted_points = sorted(points)

    lower = []
    for point in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    hull = lower[:-1] + upper[:-1]
    return hull


def minimum_width(hull):
    count = len(hull)

    if count <= 2:
        return 0.0

    best = float('inf')

    for i in range(count):
        a = hull[i]
        b = hull[(i + 1) % count]

        dx = b[0] - a[0]
        dy = b[1] - a[1]

        edge_length = math.hypot(dx, dy)

        max_distance = 0.0

        for point in hull:
            area_twice = abs(cross(a, b, point))
            distance = area_twice / edge_length

            if max_distance < distance:
                max_distance = distance

        if max_distance < best:
            best = max_distance

    return best


def ceil_to_cent(value):
    scaled = value * 100
    rounded_up = math.ceil(scaled - 1e-9)
    return rounded_up / 100

answers = []
case_number = 1

while True:
    n = int(input())
    if n == 0:
        break

    points = []

    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    hull = convex_hull(points)
    width = minimum_width(hull)
    width = ceil_to_cent(width)

    answers.append(f'Case {case_number}: {width:.2f}')

    case_number += 1

print('\n'.join(answers))