public class ConversionFun {
    public static void main(String[] args){
        double myDouble = 3.14;

        // Numbers have double data type by default in Java
        // float myFloat = (float)3.14;
        float myFloat = 3.14f;  // narrowing/lossy conversion (double to float)
        double yourDouble = myFloat;    // widening/lossless conversion

        // Challenge: Name the Primitive Types
        //  byte - 1 byte (8 bit)
        //  char - 2 bytes (16 bit)
        //  short - 2 bytes (16 bit)
        //  int - 4 bytes (32 bit)
        //  long - 8 bytes (64 bit)
        //  float - 4 bytes (32 bit)
        //  double - 8 bytes (64 bit)
        //  boolean

        short myShort = (short)32767;   // maximum int value for short datatype
        System.out.println(myShort);
        myShort += 1;
        System.out.println(myShort);
    }
}
