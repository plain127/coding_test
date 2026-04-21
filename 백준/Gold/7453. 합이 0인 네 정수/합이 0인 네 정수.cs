using System;
using System.IO;

class FastScanner
{
    private readonly Stream _stream = Console.OpenStandardInput();
    private readonly byte[] _buffer = new byte[1 << 16];
    private int _ptr, _len;

    private byte Read()
    {
        if (_ptr >= _len)
        {
            _len = _stream.Read(_buffer, 0, _buffer.Length);
            _ptr = 0;
            if (_len == 0) return 0;
        }
        return _buffer[_ptr++];
    }

    public int NextInt()
    {
        byte c;
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

        int num = 0;
        while (c > 32)
        {
            num = num * 10 + (c - (byte)'0');
            c = Read();
        }

        return num * sign;
    }
}

class Program
{
    static int LowerBound(int[] arr, int target)
    {
        int left = 0, right = arr.Length;
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    static int UpperBound(int[] arr, int target)
    {
        int left = 0, right = arr.Length;
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (arr[mid] <= target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    static void Main()
    {
        var fs = new FastScanner();

        int n = fs.NextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        int[] d = new int[n];

        for (int i = 0; i < n; i++)
        {
            a[i] = fs.NextInt();
            b[i] = fs.NextInt();
            c[i] = fs.NextInt();
            d[i] = fs.NextInt();
        }

        int size = n * n;
        int[] ab = new int[size];
        int[] cd = new int[size];

        int idx = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                ab[idx++] = a[i] + b[j];
            }
        }

        idx = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cd[idx++] = c[i] + d[j];
            }
        }

        Array.Sort(cd);

        long ans = 0;
        for (int i = 0; i < size; i++)
        {
            int target = -ab[i];
            int left = LowerBound(cd, target);
            int right = UpperBound(cd, target);
            ans += (right - left);
        }

        Console.WriteLine(ans);
    }
}