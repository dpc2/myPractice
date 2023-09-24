#include <iostream>

using namespace std;

// Passing by reference
void Swap1(int &x, int &y){
    int temp = x;
    x = y;
    y = temp;
    cout << "Function &x: " << &x << endl;
    cout << "Function &y: " << &y << endl << endl;
}

// Passing by address
void Swap2(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
    cout << "Function &x: " << &x << endl;
    cout << "Function &y: " << &y << endl << endl;
}

void Print(int *ptr){
    cout << "Print\n";
    cout << ptr << endl;
    cout << &ptr << endl;

    if(ptr != nullptr)
        cout << *ptr << endl;
}

void Print2(int &ptr){
    cout << "Print2\n";
    cout << ptr << endl;
    // cout << &ptr << endl;
}

int main(){

    int x = 5;
    int y = 10;
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "&x: " << &x << endl;
    cout << "&y: " << &y << endl << endl;

    Swap1(x, y);
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "&x: " << &x << endl;
    cout << "&y: " << &y << endl << endl;

    Swap2(&x, &y);
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "&x: " << &x << endl;
    cout << "&y: " << &y << endl << endl;


    // Using Print
    int z = 5;
    cout << "&z: " << &z << endl;
    Print(&z);
    Print(nullptr);
    Print2(z);
    // Print2(nullptr)

    // Conclusion: When passing by reference, the reference cannot be null.
    // The reference will always have a valid value. If a function accepts
    // a pointer, the first thing you have to do is check for null.
    return 0;
}