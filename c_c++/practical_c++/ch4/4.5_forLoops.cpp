#include <iostream>

using namespace std;

int main(){

    int myMax = 1000;

    for (int i=0; i< myMax; i++){
        cout << "Hello World! " + to_string(i) << endl;
        cout << "Hello! " << i << endl;
    }

    

    return 0;
}