using System;
using System.IO;
using System.Collections.Generic;
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

struct Point
{
    public int X;
    public int Y;
    public long W;

    public Point(int x, int y, long w)
    {
        X = x;
        Y = y;
        W = w;
    }
}

class SegmentTree
{
    int size;
    long[] sum;
    long[] pref;
    long[] suff;
    long[] best;

    public SegmentTree(int n)
    {
        size = 1;
        while (size < n) size <<= 1;

        sum = new long[size * 2];
        pref = new long[size * 2];
        suff = new long[size * 2];
        best = new long[size * 2];
    }

    public void Clear()
    {
        Array.Clear(sum, 0, sum.Length);
        Array.Clear(pref, 0, pref.Length);
        Array.Clear(suff, 0, suff.Length);
        Array.Clear(best, 0, best.Length);
    }

    void Pull(int node)
    {
        int left = node * 2;
        int right = left + 1;

        sum[node] = sum[left] + sum[right];

        pref[node] = Math.Max(pref[left], sum[left] + pref[right]);
        suff[node] = Math.Max(suff[right], sum[right] + suff[left]);

        best[node] = Math.Max(Math.Max(best[left], best[right]), suff[left] + pref[right]);
    }

    public void Add(int pos, long value)
    {
        int node = size + pos;

        sum[node] += value;
        pref[node] += value;
        suff[node] += value;
        best[node] += value;

        node >>= 1;

        while (node > 0)
        {
            Pull(node);
            node >>= 1;
        }
    }

    public long Best()
    {
        return best[1];
    }
}

class Program
{
    static void Main()
    {
        var fs = new FastScanner();

        int n = fs.NextInt();

        Point[] points = new Point[n];
        int[] xs = new int[n];
        int[] ys = new int[n];

        for (int i = 0; i < n; i++)
        {
            int x = fs.NextInt();
            int y = fs.NextInt();
            int w = fs.NextInt();

            points[i] = new Point(x, y, w);
            xs[i] = x;
            ys[i] = y;
        }

        Array.Sort(xs);
        Array.Sort(ys);

        List<int> uniqueX = new List<int>();
        List<int> uniqueY = new List<int>();

        for (int i = 0; i < n; i++)
        {
            if (i == 0 || xs[i] != xs[i - 1])
                uniqueX.Add(xs[i]);

            if (i == 0 || ys[i] != ys[i - 1])
                uniqueY.Add(ys[i]);
        }

        Dictionary<int, int> xIndex = new Dictionary<int, int>();
        Dictionary<int, int> yIndex = new Dictionary<int, int>();

        for (int i = 0; i < uniqueX.Count; i++)
            xIndex[uniqueX[i]] = i;

        for (int i = 0; i < uniqueY.Count; i++)
            yIndex[uniqueY[i]] = i;

        List<(int x, long w)>[] byY = new List<(int x, long w)>[uniqueY.Count];

        for (int i = 0; i < uniqueY.Count; i++)
            byY[i] = new List<(int x, long w)>();

        for (int i = 0; i < n; i++)
        {
            int cx = xIndex[points[i].X];
            int cy = yIndex[points[i].Y];

            byY[cy].Add((cx, points[i].W));
        }

        SegmentTree seg = new SegmentTree(uniqueX.Count);

        long answer = long.MinValue;

        for (int bottom = 0; bottom < uniqueY.Count; bottom++)
        {
            seg.Clear();

            for (int top = bottom; top < uniqueY.Count; top++)
            {
                foreach (var item in byY[top])
                {
                    seg.Add(item.x, item.w);
                }

                long current = seg.Best();

                if (current > answer)
                    answer = current;
            }
        }

        Console.WriteLine(answer);
    }
}