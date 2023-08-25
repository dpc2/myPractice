#include <iostream>
#include <string>

using namespace std;

// Convention is to use upper case
class Robot {

// No indentation
public:
    Robot(string name, int version_number)
        : name(name), version_number(version_number),
        internal_temperature(30.0)
    {

    }
    void say_hi()
    {
        cout << "Hello, world! My name is "
             << name
             << ", ready to help!"
             << endl;      
    }

    void init_hardware()
    {
        cout << "Init hardware." << endl;
    }

    void print_info()
    {
        say_hi();
        cout << "Version number: " << version_number << endl;
        cout << "Temperature: " << internal_temperature << endl;

        // name = "";
    }
private:
    string name;
    int version_number;
    double internal_temperature;
};


int main()
{
    return 0;
}