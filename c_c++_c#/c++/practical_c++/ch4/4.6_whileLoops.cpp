#include <iostream>

using namespace std;

int main(){

    cout << "My for loop\n";

    // Use for loops when you know exactly how many times you need to loop
    for (int i=0; i<10; i++){
        cout << "Hello! " << i << endl;
    }

    // Use a while loop when you don't know how many times to go around
    cout << "My while loop\n";

    int i = 0;
    while (i < 10){
        cout << "Hellooo " << i << endl;
        i++;
    }
    
    return 0;
}