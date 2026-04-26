import sys

input = sys.stdin.buffer.readline


def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def convex_hull(points):
    points.sort()

    if len(points) <= 2:
        return points

    lower = []

    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()

        lower.append(p)

    upper = []

    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()

        upper.append(p)

    return lower[:-1] + upper[:-1]


def rotating_calipers(hull):
    size = len(hull)

    if size == 2:
        return hull[0], hull[1]

    best_distance = -1
    answer_a = hull[0]
    answer_b = hull[1]

    j = 1

    for i in range(size):
        next_i = (i + 1) % size

        while True:
            next_j = (j + 1) % size

            current_area = abs(ccw(hull[i], hull[next_i], hull[j]))
            next_area = abs(ccw(hull[i], hull[next_i], hull[next_j]))

            if next_area > current_area:
                j = next_j
            else:
                break

        d = dist2(hull[i], hull[j])

        if d > best_distance:
            best_distance = d
            answer_a = hull[i]
            answer_b = hull[j]

        d = dist2(hull[next_i], hull[j])

        if d > best_distance:
            best_distance = d
            answer_a = hull[next_i]
            answer_b = hull[j]

    return answer_a, answer_b


t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    hull = convex_hull(points)
    a, b = rotating_calipers(hull)

    answers.append(f'{a[0]} {a[1]} {b[0]} {b[1]}')

sys.stdout.write('\n'.join(answers))