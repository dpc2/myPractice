#include <iostream>

using namespace std;

//Factorial function
int Factorial(int x){
    int result = 1;
    for (int i = x; i > 0; i--){
        result *= i;
        cout << result << endl;
    }
    return result;
}

int main(){
    int input;
    cout << "Enter an integer to calculate factorial:\n";
    cin >> input;

    int result = Factorial(input);
    cout << "Factorial of " << input << ":\n"
         << result << endl;

    return 0;
}