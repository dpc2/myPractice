#include <iostream>

using namespace std;

int main(){

    int user_age = 77;

    if (user_age < 18){
        cout << "You're not an adult yet." << endl;
    }
    else if ((user_age >= 18) && (user_age < 30)) {
        cout << "You are an adult below 30." << endl;
    }
    else if ((user_age >= 30) && (user_age < 40)) {
        cout << "You are in your 30s" << endl;
    }
    else {
        cout << "You are 40 or more." << endl;
    }
    
    cout << "End of program." << endl;

    return 0;
}