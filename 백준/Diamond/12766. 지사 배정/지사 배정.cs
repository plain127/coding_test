using System;
using System.IO;
using System.Collections.Generic;

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

struct Edge
{
    public int To;
    public long Cost;

    public Edge(int to, long cost)
    {
        To = to;
        Cost = cost;
    }
}

class MinHeap
{
    private readonly List<(long dist, int node)> heap = new List<(long dist, int node)>();

    public int Count => heap.Count;

    public void Push(long dist, int node)
    {
        heap.Add((dist, node));

        int cur = heap.Count - 1;

        while (cur > 0)
        {
            int parent = (cur - 1) / 2;

            if (heap[parent].dist <= heap[cur].dist)
                break;

            var temp = heap[parent];
            heap[parent] = heap[cur];
            heap[cur] = temp;

            cur = parent;
        }
    }

    public (long dist, int node) Pop()
    {
        var result = heap[0];

        heap[0] = heap[heap.Count - 1];
        heap.RemoveAt(heap.Count - 1);

        int cur = 0;

        while (true)
        {
            int left = cur * 2 + 1;
            int right = cur * 2 + 2;
            int smallest = cur;

            if (left < heap.Count && heap[left].dist < heap[smallest].dist)
                smallest = left;

            if (right < heap.Count && heap[right].dist < heap[smallest].dist)
                smallest = right;

            if (smallest == cur)
                break;

            var temp = heap[cur];
            heap[cur] = heap[smallest];
            heap[smallest] = temp;

            cur = smallest;
        }

        return result;
    }
}

class Program
{
    const long INF = long.MaxValue / 4;

    static int n, b, s, r;
    static List<Edge>[] graph;
    static List<Edge>[] reverseGraph;
    static long[] prefix;
    static long[] prevDp;
    static long[] curDp;

    static long[] Dijkstra(List<Edge>[] g, int start)
    {
        long[] dist = new long[n + 1];

        for (int i = 1; i <= n; i++)
            dist[i] = INF;

        dist[start] = 0;

        MinHeap heap = new MinHeap();
        heap.Push(0, start);

        while (heap.Count > 0)
        {
            var item = heap.Pop();
            long curDist = item.dist;
            int cur = item.node;

            if (curDist != dist[cur])
                continue;

            foreach (var edge in g[cur])
            {
                long nextDist = curDist + edge.Cost;

                if (nextDist < dist[edge.To])
                {
                    dist[edge.To] = nextDist;
                    heap.Push(nextDist, edge.To);
                }
            }
        }

        return dist;
    }

    static long Cost(int k, int i)
    {
        return (long)(i - k - 1) * (prefix[i] - prefix[k]);
    }

    static void Compute(int left, int right, int optLeft, int optRight)
    {
        if (left > right)
            return;

        int mid = (left + right) / 2;

        long bestValue = INF;
        int bestK = optLeft;

        int end = Math.Min(optRight, mid - 1);

        for (int k = optLeft; k <= end; k++)
        {
            long candidate = prevDp[k] + Cost(k, mid);

            if (candidate < bestValue)
            {
                bestValue = candidate;
                bestK = k;
            }
        }

        curDp[mid] = bestValue;

        Compute(left, mid - 1, optLeft, bestK);
        Compute(mid + 1, right, bestK, optRight);
    }

    static void Main()
    {
        var fs = new FastScanner();

        n = fs.NextInt();
        b = fs.NextInt();
        s = fs.NextInt();
        r = fs.NextInt();

        graph = new List<Edge>[n + 1];
        reverseGraph = new List<Edge>[n + 1];

        for (int i = 1; i <= n; i++)
        {
            graph[i] = new List<Edge>();
            reverseGraph[i] = new List<Edge>();
        }

        for (int i = 0; i < r; i++)
        {
            int u = fs.NextInt();
            int v = fs.NextInt();
            int l = fs.NextInt();

            graph[u].Add(new Edge(v, l));
            reverseGraph[v].Add(new Edge(u, l));
        }

        int hq = b + 1;

        long[] fromHQ = Dijkstra(graph, hq);
        long[] toHQ = Dijkstra(reverseGraph, hq);

        long[] vals = new long[b + 1];

        for (int i = 1; i <= b; i++)
        {
            vals[i] = fromHQ[i] + toHQ[i];
        }

        Array.Sort(vals, 1, b);

        prefix = new long[b + 1];

        for (int i = 1; i <= b; i++)
        {
            prefix[i] = prefix[i - 1] + vals[i];
        }

        prevDp = new long[b + 1];
        curDp = new long[b + 1];

        for (int i = 1; i <= b; i++)
        {
            prevDp[i] = Cost(0, i);
        }

        for (int group = 2; group <= s; group++)
        {
            for (int i = 0; i <= b; i++)
                curDp[i] = INF;

            Compute(group, b, group - 1, b - 1);

            var temp = prevDp;
            prevDp = curDp;
            curDp = temp;
        }

        Console.WriteLine(prevDp[b]);
    }
}