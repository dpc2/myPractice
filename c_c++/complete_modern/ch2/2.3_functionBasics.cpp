#include <iostream>
#include "math.h"

using namespace std;

// It is not typical to put function definitions before main(),
// but it will be done for simplicity in this course
void Print(char ch);

int main(){

    int x, y;
    cout << "Enter two integer values: " << endl;
    cin >> x >> y;
    // int result = x + y;
    int myResult = Add(x, y);
    cout << "Result is: " << myResult << endl;

    Print('?');

    return 0;
}

void Print(char ch){
    for(int i = 0; i < 10; i++){
        cout << ch << endl;
    }
}
