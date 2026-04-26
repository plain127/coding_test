using System;
using System.IO;
using System.Text;

class FastScanner
{
    private readonly Stream stream = Console.OpenStandardInput();
    private readonly byte[] buffer = new byte[1 << 16];
    private int index = 0;
    private int size = 0;

    private int Read()
    {
        if (index >= size)
        {
            size = stream.Read(buffer, 0, buffer.Length);
            index = 0;
            if (size == 0) return -1;
        }

        return buffer[index++];
    }

    public int NextInt()
    {
        int c;

        do
        {
            c = Read();
        } while (c <= 32);

        int value = 0;

        while (c > 32)
        {
            value = value * 10 + (c - '0');
            c = Read();
        }

        return value;
    }
}

class Program
{
    const int MOD = 998244353;
    const int ROOT = 3;

    static long Pow(long a, long e)
    {
        long result = 1;

        while (e > 0)
        {
            if ((e & 1) == 1)
                result = result * a % MOD;

            a = a * a % MOD;
            e >>= 1;
        }

        return result;
    }

    static void Ntt(int[] a, bool invert)
    {
        int n = a.Length;

        for (int i = 1, j = 0; i < n; i++)
        {
            int bit = n >> 1;

            while ((j & bit) != 0)
            {
                j ^= bit;
                bit >>= 1;
            }

            j ^= bit;

            if (i < j)
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }

        for (int len = 2; len <= n; len <<= 1)
        {
            int wlen = (int)Pow(ROOT, (MOD - 1) / len);

            if (invert)
                wlen = (int)Pow(wlen, MOD - 2);

            int half = len >> 1;

            for (int i = 0; i < n; i += len)
            {
                long w = 1;

                for (int j = 0; j < half; j++)
                {
                    int u = a[i + j];
                    int v = (int)(a[i + j + half] * w % MOD);

                    int x = u + v;
                    if (x >= MOD) x -= MOD;

                    int y = u - v;
                    if (y < 0) y += MOD;

                    a[i + j] = x;
                    a[i + j + half] = y;

                    w = w * wlen % MOD;
                }
            }
        }

        if (invert)
        {
            long invN = Pow(n, MOD - 2);

            for (int i = 0; i < n; i++)
                a[i] = (int)(a[i] * invN % MOD);
        }
    }

    static void Main()
    {
        var fs = new FastScanner();

        int t = fs.NextInt();

        int[] queries = new int[t];
        int maxN = 0;

        for (int i = 0; i < t; i++)
        {
            queries[i] = fs.NextInt();

            if (queries[i] > maxN)
                maxN = queries[i];
        }

        bool[] isPrime = new bool[maxN + 1];

        if (maxN >= 2)
        {
            for (int i = 2; i <= maxN; i++)
                isPrime[i] = true;

            for (int i = 2; (long)i * i <= maxN; i++)
            {
                if (!isPrime[i])
                    continue;

                for (long j = (long)i * i; j <= maxN; j += i)
                    isPrime[(int)j] = false;
            }
        }

        int size = 1;

        while (size <= maxN * 2)
            size <<= 1;

        int[] oddPrime = new int[size];
        int[] evenSemiPrime = new int[size];

        // A[p] = p가 홀수 소수이면 1
        for (int p = 3; p <= maxN; p += 2)
        {
            if (isPrime[p])
                oddPrime[p] = 1;
        }

        // B[2*p] = 1, p가 소수이면
        // 2*2 = 4도 짝수 세미소수라 포함된다.
        for (int p = 2; 2 * p <= maxN; p++)
        {
            if (isPrime[p])
                evenSemiPrime[2 * p] = 1;
        }

        Ntt(oddPrime, false);
        Ntt(evenSemiPrime, false);

        for (int i = 0; i < size; i++)
            oddPrime[i] = (int)((long)oddPrime[i] * evenSemiPrime[i] % MOD);

        Ntt(oddPrime, true);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++)
        {
            int n = queries[i];
            sb.Append(oddPrime[n]).Append('\n');
        }

        Console.Write(sb.ToString());
    }
}