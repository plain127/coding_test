using System;
using System.IO;

class Program
{
    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        
        int n = int.Parse(sr.ReadLine());
        int[,] mat = new int[n, 2];

        for (int i = 0; i < n; i++)
        {
            string[] input = sr.ReadLine().Split();
            mat[i, 0] = int.Parse(input[0]);
            mat[i, 1] = int.Parse(input[1]);
        }

        long[,] dp = new long[n, n];
        long INF = long.MaxValue;

        for (int length = 2; length <= n; length++)
        {
            for (int i = 0; i <= n - length; i++)
            {
                int j = i + length - 1;
                dp[i, j] = INF;

                for (int k = i; k < j; k++)
                {
                    long cost = dp[i, k]
                              + dp[k + 1, j]
                              + (long)mat[i, 0] * mat[k, 1] * mat[j, 1];

                    if (cost < dp[i, j])
                        dp[i, j] = cost;
                }
            }
        }

        Console.WriteLine(dp[0, n - 1]);
    }
}