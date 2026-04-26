import sys

input = sys.stdin.readline

mask64 = (1 << 64) - 1
base = 911382323
max_len = 2000

def get_hash(word):
    h = 0

    for ch in word:
        h = (h * base + ord(ch)) & mask64

    return h


def get_reverse_hash(word):
    h = 0

    for ch in reversed(word):
        h = (h * base + ord(ch)) & mask64

    return h

c, n = map(int, input().split())
color_hashes = [set() for _ in range(max_len + 1)]
nick_hashes = [set() for _ in range(max_len + 1)]

max_color_len = 0
max_nick_len = 0

for _ in range(c):
    word = input().strip()
    length = len(word)

    color_hashes[length].add(get_hash(word))

    if max_color_len < length:
        max_color_len = length

for _ in range(n):
    word = input().strip()
    length = len(word)

    nick_hashes[length].add(get_reverse_hash(word))

    if max_nick_len < length:
        max_nick_len = length


def can_make(team):
    length = len(team)

    if length < 2:
        return False
    color_possible = [False] * (length + 1)

    h = 0
    left_limit = min(max_color_len, length - 1)

    for i in range(left_limit):
        h = (h * base + ord(team[i])) & mask64

        prefix_len = i + 1

        if h in color_hashes[prefix_len]:
            color_possible[prefix_len] = True

    h = 0

    right_limit = min(max_nick_len, length - 1)

    for suffix_len in range(1, right_limit + 1):
        split = length - suffix_len
        h = (h * base + ord(team[split])) & mask64

        if h in nick_hashes[suffix_len] and color_possible[split]:
            return True

    return False


q = int(input())
answer = []

for _ in range(q):
    team = input().strip()

    if can_make(team):
        answer.append('Yes')
    else:
        answer.append('No')

print('\n'.join(answer))