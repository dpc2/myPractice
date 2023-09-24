#include <iostream>

using namespace std;

int main(){

    // Old school initialization
    int a1;    // Uninitialized
    int a2 = 0;    // Copy initialization 
    int a3(5);    // Direct initialization
    string s1;
    string s2("C++");

    cout << a1 << endl << a2 << endl
         << a3 << endl;
    
    cout << s1 << endl << s2 << endl;

    char arr1[8];    // Uninitialized
    char arr2[8] = {'\0'};    // Initialized with null terminating character and copy initialization
    char arr3[8] = {'a', 'b', 'c', 'd'};    // Aggregate initialization with copy initialization
    char arr4[8] = {"abcd"};    // Copy initialization


    // This gets pretty complicated, uniform initialization is better

    int b1{};    // Value initialization
    int b2[5];    // Direct initialization
    int b3();    // Most vexing parse - a mistake

    char arr5[8]{};
    char arr6[8]{"Hello"};


    // Heap based objects
    int *p1 = new int{};
    
    char *p2 = new char[8]{};
    char *p3 = new char[8]{"Hello"};

/*
1. Value initialization => T obj{};
2. Direct initialization => T obj{v};
3. Copy initialization => T obj = v;    // Avoid this with user defined objects

Uniform initialization advantages:
1. It forces initialization
2. You can use direct initialization for array types
3. It prevents narrowing conversions
4. Uniform syntax for all types
*/

    // Example of narrowing conversion:
    float f{};
    int i{f};

    return 0;
}