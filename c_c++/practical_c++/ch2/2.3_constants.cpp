#include <iostream>

// 'using' declarations
using std::cout;
using std::endl;
using std::string;


int main()
{

    // Must initialize on the same line, can't use:
        // const int var;
        // var = 10;
        
    const int seconds_per_hour = 3600;
    const double max_allowed_temperature = 76.8;

    // seconds_per_hour = 3;

    int user_age = 32;
    double temperature = 20.6;
    bool is_alive = false;
    string username = "Deez Nuts";

    cout << seconds_per_hour << endl;
    cout << max_allowed_temperature << endl;


    return 0;
}