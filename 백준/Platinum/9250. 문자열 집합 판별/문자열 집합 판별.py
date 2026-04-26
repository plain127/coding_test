import sys
from collections import deque

data = sys.stdin.buffer.read().split()
idx = 0

n = int(data[idx])
idx += 1

children = [{}]
fail = [0]
output = [False]


def new_node():
    children.append({})
    fail.append(0)
    output.append(False)
    return len(children) - 1


def insert(word):
    node = 0

    for ch in word:
        if ch not in children[node]:
            children[node][ch] = new_node()

        node = children[node][ch]

    output[node] = True


for _ in range(n):
    insert(data[idx])
    idx += 1


def build_fail():
    q = deque()

    for nxt in children[0].values():
        fail[nxt] = 0
        q.append(nxt)

    while q:
        cur = q.popleft()

        for ch, nxt in children[cur].items():
            f = fail[cur]

            while f != 0 and ch not in children[f]:
                f = fail[f]

            if ch in children[f]:
                fail[nxt] = children[f][ch]
            else:
                fail[nxt] = 0

            if output[fail[nxt]]:
                output[nxt] = True

            q.append(nxt)


def contains_pattern(text):
    node = 0

    for ch in text:
        while node != 0 and ch not in children[node]:
            node = fail[node]

        if ch in children[node]:
            node = children[node][ch]
        else:
            node = 0

        if output[node]:
            return True

    return False


build_fail()

q = int(data[idx])
idx += 1

answer = []

for _ in range(q):
    text = data[idx]
    idx += 1

    if contains_pattern(text):
        answer.append('YES')
    else:
        answer.append('NO')

sys.stdout.write('\n'.join(answer))