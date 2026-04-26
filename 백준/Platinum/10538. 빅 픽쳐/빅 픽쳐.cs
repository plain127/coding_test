using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    static int hp, wp, hm, wm;
    static int[] next0;
    static int[] next1;
    static int[] fail;
    static int[] output;
    static int nodeCount = 1;

    static int NewNode()
    {
        int id = nodeCount++;
        return id;
    }

    static void Insert(string s, int id)
    {
        int node = 0;

        for (int i = 0; i < s.Length; i++)
        {
            int ch = s[i] == 'x' ? 0 : 1;

            if (ch == 0)
            {
                if (next0[node] == 0)
                    next0[node] = NewNode();

                node = next0[node];
            }
            else
            {
                if (next1[node] == 0)
                    next1[node] = NewNode();

                node = next1[node];
            }
        }

        output[node] = id;
    }

    static void BuildFail()
    {
        Queue<int> q = new Queue<int>();

        if (next0[0] != 0)
            q.Enqueue(next0[0]);

        if (next1[0] != 0)
            q.Enqueue(next1[0]);

        while (q.Count > 0)
        {
            int cur = q.Dequeue();

            int child = next0[cur];

            if (child != 0)
            {
                fail[child] = next0[fail[cur]];
                q.Enqueue(child);
            }
            else
            {
                next0[cur] = next0[fail[cur]];
            }

            child = next1[cur];

            if (child != 0)
            {
                fail[child] = next1[fail[cur]];
                q.Enqueue(child);
            }
            else
            {
                next1[cur] = next1[fail[cur]];
            }
        }
    }

    static int[] BuildPi(int[] pattern)
    {
        int n = pattern.Length;
        int[] pi = new int[n];

        for (int i = 1; i < n; i++)
        {
            int j = pi[i - 1];

            while (j > 0 && pattern[i] != pattern[j])
                j = pi[j - 1];

            if (pattern[i] == pattern[j])
                j++;

            pi[i] = j;
        }

        return pi;
    }

    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput(), Encoding.ASCII, false, 1 << 20);

        string[] first = sr.ReadLine().Split();
        hp = int.Parse(first[0]);
        wp = int.Parse(first[1]);
        hm = int.Parse(first[2]);
        wm = int.Parse(first[3]);

        int maxNodes = hp * wp + 5;
        next0 = new int[maxNodes];
        next1 = new int[maxNodes];
        fail = new int[maxNodes];
        output = new int[maxNodes];

        Dictionary<string, int> rowId = new Dictionary<string, int>();
        int[] patternIds = new int[hp];
        int idCount = 0;

        for (int r = 0; r < hp; r++)
        {
            string row = sr.ReadLine();

            if (!rowId.TryGetValue(row, out int id))
            {
                id = ++idCount;
                rowId[row] = id;
                Insert(row, id);
            }

            patternIds[r] = id;
        }

        BuildFail();

        int cols = wm - wp + 1;
        int[,] check = new int[hm, cols];

        for (int r = 0; r < hm; r++)
        {
            string line = sr.ReadLine();
            int state = 0;

            for (int c = 0; c < wm; c++)
            {
                int ch = line[c] == 'x' ? 0 : 1;
                state = ch == 0 ? next0[state] : next1[state];

                int id = output[state];

                if (id != 0 && c >= wp - 1)
                {
                    int startCol = c - wp + 1;
                    check[r, startCol] = id;
                }
            }
        }

        int[] pi = BuildPi(patternIds);
        long answer = 0;

        for (int col = 0; col < cols; col++)
        {
            int matched = 0;

            for (int row = 0; row < hm; row++)
            {
                int value = check[row, col];

                while (matched > 0 && value != patternIds[matched])
                    matched = pi[matched - 1];

                if (value == patternIds[matched])
                    matched++;

                if (matched == hp)
                {
                    answer++;
                    matched = pi[matched - 1];
                }
            }
        }

        Console.WriteLine(answer);
    }
}