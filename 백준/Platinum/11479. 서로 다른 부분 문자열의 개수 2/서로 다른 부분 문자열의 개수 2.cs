using System;
using System.Text;

class Program
{
    static int[] BuildSuffixArray(string original)
    {
        string s = original + '\0';
        int n = s.Length;

        int[] p = new int[n];
        int[] c = new int[n];
        int[] pn = new int[n];
        int[] cn = new int[n];

        int alphabet = 256;
        int[] cnt = new int[Math.Max(alphabet, n)];

        for (int i = 0; i < n; i++)
            cnt[s[i]]++;

        for (int i = 1; i < alphabet; i++)
            cnt[i] += cnt[i - 1];

        for (int i = 0; i < n; i++)
            p[--cnt[s[i]]] = i;

        c[p[0]] = 0;
        int classes = 1;

        for (int i = 1; i < n; i++)
        {
            if (s[p[i]] != s[p[i - 1]])
                classes++;

            c[p[i]] = classes - 1;
        }

        for (int h = 0; (1 << h) < n; h++)
        {
            int len = 1 << h;

            for (int i = 0; i < n; i++)
            {
                pn[i] = p[i] - len;

                if (pn[i] < 0)
                    pn[i] += n;
            }

            Array.Clear(cnt, 0, classes);

            for (int i = 0; i < n; i++)
                cnt[c[pn[i]]]++;

            for (int i = 1; i < classes; i++)
                cnt[i] += cnt[i - 1];

            for (int i = n - 1; i >= 0; i--)
                p[--cnt[c[pn[i]]]] = pn[i];

            cn[p[0]] = 0;
            int newClasses = 1;

            for (int i = 1; i < n; i++)
            {
                int cur1 = c[p[i]];
                int cur2 = c[(p[i] + len) % n];

                int prev1 = c[p[i - 1]];
                int prev2 = c[(p[i - 1] + len) % n];

                if (cur1 != prev1 || cur2 != prev2)
                    newClasses++;

                cn[p[i]] = newClasses - 1;
            }

            int[] temp = c;
            c = cn;
            cn = temp;

            classes = newClasses;

            if (classes == n)
                break;
        }

        int originalLength = original.Length;
        int[] sa = new int[originalLength];

        for (int i = 1; i < n; i++)
            sa[i - 1] = p[i];

        return sa;
    }

    static long GetLcpSum(string s, int[] sa)
    {
        int n = s.Length;

        int[] rank = new int[n];

        for (int i = 0; i < n; i++)
            rank[sa[i]] = i;

        int h = 0;
        long lcpSum = 0;

        for (int i = 0; i < n; i++)
        {
            int r = rank[i];

            if (r == 0)
                continue;

            int j = sa[r - 1];

            while (i + h < n && j + h < n && s[i + h] == s[j + h])
                h++;

            lcpSum += h;

            if (h > 0)
                h--;
        }

        return lcpSum;
    }

    static void Main()
    {
        string s = Console.ReadLine();

        int n = s.Length;

        int[] sa = BuildSuffixArray(s);

        long totalSubstrings = (long)n * (n + 1) / 2;
        long lcpSum = GetLcpSum(s, sa);

        Console.WriteLine(totalSubstrings - lcpSum);
    }
}