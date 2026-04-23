using System;
using System.Collections.Generic;
using System.IO;

class FastScanner
{
    private readonly Stream stream = Console.OpenStandardInput();
    private readonly byte[] buffer = new byte[1 << 16];
    private int ptr, len;

    private int Read()
    {
        if (ptr >= len)
        {
            len = stream.Read(buffer, 0, buffer.Length);
            ptr = 0;
            if (len <= 0) return -1;
        }
        return buffer[ptr++];
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

struct Group
{
    public int Size;
    public int Candy;

    public Group(int size, int candy)
    {
        Size = size;
        Candy = candy;
    }
}

class Program
{
    static int Find(int x, int[] parent)
    {
        while (parent[x] != x)
        {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    static void Union(int a, int b, int[] parent)
    {
        int ra = Find(a, parent);
        int rb = Find(b, parent);

        if (ra == rb) return;

        if (ra < rb) parent[rb] = ra;
        else parent[ra] = rb;
    }

    static void Main()
    {
        var fs = new FastScanner();

        int n = fs.NextInt();
        int m = fs.NextInt();
        int k = fs.NextInt();

        int[] candy = new int[n + 1];
        for (int i = 1; i <= n; i++)
            candy[i] = fs.NextInt();

        int[] parent = new int[n + 1];
        for (int i = 1; i <= n; i++)
            parent[i] = i;

        for (int i = 0; i < m; i++)
        {
            int a = fs.NextInt();
            int b = fs.NextInt();
            Union(a, b, parent);
        }

        int[] groupSize = new int[n + 1];
        int[] groupCandy = new int[n + 1];

        for (int i = 1; i <= n; i++)
        {
            int root = Find(i, parent);
            groupSize[root]++;
            groupCandy[root] += candy[i];
        }

        List<Group> groups = new List<Group>();
        for (int i = 1; i <= n; i++)
        {
            if (groupSize[i] > 0 && groupSize[i] < k)
                groups.Add(new Group(groupSize[i], groupCandy[i]));
        }

        int[] dp = new int[k];

        foreach (Group g in groups)
        {
            for (int j = k - 1; j >= g.Size; j--)
            {
                dp[j] = Math.Max(dp[j], dp[j - g.Size] + g.Candy);
            }
        }

        Console.WriteLine(dp[k - 1]);
    }
}