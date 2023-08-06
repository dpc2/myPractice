#include <iostream>
#include <vector>

// 'using' declarations
using std::cout;
using std::endl;
using std::string;
using std::vector;

int main()
{
    // Standard arrays cannot change in size
    double temperature_list[4] = { 34.5, 27.8, 26.8, 22.0 };

    cout << temperature_list[3] << endl;
    temperature_list[3] = 15.4;
    cout << temperature_list[3] << endl;


    // Vectors are much more flexible
    vector<double> temperatures = { 34.5, 27.8, 26.8 };

    cout << temperatures.at(1) << endl;
    temperatures.at(1) = 30.7;
    cout << temperatures.at(1) << endl;

    temperatures.push_back(17.4);
    cout << temperatures.size() << endl;
        
    return 0;
}