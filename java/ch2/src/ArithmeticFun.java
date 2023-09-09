public class ArithmeticFun {
    public static void main(String[] args){
        int a = 10;
        int b = 15;
        int result = a + b;
        int difference = a - b;
        int product = a * b;
        float quotient = (float)b / (float)a;
        int remainder = b % a;

        System.out.println(a + " + " + b + " = " + result);
        System.out.println(a + " - " + b + " = " + difference);
        System.out.println(a + " * " + b + " = " + product);
        System.out.println(b + " / " + a + " = " + quotient);
        System.out.println(b + " % " + a + " = " + remainder);
        System.out.println('\n');

        //  Compound arithmetic operators
        result += 20;   // result = result + 20
        difference -= 20;
        product *= 20;
        quotient /= 20;
        remainder %= 20;

        System.out.println("Result: " + result);
        System.out.println("Difference: " + difference);
        System.out.println("Product : " + product);
        System.out.println("Quotient : " + quotient);
        System.out.println("Remainder : " + remainder);

        result ++;  //++result;
        System.out.println("Result++ " + result);
        result --;  //--result;
        System.out.println("Result-- " + result);


        // Challenge:
        System.out.println("\nChallenge:");
        product *= 2;   //product = product * 2
        System.out.println("Product * 2 = " + product);
    }
}
