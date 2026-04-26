import sys

input = sys.stdin.readline

answers = []

while True:
    line = input()
    if not line:
        break

    n = int(line)
    words = []

    for _ in range(n):
        word = input().strip()
        words.append(word)
    word_set = set(words)

    def get_lcp(a, b):
        limit = min(len(a), len(b))
        same = 0

        while same < limit and a[same] == b[same]:
            same += 1

        return same
    sorted_words = sorted(words)
    branch_prefixes = set()

    for i in range(n - 1):
        a = sorted_words[i]
        b = sorted_words[i + 1]

        same = get_lcp(a, b)

        if same < len(a) and same < len(b):
            branch_prefixes.add(a[:same])

    total_press = 0

    for word in words:
        press_count = 1

        for cut in range(1, len(word)):
            prefix = word[:cut]

            if prefix in word_set:
                press_count += 1
            elif prefix in branch_prefixes:
                press_count += 1

        total_press += press_count

    average = total_press / n
    answers.append(f'{average:.2f}')

print('\n'.join(answers))