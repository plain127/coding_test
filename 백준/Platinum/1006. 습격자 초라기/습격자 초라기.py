import sys

input = sys.stdin.readline

INF = 10 ** 9

case_count = int(input())
answers = []


def solve_case(n, w, upper, lower):
    if n == 1:
        if upper[0] + lower[0] <= w:
            return 1
        return 2

    def calc(wrap_top, wrap_bottom):
        fixed = [0] * n
        base = 0

        if wrap_top:
            if upper[0] + upper[n - 1] > w:
                return INF

            fixed[0] |= 1
            fixed[n - 1] |= 1
            base += 1

        if wrap_bottom:
            if lower[0] + lower[n - 1] > w:
                return INF

            fixed[0] |= 2
            fixed[n - 1] |= 2
            base += 1

        dp = {0: base}

        for col in range(n):
            next_dp = {}

            for mask, cost in dp.items():
                if mask & fixed[col]:
                    continue

                filled = mask | fixed[col]

                def fill(filled, next_mask, add):
                    if filled == 3:
                        new_cost = cost + add
                        if new_cost < next_dp.get(next_mask, INF):
                            next_dp[next_mask] = new_cost
                        return

                    if filled & 1 == 0:
                        bit = 1
                        row = 0
                    else:
                        bit = 2
                        row = 1

                    fill(filled | bit, next_mask, add + 1)
                    if filled == 0 and upper[col] + lower[col] <= w:
                        fill(3, next_mask, add + 1)

                    if col + 1 < n:
                        if next_mask & bit == 0 and fixed[col + 1] & bit == 0:
                            if row == 0 and upper[col] + upper[col + 1] <= w:
                                fill(filled | bit, next_mask | bit, add + 1)

                            if row == 1 and lower[col] + lower[col + 1] <= w:
                                fill(filled | bit, next_mask | bit, add + 1)

                fill(filled, 0, 0)

            dp = next_dp

        return dp.get(0, INF)

    answer = INF

    for wrap_top in (False, True):
        for wrap_bottom in (False, True):
            answer = min(answer, calc(wrap_top, wrap_bottom))

    return answer


for _ in range(case_count):
    n, w = map(int, input().split())

    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    answers.append(str(solve_case(n, w, upper, lower)))

print('\n'.join(answers))