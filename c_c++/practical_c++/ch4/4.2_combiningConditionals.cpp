#include <iostream>

using namespace std;

int main(){
    
    cout << boolalpha;

    cout << ((1 == 1) || (3 == 4)) << endl;
    cout << ((1 == 1) && (3 == 4)) << endl;
    cout << ((1 == 1) || (3 == 3)) << endl;

    double temperature = 25.0;

    cout << ((temperature >= 20.0) && (temperature < 30.0)) << endl;

    return 0;
}