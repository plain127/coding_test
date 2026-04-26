import sys

input = sys.stdin.readline


def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def solve(left, right):
    length = right - left

    if length <= 3:
        best = INF

        for i in range(left, right):
            for j in range(i + 1, right):
                d = dist2(points[i], points[j])

                if d < best:
                    best = d

        small = points[left:right]
        small.sort(key=lambda p: p[1])

        return small, best

    mid = (left + right) // 2
    mid_x = points[mid][0]

    left_y, left_best = solve(left, mid)
    right_y, right_best = solve(mid, right)

    best = left_best if left_best < right_best else right_best

    merged = []
    i = 0
    j = 0

    while i < len(left_y) and j < len(right_y):
        if left_y[i][1] <= right_y[j][1]:
            merged.append(left_y[i])
            i += 1
        else:
            merged.append(right_y[j])
            j += 1

    if i < len(left_y):
        merged.extend(left_y[i:])

    if j < len(right_y):
        merged.extend(right_y[j:])

    strip = []

    for point in merged:
        dx = point[0] - mid_x

        if dx * dx < best:
            strip.append(point)

    strip_len = len(strip)

    for i in range(strip_len):
        a = strip[i]

        for j in range(i + 1, strip_len):
            b = strip[j]
            dy = b[1] - a[1]

            if dy * dy >= best:
                break

            d = dist2(a, b)

            if d < best:
                best = d

    return merged, best


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

if len(set(points)) < n:
    print(0)
    sys.exit()

points.sort()

INF = 10 ** 20

_, answer = solve(0, n)

print(answer)