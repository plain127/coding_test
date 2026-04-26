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

class Edge
{
    public int To;
    public int Rev;
    public int Cap;
    public int Cost;

    public Edge(int to, int rev, int cap, int cost)
    {
        To = to;
        Rev = rev;
        Cap = cap;
        Cost = cost;
    }
}

class Program
{
    const int INF = 1_000_000_000;

    static List<Edge>[] graph;
    static int nodeCount;
    static int source;
    static int sink;

    static void AddEdge(int from, int to, int cap, int cost)
    {
        graph[from].Add(new Edge(to, graph[to].Count, cap, cost));
        graph[to].Add(new Edge(from, graph[from].Count - 1, 0, -cost));
    }

    static void MinCostMaxFlow(out int totalFlow, out int totalCost)
    {
        totalFlow = 0;
        totalCost = 0;

        int[] dist = new int[nodeCount];
        int[] prevNode = new int[nodeCount];
        int[] prevEdge = new int[nodeCount];
        bool[] inQueue = new bool[nodeCount];

        Queue<int> queue = new Queue<int>();

        while (true)
        {
            for (int i = 0; i < nodeCount; i++)
            {
                dist[i] = INF;
                prevNode[i] = -1;
                prevEdge[i] = -1;
                inQueue[i] = false;
            }

            dist[source] = 0;
            queue.Clear();
            queue.Enqueue(source);
            inQueue[source] = true;

            while (queue.Count > 0)
            {
                int cur = queue.Dequeue();
                inQueue[cur] = false;

                for (int i = 0; i < graph[cur].Count; i++)
                {
                    Edge edge = graph[cur][i];

                    if (edge.Cap <= 0)
                        continue;

                    int next = edge.To;
                    int nextCost = dist[cur] + edge.Cost;

                    if (dist[next] > nextCost)
                    {
                        dist[next] = nextCost;
                        prevNode[next] = cur;
                        prevEdge[next] = i;

                        if (!inQueue[next])
                        {
                            queue.Enqueue(next);
                            inQueue[next] = true;
                        }
                    }
                }
            }

            if (prevNode[sink] == -1)
                break;

            int flow = INF;

            for (int cur = sink; cur != source; cur = prevNode[cur])
            {
                int before = prevNode[cur];
                int edgeIndex = prevEdge[cur];
                Edge edge = graph[before][edgeIndex];

                if (edge.Cap < flow)
                    flow = edge.Cap;
            }

            for (int cur = sink; cur != source; cur = prevNode[cur])
            {
                int before = prevNode[cur];
                int edgeIndex = prevEdge[cur];
                Edge edge = graph[before][edgeIndex];

                edge.Cap -= flow;
                graph[cur][edge.Rev].Cap += flow;
                totalCost += flow * edge.Cost;
            }

            totalFlow += flow;
        }
    }

    static void Main()
    {
        var fs = new FastScanner();

        int n = fs.NextInt();
        int m = fs.NextInt();

        source = 0;
        int workerStart = 1;
        int jobStart = workerStart + n;
        sink = jobStart + m;
        nodeCount = sink + 1;

        graph = new List<Edge>[nodeCount];

        for (int i = 0; i < nodeCount; i++)
        {
            graph[i] = new List<Edge>();
        }

        for (int worker = 0; worker < n; worker++)
        {
            int workerNode = workerStart + worker;
            AddEdge(source, workerNode, 1, 0);
        }

        for (int worker = 0; worker < n; worker++)
        {
            int workerNode = workerStart + worker;
            int count = fs.NextInt();

            for (int i = 0; i < count; i++)
            {
                int job = fs.NextInt();
                int wage = fs.NextInt();

                int jobNode = jobStart + job - 1;
                AddEdge(workerNode, jobNode, 1, wage);
            }
        }

        for (int job = 0; job < m; job++)
        {
            int jobNode = jobStart + job;
            AddEdge(jobNode, sink, 1, 0);
        }

        MinCostMaxFlow(out int flow, out int cost);

        Console.WriteLine(flow);
        Console.WriteLine(cost);
    }
}