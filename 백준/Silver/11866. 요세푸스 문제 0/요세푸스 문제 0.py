import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
circle = deque([i for i in range(1, n+1)])
results = []

while len(circle) > 0:   
    circle.rotate(-(k-1))
    results.append(str(circle.popleft()))
    
print('<'+', '.join(results)+'>')