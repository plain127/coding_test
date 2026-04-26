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

struct Query
{
    public int Block;
    public int OrderRight;
    public int Left;
    public int Right;
    public int Id;

    public Query(int block, int orderRight, int left, int right, int id)
    {
        Block = block;
        OrderRight = orderRight;
        Left = left;
        Right = right;
        Id = id;
    }
}

class Program
{
    static int n;
    static int shift;

    static int[] prefixValue;
    static int[] occPos;
    static int[] occ;
    static int[] head;
    static int[] tail;

    static int[] countLength;
    static int[] bucket;
    static int lengthBlock;
    static int bucketCount;

    static int GetSpan(int value)
    {
        if (head[value] > tail[value])
            return -1;

        return occ[tail[value]] - occ[head[value]];
    }

    static void AddLength(int length)
    {
        countLength[length]++;
        bucket[length / lengthBlock]++;
    }

    static void RemoveLength(int length)
    {
        countLength[length]--;
        bucket[length / lengthBlock]--;
    }

    static void AddIndex(int index, bool toLeft)
    {
        int value = prefixValue[index];

        int oldSpan = GetSpan(value);

        if (oldSpan != -1)
            RemoveLength(oldSpan);

        int position = occPos[index];

        if (head[value] > tail[value])
        {
            head[value] = position;
            tail[value] = position;
        }
        else if (toLeft)
        {
            head[value] = position;
        }
        else
        {
            tail[value] = position;
        }

        int newSpan = GetSpan(value);
        AddLength(newSpan);
    }

    static void RemoveIndex(int index, bool fromLeft)
    {
        int value = prefixValue[index];

        int oldSpan = GetSpan(value);
        RemoveLength(oldSpan);

        if (fromLeft)
            head[value]++;
        else
            tail[value]--;

        int newSpan = GetSpan(value);

        if (newSpan != -1)
            AddLength(newSpan);
    }

    static int GetAnswer()
    {
        for (int b = bucketCount - 1; b >= 0; b--)
        {
            if (bucket[b] == 0)
                continue;

            int right = Math.Min(n, (b + 1) * lengthBlock - 1);
            int left = b * lengthBlock;

            for (int len = right; len >= left; len--)
            {
                if (countLength[len] > 0)
                    return len;
            }
        }

        return 0;
    }

    static void Main()
    {
        var fs = new FastScanner();

        n = fs.NextInt();

        int[] prefix = new int[n + 1];

        for (int i = 1; i <= n; i++)
        {
            int value = fs.NextInt();
            prefix[i] = prefix[i - 1] + value;
        }

        shift = n;
        int valueRange = 2 * n + 1;

        prefixValue = new int[n + 1];
        int[] valueCount = new int[valueRange];

        for (int i = 0; i <= n; i++)
        {
            int value = prefix[i] + shift;
            prefixValue[i] = value;
            valueCount[value]++;
        }

        int[] start = new int[valueRange];
        int total = 0;

        for (int v = 0; v < valueRange; v++)
        {
            start[v] = total;
            total += valueCount[v];
        }

        occ = new int[n + 1];
        occPos = new int[n + 1];

        int[] fill = new int[valueRange];

        for (int v = 0; v < valueRange; v++)
            fill[v] = start[v];

        for (int i = 0; i <= n; i++)
        {
            int value = prefixValue[i];
            int pos = fill[value]++;

            occ[pos] = i;
            occPos[i] = pos;
        }

        head = new int[valueRange];
        tail = new int[valueRange];

        for (int v = 0; v < valueRange; v++)
        {
            head[v] = start[v];
            tail[v] = start[v] - 1;
        }

        int m = fs.NextInt();

        int queryBlock = (int)Math.Sqrt(n + 1) + 1;
        Query[] queries = new Query[m];

        for (int id = 0; id < m; id++)
        {
            int left = fs.NextInt();
            int right = fs.NextInt();

            int qLeft = left - 1;
            int qRight = right;

            int block = qLeft / queryBlock;
            int orderRight = (block % 2 == 0) ? qRight : -qRight;

            queries[id] = new Query(block, orderRight, qLeft, qRight, id);
        }

        Array.Sort(queries, (a, b) =>
        {
            if (a.Block != b.Block)
                return a.Block.CompareTo(b.Block);

            return a.OrderRight.CompareTo(b.OrderRight);
        });

        lengthBlock = (int)Math.Sqrt(n + 1) + 1;
        bucketCount = (n + lengthBlock) / lengthBlock + 1;

        countLength = new int[n + 1];
        bucket = new int[bucketCount];

        int[] answers = new int[m];

        int curLeft = 0;
        int curRight = -1;

        foreach (Query query in queries)
        {
            while (curLeft > query.Left)
            {
                curLeft--;
                AddIndex(curLeft, true);
            }

            while (curRight < query.Right)
            {
                curRight++;
                AddIndex(curRight, false);
            }

            while (curLeft < query.Left)
            {
                RemoveIndex(curLeft, true);
                curLeft++;
            }

            while (curRight > query.Right)
            {
                RemoveIndex(curRight, false);
                curRight--;
            }

            answers[query.Id] = GetAnswer();
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++)
        {
            sb.Append(answers[i]).Append('\n');
        }

        Console.Write(sb.ToString());
    }
}