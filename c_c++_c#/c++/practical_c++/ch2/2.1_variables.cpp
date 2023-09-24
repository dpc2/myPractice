// Identifiers cin and cout are defined inside standard
// header file <iostream> of the namespace std

// Namespace std:
            // |
            // |--<string>
            // |--<vector>
            // |--<iostream>
                        // |
                        // |-- cin, cout, endl, etc.


#include <iostream>

// 'using' declarations
using std::cout;
using std::endl;

// std namespace with 'using' directive:
// Brings in all identifiers of the namespace std as if 
// they were declared globally
// This is considered poor practice, as it could create
// conflicts if custom functions are defined
using namespace std;


int main()
{
    int number = 2 - 3;

    // Namespace: std
    // Scope resolution operator: ::
    // Identifier belonging to std namespace: cout, endl

    // std::cout << number << std::endl;
    // std::cout << number + 1 << std::endl;
    // std::cout << number + 2 << std::endl;
    // std::cout << number + 3 << std::endl;

    cout << number << endl;
    cout << number + 1 << endl;
    cout << number + 2 << endl;
    cout << number + 3 << endl;

    int b = number + 2;
    cout << b << endl;

    int c = number + b;
    cout << c << endl;

    // Better to use meaningful names for variables:
    int temperature = 0;
    int user_age = 32;

    return 0;
}