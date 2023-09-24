#include <iostream>

using namespace std;

int main(){

    int x = 10;    // Referent
    int &ref = x;    // Reference

    cout << "x: " << x << endl;
    cout << "ref: " << ref << endl;

    x = 20;
    cout << "ref: " << ref << endl;

    // Print addresses of both:
    cout << "&x: " << &x << endl;
    cout << "&ref: " << &ref << endl << endl;


    // Difference between assigning one variable value to another,
    // and using aliases
    int  y = 30;
    ref = y;

    cout << "y: " << y << endl;
    cout << "ref: " << ref << endl;
    cout << "&y: " << &y << endl;
    cout << "&ref: " << &ref << endl;
    cout << "x: " << x << endl;
    cout << "&x: " << &x << endl;
    return 0;
}