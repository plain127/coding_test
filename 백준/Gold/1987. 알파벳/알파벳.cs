using System;

class Program
{
    static int r, c;
    static char[][] graph;
    static bool[] visited = new bool[26];
    static int cnt = 0;

    static int[,] dirs = new int[,] { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

    static void Dfs(int col, int row, int depth)
    {
        if (depth > cnt)
            cnt = depth;

        for (int i = 0; i < 4; i++)
        {
            int nx = col + dirs[i, 0];
            int ny = row + dirs[i, 1];

            if (0 <= nx && nx < c && 0 <= ny && ny < r)
            {
                int num = graph[ny][nx] - 'A';
                if (!visited[num])
                {
                    visited[num] = true;
                    Dfs(nx, ny, depth + 1);
                    visited[num] = false; // 백트래킹
                }
            }
        }
    }

    static void Main()
    {
        var input = Console.ReadLine().Split();
        r = int.Parse(input[0]);
        c = int.Parse(input[1]);

        graph = new char[r][];
        for (int i = 0; i < r; i++)
        {
            string line = Console.ReadLine();
            graph[i] = line.ToCharArray();
        }

        visited[graph[0][0] - 'A'] = true;
        Dfs(0, 0, 1);

        Console.WriteLine(cnt);
    }
}