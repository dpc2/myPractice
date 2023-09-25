using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            //Exercise 1
            // Comment this line using single line comments

            //Exercise 2
            /* Comment this and the next line using multiline comment.
            VS will show error if we dont comment normal text. */

            //Exercise 3
            // C# statement to print your name to the console
            Console.WriteLine("Enter your name:\n");
            string str = Console.ReadLine();
            Console.WriteLine("Your name is:\n" + str);
        }
    }
}
