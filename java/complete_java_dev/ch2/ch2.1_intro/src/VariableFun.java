public class VariableFun {
    public static void main(String[] args){

        // Variable, data type, identifier,
        // declaration, assignment, initialization

        int myAge;    // Declaration
        myAge = 19;   // Initialization
        // Int variable directly holds the value of 19

        // Symbolic constants (or just constants)
        // It is common to use "snake" or underscore case
        final int SOME_NUM = 150;

        String name = "Billy";
        // String variable holds the address of the string
        // object in memory

        System.out.print(name + " is " + myAge);
        System.out.println(name + " is " + myAge);
        // println inserts a new line

        System.out.print(name + " is " + myAge + "\n");
        System.out.println(name + " is " + myAge);

        String myHomeTown = "Ladera Ranch, CA";
        System.out.println("My hometown is: " + myHomeTown);
    }
}
