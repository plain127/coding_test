from collections import deque
import sys

n = int(sys.stdin.readline().strip())
cards = [i for i in range(1, n+1)]
q = deque(cards)
        
while len(q) > 1:
    q.popleft()
    temp = q[0]
    q.popleft()
    q.append(temp)

print(q[0])