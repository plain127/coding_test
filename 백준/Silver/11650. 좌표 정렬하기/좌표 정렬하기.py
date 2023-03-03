N= int(input())
points = []
for i in range(N):
    points.append(tuple(map(int,input().split())))

sorted_points = sorted(points, key=lambda x : (x[0], x[1]))

for point in sorted_points:
    print(point[0], point[1])