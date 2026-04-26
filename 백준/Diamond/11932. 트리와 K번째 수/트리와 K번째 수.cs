using System;
using System.IO;
using System.Text;
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
    static int N, M, LOG;

    static int[] weight;
    static int[] compressedWeight;
    static int[] sortedValues;

    static List<int>[] graph;

    static int[,] parent;
    static int[] depth;

    static int[] root;
    static int[] leftChild;
    static int[] rightChild;
    static int[] count;
    static int nodeCount = 0;

    static int Update(int prevNode, int start, int end, int position)
    {
        int curNode = ++nodeCount;

        leftChild[curNode] = leftChild[prevNode];
        rightChild[curNode] = rightChild[prevNode];
        count[curNode] = count[prevNode] + 1;

        if (start == end)
            return curNode;

        int mid = (start + end) >> 1;

        if (position <= mid)
            leftChild[curNode] = Update(leftChild[prevNode], start, mid, position);
        else
            rightChild[curNode] = Update(rightChild[prevNode], mid + 1, end, position);

        return curNode;
    }

    static int Kth(int ru, int rv, int rlca, int rplca, int start, int end, int k)
    {
        if (start == end)
            return start;

        int mid = (start + end) >> 1;

        int leftCount =
            count[leftChild[ru]]
            + count[leftChild[rv]]
            - count[leftChild[rlca]]
            - count[leftChild[rplca]];

        if (k <= leftCount)
        {
            return Kth(
                leftChild[ru],
                leftChild[rv],
                leftChild[rlca],
                leftChild[rplca],
                start,
                mid,
                k
            );
        }

        return Kth(
            rightChild[ru],
            rightChild[rv],
            rightChild[rlca],
            rightChild[rplca],
            mid + 1,
            end,
            k - leftCount
        );
    }

    static int Lca(int a, int b)
    {
        if (depth[a] < depth[b])
        {
            int temp = a;
            a = b;
            b = temp;
        }

        int diff = depth[a] - depth[b];

        for (int i = 0; i < LOG; i++)
        {
            if (((diff >> i) & 1) == 1)
                a = parent[i, a];
        }

        if (a == b)
            return a;

        for (int i = LOG - 1; i >= 0; i--)
        {
            if (parent[i, a] != parent[i, b])
            {
                a = parent[i, a];
                b = parent[i, b];
            }
        }

        return parent[0, a];
    }

    static void BuildTree()
    {
        int[] queue = new int[N + 5];
        int front = 0;
        int back = 0;

        queue[back++] = 1;
        parent[0, 1] = 0;
        depth[1] = 0;

        bool[] visited = new bool[N + 1];
        visited[1] = true;

        while (front < back)
        {
            int node = queue[front++];

            root[node] = Update(root[parent[0, node]], 1, N, compressedWeight[node]);

            foreach (int next in graph[node])
            {
                if (visited[next])
                    continue;

                visited[next] = true;
                parent[0, next] = node;
                depth[next] = depth[node] + 1;
                queue[back++] = next;
            }
        }

        for (int level = 1; level < LOG; level++)
        {
            for (int node = 1; node <= N; node++)
            {
                parent[level, node] = parent[level - 1, parent[level - 1, node]];
            }
        }
    }

    static void Main()
    {
        var fs = new FastScanner();

        N = fs.NextInt();
        M = fs.NextInt();

        LOG = 1;
        while ((1 << LOG) <= N)
            LOG++;

        weight = new int[N + 1];
        compressedWeight = new int[N + 1];
        sortedValues = new int[N];

        for (int i = 1; i <= N; i++)
        {
            weight[i] = fs.NextInt();
            sortedValues[i - 1] = weight[i];
        }

        Array.Sort(sortedValues);

        for (int i = 1; i <= N; i++)
        {
            compressedWeight[i] = Array.BinarySearch(sortedValues, weight[i]) + 1;
        }

        graph = new List<int>[N + 1];

        for (int i = 1; i <= N; i++)
            graph[i] = new List<int>();

        for (int i = 0; i < N - 1; i++)
        {
            int a = fs.NextInt();
            int b = fs.NextInt();

            graph[a].Add(b);
            graph[b].Add(a);
        }

        parent = new int[LOG, N + 1];
        depth = new int[N + 1];
        root = new int[N + 1];

        int maxNodes = (N + 5) * (LOG + 2);

        leftChild = new int[maxNodes];
        rightChild = new int[maxNodes];
        count = new int[maxNodes];

        BuildTree();

        StringBuilder sb = new StringBuilder();

        for (int q = 0; q < M; q++)
        {
            int u = fs.NextInt();
            int v = fs.NextInt();
            int k = fs.NextInt();

            int lca = Lca(u, v);
            int parentOfLca = parent[0, lca];

            int compressedAnswer = Kth(
                root[u],
                root[v],
                root[lca],
                root[parentOfLca],
                1,
                N,
                k
            );

            int realAnswer = sortedValues[compressedAnswer - 1];

            sb.Append(realAnswer).Append('\n');
        }

        Console.Write(sb.ToString());
    }
}