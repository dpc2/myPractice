#include <iostream>
#include <vector>

using namespace std;

int main(){

    string myString = "Hello World!";
    cout << myString << " " << &myString << endl;
    string *myPointer = &myString;
    cout << "My string pointer:\n" << myPointer << endl;
    cout << "My string pointer location: " << &myPointer << endl;

    //Change myString using pointer
    *myPointer = "Goodbye, cruel world!";
    cout << *myPointer << "\n\n";


    vector<int> myVector{1, 2, 3, 4, 5, 6};
    cout << myVector[3]<< endl;

    int *newPointer = &myVector[3];
    cout << &myVector[3] << endl;
    cout << newPointer << endl;
    cout << *newPointer << endl;
    cout << &newPointer << endl;


    return 0;
}