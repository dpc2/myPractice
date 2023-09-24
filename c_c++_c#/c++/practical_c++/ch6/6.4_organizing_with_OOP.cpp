#include "robot.hpp"


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