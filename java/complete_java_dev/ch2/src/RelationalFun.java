public class RelationalFun {
    public static void main(String[] args){
        boolean myBool = true;
        boolean yourBool = false;
        int myAge = 32;
        int yourAge = 20;
        int bobsAge = 20;

        System.out.println("myBool is " + myBool);
        System.out.println("yourBool is " + yourBool);

        // Relational operations
        System.out.println("\nmyAge: " + myAge);
        System.out.println("yourAge: " + yourAge);
        System.out.println("bobsAge: " + bobsAge);

        boolean ageComparison = myAge > yourAge;
        System.out.println("myAge > yourAge ? " + ageComparison);

        ageComparison = yourAge > bobsAge;
        System.out.println("yourAge > bobsAge ? " + ageComparison);

        ageComparison = yourAge == bobsAge;
        System.out.println("yourAge == bobsAge ? " + ageComparison);

        // Comparing (reference type) Strings:
        String mystring1 = "Hello World!";
        String mystring2 = "Hello World!";
        //String mystring2 = new String("Hello World!");

        boolean stringCompare = mystring1 == mystring2;
        System.out.println("myString1: " + mystring1 + "\nmystring2: " + mystring2 + "\nMatch? " + stringCompare);

        String myName = "John";
        String yourName = "Johnny";
        boolean nameComparison = myName.equals(yourName);
        System.out.println("Do names match? " + nameComparison);


        // Challenge:
        int currentAge = 32;
        boolean newAgeComparison = currentAge >= 21;
        System.out.println("Can drink? " + newAgeComparison);

    }//end main
}
