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

class SegmentTree
{
    const ulong MASK = 0xFFFFFFFFUL;

    int n;
    ulong[] tree;
    ulong[] lazyMul;
    ulong[] lazyAdd;

    public SegmentTree(int n)
    {
        this.n = n;

        int size = n * 4 + 5;

        tree = new ulong[size];
        lazyMul = new ulong[size];
        lazyAdd = new ulong[size];

        for (int i = 0; i < size; i++)
            lazyMul[i] = 1;
    }

    void Apply(int node, int left, int right, ulong mul, ulong add)
    {
        ulong len = (ulong)(right - left + 1);

        unchecked
        {
            tree[node] = (tree[node] * mul + len * add) & MASK;
            lazyMul[node] = (lazyMul[node] * mul) & MASK;
            lazyAdd[node] = (lazyAdd[node] * mul + add) & MASK;
        }
    }

    void Push(int node, int left, int right)
    {
        if (lazyMul[node] == 1 && lazyAdd[node] == 0)
            return;

        int mid = (left + right) >> 1;

        Apply(node * 2, left, mid, lazyMul[node], lazyAdd[node]);
        Apply(node * 2 + 1, mid + 1, right, lazyMul[node], lazyAdd[node]);

        lazyMul[node] = 1;
        lazyAdd[node] = 0;
    }

    public void Update(int ql, int qr, ulong mul, ulong add)
    {
        Update(1, 1, n, ql, qr, mul, add);
    }

    void Update(int node, int left, int right, int ql, int qr, ulong mul, ulong add)
    {
        if (qr < left || right < ql)
            return;

        if (ql <= left && right <= qr)
        {
            Apply(node, left, right, mul, add);
            return;
        }

        Push(node, left, right);

        int mid = (left + right) >> 1;

        Update(node * 2, left, mid, ql, qr, mul, add);
        Update(node * 2 + 1, mid + 1, right, ql, qr, mul, add);

        tree[node] = (tree[node * 2] + tree[node * 2 + 1]) & MASK;
    }

    public ulong Query(int ql, int qr)
    {
        return Query(1, 1, n, ql, qr);
    }

    ulong Query(int node, int left, int right, int ql, int qr)
    {
        if (qr < left || right < ql)
            return 0;

        if (ql <= left && right <= qr)
            return tree[node];

        Push(node, left, right);

        int mid = (left + right) >> 1;

        ulong result = Query(node * 2, left, mid, ql, qr)
                     + Query(node * 2 + 1, mid + 1, right, ql, qr);

        return result & MASK;
    }
}

class Program
{
    const ulong MASK = 0xFFFFFFFFUL;

    static int N, Q;

    static int[] head;
    static int[] to;
    static int[] next;
    static int edgeCount;

    static int[] parent;
    static int[] depth;
    static int[] subtreeSize;
    static int[] heavy;
    static int[] top;
    static int[] pos;

    static SegmentTree seg;

    static void AddEdge(int a, int b)
    {
        to[edgeCount] = b;
        next[edgeCount] = head[a];
        head[a] = edgeCount++;

        to[edgeCount] = a;
        next[edgeCount] = head[b];
        head[b] = edgeCount++;
    }

    static void BuildHld()
    {
        int[] stack = new int[N];
        int[] order = new int[N];

        int sp = 0;
        int orderCount = 0;

        stack[sp++] = 1;
        parent[1] = 0;
        depth[1] = 0;

        while (sp > 0)
        {
            int node = stack[--sp];
            order[orderCount++] = node;

            for (int e = head[node]; e != -1; e = next[e])
            {
                int child = to[e];

                if (child == parent[node])
                    continue;

                parent[child] = node;
                depth[child] = depth[node] + 1;
                stack[sp++] = child;
            }
        }

        for (int i = orderCount - 1; i >= 0; i--)
        {
            int node = order[i];

            subtreeSize[node] = 1;
            int maxSize = 0;

            for (int e = head[node]; e != -1; e = next[e])
            {
                int child = to[e];

                if (child == parent[node])
                    continue;

                subtreeSize[node] += subtreeSize[child];

                if (subtreeSize[child] > maxSize)
                {
                    maxSize = subtreeSize[child];
                    heavy[node] = child;
                }
            }
        }

        int timer = 0;

        int[] stackNode = new int[N + 5];
        int[] stackTop = new int[N + 5];

        sp = 0;
        stackNode[sp] = 1;
        stackTop[sp] = 1;
        sp++;

        while (sp > 0)
        {
            sp--;

            int node = stackNode[sp];
            int chainTop = stackTop[sp];

            int cur = node;

            while (cur != 0)
            {
                pos[cur] = ++timer;
                top[cur] = chainTop;

                for (int e = head[cur]; e != -1; e = next[e])
                {
                    int child = to[e];

                    if (child == parent[cur] || child == heavy[cur])
                        continue;

                    stackNode[sp] = child;
                    stackTop[sp] = child;
                    sp++;
                }

                cur = heavy[cur];
            }
        }
    }

    static void UpdateSubtree(int x, ulong mul, ulong add)
    {
        int left = pos[x];
        int right = pos[x] + subtreeSize[x] - 1;

        seg.Update(left, right, mul, add);
    }

    static ulong QuerySubtree(int x)
    {
        int left = pos[x];
        int right = pos[x] + subtreeSize[x] - 1;

        return seg.Query(left, right);
    }

    static void UpdatePath(int a, int b, ulong mul, ulong add)
    {
        while (top[a] != top[b])
        {
            if (depth[top[a]] < depth[top[b]])
            {
                int temp = a;
                a = b;
                b = temp;
            }

            seg.Update(pos[top[a]], pos[a], mul, add);
            a = parent[top[a]];
        }

        if (depth[a] > depth[b])
        {
            int temp = a;
            a = b;
            b = temp;
        }

        seg.Update(pos[a], pos[b], mul, add);
    }

    static ulong QueryPath(int a, int b)
    {
        ulong result = 0;

        while (top[a] != top[b])
        {
            if (depth[top[a]] < depth[top[b]])
            {
                int temp = a;
                a = b;
                b = temp;
            }

            result = (result + seg.Query(pos[top[a]], pos[a])) & MASK;
            a = parent[top[a]];
        }

        if (depth[a] > depth[b])
        {
            int temp = a;
            a = b;
            b = temp;
        }

        result = (result + seg.Query(pos[a], pos[b])) & MASK;

        return result;
    }

    static void Main()
    {
        var fs = new FastScanner();

        N = fs.NextInt();
        Q = fs.NextInt();

        head = new int[N + 1];
        Array.Fill(head, -1);

        to = new int[(N - 1) * 2];
        next = new int[(N - 1) * 2];

        for (int i = 0; i < N - 1; i++)
        {
            int a = fs.NextInt();
            int b = fs.NextInt();

            AddEdge(a, b);
        }

        parent = new int[N + 1];
        depth = new int[N + 1];
        subtreeSize = new int[N + 1];
        heavy = new int[N + 1];
        top = new int[N + 1];
        pos = new int[N + 1];

        BuildHld();

        seg = new SegmentTree(N);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Q; i++)
        {
            int op = fs.NextInt();

            if (op == 1)
            {
                int x = fs.NextInt();
                ulong v = (ulong)fs.NextInt();

                UpdateSubtree(x, 1, v & MASK);
            }
            else if (op == 2)
            {
                int x = fs.NextInt();
                int y = fs.NextInt();
                ulong v = (ulong)fs.NextInt();

                UpdatePath(x, y, 1, v & MASK);
            }
            else if (op == 3)
            {
                int x = fs.NextInt();
                ulong v = (ulong)fs.NextInt();

                UpdateSubtree(x, v & MASK, 0);
            }
            else if (op == 4)
            {
                int x = fs.NextInt();
                int y = fs.NextInt();
                ulong v = (ulong)fs.NextInt();

                UpdatePath(x, y, v & MASK, 0);
            }
            else if (op == 5)
            {
                int x = fs.NextInt();

                sb.Append(QuerySubtree(x)).Append('\n');
            }
            else
            {
                int x = fs.NextInt();
                int y = fs.NextInt();

                sb.Append(QueryPath(x, y)).Append('\n');
            }
        }

        Console.Write(sb.ToString());
    }
}