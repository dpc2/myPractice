using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // C# characters
            char c = 'a';
            char d = '1';
            char s = '*';

            // Size of char in bytes
            int i = sizeof(char);
            Console.WriteLine("Size of 'char' in bytes: " + i);

            // C# strings
            string s1 = "hello";
            string s2 = "12345";    
            string s3 = "!@#$%";

            Console.WriteLine("Hello world!");
            Console.WriteLine(s1);
            Console.WriteLine(s2);
            Console.WriteLine(s3);

            // Different ways to represent string literals
            string str1 = "world";
            // Verbatim
            // string str2 = "C:\myFolder\test.txt";    // This doesn't work because of the slashes
            string str2 = @"C:\myFolder\test.txt";
            // Interpolated
            string str3 = $"hello {str1}";

            Console.WriteLine(str2);
            Console.WriteLine(str3);

        }
    }
}
