#include <iostream>

// 'using' declarations
using std::cout;
using std::endl;
using std::string;


int main()
{
    double temperature_list[4] = { 34.5, 27.8, 26.8, 22.0 };

    cout << temperature_list[3] << endl;
    temperature_list[3] = 15.4;
    cout << temperature_list[3] << endl;

    return 0;
}