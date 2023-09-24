using System;

namespace Basics
{
    class Program
    {
        /// <summary>
        /// Basics of the C# language
        /// </summary>
        static void Main(string[] args)
        {
            Console.WriteLine("Hello");

            // C# Blocks
            if(true)
            {
                int a = 100;
                int b = a;
            }

            // C# Comments
            // Single line comments
            /* Multi
            line comments */
            /// Documentation comments

            // C# Read and Write
            string str = Console.ReadLine();
            Console.WriteLine("Hello World!");
            Console.Write("hello");

            Console.WriteLine(str);
        }
    }
}
