import sys
from array import array

data = sys.stdin.buffer.read()
idx = 0
data_len = len(data)


def next_int():
    global idx

    while idx < data_len and data[idx] <= 32:
        idx += 1

    num = 0

    while idx < data_len and data[idx] > 32:
        num = num * 10 + (data[idx] - 48)
        idx += 1

    return num


MAX_BIT = 18
MAX_VALUE = (1 << 19) - 1

m = next_int()

# 추가 쿼리가 최대 m개.
# 숫자 하나 추가할 때 root 포함 약 20개 노드 생성.
max_nodes = (m + 5) * (MAX_BIT + 2) + 5

left_child = array('i', [0]) * max_nodes
right_child = array('i', [0]) * max_nodes
count = array('i', [0]) * max_nodes
roots = array('i', [0]) * (m + 5)

node_count = 0


def update(prev_root, x):
    global node_count

    # 새 root 만들기
    node_count += 1
    new_root = node_count

    left_child[new_root] = left_child[prev_root]
    right_child[new_root] = right_child[prev_root]
    count[new_root] = count[prev_root] + 1

    prev_node = prev_root
    cur_node = new_root

    # x의 비트를 따라 내려가면서 그 경로만 새 노드로 복사
    for bit in range(MAX_BIT, -1, -1):
        x_bit = (x >> bit) & 1

        if x_bit == 0:
            prev_child = left_child[prev_node]

            node_count += 1
            new_child = node_count

            left_child[new_child] = left_child[prev_child]
            right_child[new_child] = right_child[prev_child]
            count[new_child] = count[prev_child] + 1

            left_child[cur_node] = new_child

        else:
            prev_child = right_child[prev_node]

            node_count += 1
            new_child = node_count

            left_child[new_child] = left_child[prev_child]
            right_child[new_child] = right_child[prev_child]
            count[new_child] = count[prev_child] + 1

            right_child[cur_node] = new_child

        prev_node = prev_child
        cur_node = new_child

    return new_root


def count_less_equal(left_root, right_root, x):
    if x < 0:
        return 0

    if x >= MAX_VALUE:
        return count[right_root] - count[left_root]

    result = 0

    # root[R] - root[L-1]로 실제 구간 개수를 본다
    for bit in range(MAX_BIT, -1, -1):
        x_bit = (x >> bit) & 1

        if x_bit == 1:
            # 현재 비트가 0인 값들은 전부 x 이하로 확정
            left_zero = left_child[left_root]
            right_zero = left_child[right_root]

            result += count[right_zero] - count[left_zero]

            left_root = right_child[left_root]
            right_root = right_child[right_root]

        else:
            left_root = left_child[left_root]
            right_root = left_child[right_root]

    # x와 완전히 같은 값들 추가
    result += count[right_root] - count[left_root]

    return result


def kth_number(left_root, right_root, k):
    answer = 0

    for bit in range(MAX_BIT, -1, -1):
        left_left = left_child[left_root]
        right_left = left_child[right_root]

        left_count = count[right_left] - count[left_left]

        if k <= left_count:
            left_root = left_left
            right_root = right_left

        else:
            k -= left_count
            answer |= 1 << bit

            left_root = right_child[left_root]
            right_root = right_child[right_root]

    return answer


def max_xor_y(left_root, right_root, x):
    y = 0

    for bit in range(MAX_BIT, -1, -1):
        x_bit = (x >> bit) & 1
        want = x_bit ^ 1

        if want == 0:
            next_left = left_child[left_root]
            next_right = left_child[right_root]
        else:
            next_left = right_child[left_root]
            next_right = right_child[right_root]

        available = count[next_right] - count[next_left]

        if available > 0:
            chosen = want
            left_root = next_left
            right_root = next_right

        else:
            chosen = x_bit

            if chosen == 0:
                left_root = left_child[left_root]
                right_root = left_child[right_root]
            else:
                left_root = right_child[left_root]
                right_root = right_child[right_root]

        if chosen == 1:
            y |= 1 << bit

    return y


size = 0
answers = []

for _ in range(m):
    command = next_int()

    if command == 1:
        x = next_int()

        size += 1
        roots[size] = update(roots[size - 1], x)

    elif command == 2:
        left = next_int()
        right = next_int()
        x = next_int()

        left_root = roots[left - 1]
        right_root = roots[right]

        answers.append(str(max_xor_y(left_root, right_root, x)))

    elif command == 3:
        k = next_int()

        size -= k

    elif command == 4:
        left = next_int()
        right = next_int()
        x = next_int()

        left_root = roots[left - 1]
        right_root = roots[right]

        answers.append(str(count_less_equal(left_root, right_root, x)))

    else:
        left = next_int()
        right = next_int()
        k = next_int()

        left_root = roots[left - 1]
        right_root = roots[right]

        answers.append(str(kth_number(left_root, right_root, k)))

sys.stdout.write('\n'.join(answers))