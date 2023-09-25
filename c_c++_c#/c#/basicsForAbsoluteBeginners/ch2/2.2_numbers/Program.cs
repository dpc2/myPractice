using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // Whole numbers
            int i = 10;
            Console.WriteLine(i);
            Console.WriteLine("Enter a number:\n");
            int j = int.Parse(Console.ReadLine());
            Console.WriteLine(j);
        
            short s = 100;
            long l = 10000;
            long otherL = 20000L;
            uint ui = 12;

            int intNum = (int)l;
            short shortNum = (short)i;

            // Decimal numbers
            float f = 10.5f;
            double d = 123.99;
            decimal dd = 345.80m;

            float f2 = (float)dd;
            decimal d2 = (decimal)f;
        
        }
    }
}
