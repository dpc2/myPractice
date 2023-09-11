#include <iostream>

using namespace std;

int main(){
    int x{10};
    cout << "Variable x: " + to_string(x) << endl;
    cout << "&x:\n" << &x << endl << endl;

    //float *pointer = &x;  //Can't mismatch pointer type with variable type
    int *pointer = &x;
    cout << "Printing out pointer:\n" << pointer << endl;
    cout << "Printing out *pointer:\n" << *pointer << endl << endl;

    void *pointer2 = &x;    // void pointers are agnostic
    cout << "Void pointer:\n" << pointer2 << endl << endl;

    // Uninitialized pointers point to random addresses
    // if they compile at all. Now it's just 0?
    void *pointer3;    
    cout << "Uninitialized pointer:\n" << pointer3 << "\n\n";


    // Using dereference operator to indirectly change the value
    // of the variable
    *pointer = 20;
    cout << "New value for x:\n" << x << endl;
    cout << "Printing out &x:\n" << &x << endl;
    cout << "Printing out pointer:\n" << pointer << endl;
    cout << "Printing out &pointer:\n" << &pointer << endl;
    cout << "Printing out *pointer:\n" << *pointer << endl << endl;

    int y = *pointer;
    cout << y << endl;


    // Null Pointers
    void *pointer4 = nullptr;
    cout << pointer4 << endl << endl;

    int *pointer5 = nullptr;
    cout << "pointer5:\n" << pointer5 << endl;
    cout << "&pointer5:\n" << &pointer5 << endl;
    cout << "*pointer:\n" << *pointer5 << endl; // This causes core dump
    //*pointer5 = 10;    // This causes core dump


    return 0;
}