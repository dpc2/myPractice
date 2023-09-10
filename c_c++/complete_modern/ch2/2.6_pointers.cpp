#include <iostream>

using namespace std;

int main(){
    int x{10};
    cout << &x << endl;

    // float *pointer = &x;
    int *pointer = &x;
    cout << pointer << endl;

    void *pointer2 = &x;    // void pointers are agnostic
    cout << pointer2 << endl;

    // Uninitialized pointers point to random addresses
    // if they compile at all
    void *pointer3;    
    cout << pointer3 << endl;


    // Using dereference operator to indirectly change the value
    // of the variable
    *pointer = 20;
    cout << x << endl;

    int y = *pointer;
    cout << y << endl;


    // Null Pointer
    void *pointer4 = nullptr;
    cout << pointer4 << endl;

    int *pointer5 = nullptr;
    cout << pointer5 << endl;
    *pointer5 = 10;    // This causes core dump


    return 0;
}