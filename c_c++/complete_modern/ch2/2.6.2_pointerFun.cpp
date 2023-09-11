#include <iostream>

using namespace std;

int main(){

    string myString = "Hello World!";
    cout << myString << " " << &myString << endl;
    string *myPointer = &myString;
    cout << "My string pointer:\n" << myPointer << endl;
    cout << "My string pointer location: " << &myPointer << endl;

    //Change myString using pointer
    *myPointer = "Goodbye, cruel world!";
    cout << *myPointer << endl;

    return 0;
}