#include <iostream>
#include <string>

using namespace std;


class Robot {   // Convention is to use upper case

public:     // No indentation
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
    }
    
private:
    string name;
    int version_number;
    double internal_temperature;
};


int main()
{
    Robot robot1("R2D2", 3);

    robot1.say_hi();
    robot1.init_hardware();
    robot1.print_info();

    // robot1.version_number;   // version_number is private and cannot be accessed

    Robot robot2("C3PO", 1);

    robot2.print_info();

    return 0;
}