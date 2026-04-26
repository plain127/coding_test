import sys

input = sys.stdin.readline

MOD = 998244353
ROOT = 3

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


def bit_reverse(a):
    n = len(a)
    j = 0

    for i in range(1, n):
        bit = n >> 1

        while j & bit:
            j ^= bit
            bit >>= 1

        j ^= bit

        if i < j:
            a[i], a[j] = a[j], a[i]


def ntt(a, invert):
    n = len(a)
    bit_reverse(a)

    length = 2
    while length <= n:
        half = length >> 1
        wlen = pow(ROOT, (MOD - 1) // length, MOD)

        if invert:
            wlen = pow(wlen, MOD - 2, MOD)

        for start in range(0, n, length):
            w = 1

            for i in range(start, start + half):
                u = a[i]
                v = a[i + half] * w % MOD

                s = u + v
                if s >= MOD:
                    s -= MOD

                d = u - v
                if d < 0:
                    d += MOD

                a[i] = s
                a[i + half] = d
                w = w * wlen % MOD

        length <<= 1

    if invert:
        inv_n = pow(n, MOD - 2, MOD)

        for i in range(n):
            a[i] = a[i] * inv_n % MOD


def convolution(a, b):
    need = len(a) + len(b) - 1
    size = 1

    while size < need:
        size <<= 1

    fa = a[:] + [0] * (size - len(a))
    fb = b[:] + [0] * (size - len(b))

    ntt(fa, False)
    ntt(fb, False)

    for i in range(size):
        fa[i] = fa[i] * fb[i] % MOD

    ntt(fa, True)

    return fa[:need]


a = x + x
b = y[::-1]

conv = convolution(a, b)

print(max(conv[n - 1:2 * n - 1]))