using System;
using System.IO;

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

            if (size == 0)
                return -1;
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

        int sign = 1;

        if (c == '-')
        {
            sign = -1;
            c = Read();
        }

        int value = 0;

        while (c > 32)
        {
            value = value * 10 + (c - '0');
            c = Read();
        }

        return value * sign;
    }
}

class Program
{
    static int n;
    static long[] weight;
    static int[] depth;
    static int[] order;
    static int pos;

    static void Dfs(int node)
    {
        if (node > n)
            return;

        Dfs(node * 2);

        order[pos] = node;
        pos++;

        Dfs(node * 2 + 1);
    }

    static void Main()
    {
        var fs = new FastScanner();

        n = fs.NextInt();

        weight = new long[n + 1];

        for (int i = 1; i <= n; i++)
        {
            weight[i] = fs.NextInt();
        }

        int height = 0;
        int temp = n;

        while (temp > 0)
        {
            height++;
            temp >>= 1;
        }

        depth = new int[n + 1];

        for (int node = 2; node <= n; node++)
        {
            depth[node] = depth[node / 2] + 1;
        }

        order = new int[n];
        pos = 0;

        Dfs(1);

        long answer = long.MinValue;

        for (int top = 0; top < height; top++)
        {
            for (int bottom = top; bottom < height; bottom++)
            {
                long current = 0;
                bool started = false;

                for (int i = 0; i < n; i++)
                {
                    int node = order[i];
                    int d = depth[node];

                    if (d < top || d > bottom)
                        continue;

                    long value = weight[node];

                    if (!started)
                    {
                        current = value;
                        started = true;
                    }
                    else
                    {
                        if (current < 0)
                            current = value;
                        else
                            current += value;
                    }

                    if (current > answer)
                        answer = current;
                }
            }
        }

        Console.WriteLine(answer);
    }
}