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

        int value = 0;

        while (c > 32)
        {
            value = value * 10 + (c - '0');
            c = Read();
        }

        return value;
    }
}

class Program
{
    static void Main()
    {
        var fs = new FastScanner();

        int n = fs.NextInt();
        int[] piles = new int[n];

        int maxPile = 0;

        for (int i = 0; i < n; i++)
        {
            piles[i] = fs.NextInt();

            if (piles[i] > maxPile)
                maxPile = piles[i];
        }

        List<int> fibs = new List<int>();
        fibs.Add(1);
        fibs.Add(2);

        while (true)
        {
            int next = fibs[fibs.Count - 1] + fibs[fibs.Count - 2];

            if (next > maxPile)
                break;

            fibs.Add(next);
        }

        byte[] grundy = new byte[maxPile + 1];

        int[] seen = new int[64];
        int stamp = 0;

        for (int stones = 1; stones <= maxPile; stones++)
        {
            stamp++;

            for (int i = 0; i < fibs.Count; i++)
            {
                int move = fibs[i];

                if (move > stones)
                    break;

                seen[grundy[stones - move]] = stamp;
            }

            byte mex = 0;

            while (seen[mex] == stamp)
                mex++;

            grundy[stones] = mex;
        }

        int xor = 0;

        for (int i = 0; i < n; i++)
        {
            xor ^= grundy[piles[i]];
        }

        if (xor != 0)
            Console.WriteLine("koosaga");
        else
            Console.WriteLine("cubelover");
    }
}