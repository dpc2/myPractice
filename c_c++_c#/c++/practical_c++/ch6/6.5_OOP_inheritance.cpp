#include "robot.hpp"


int main()
{
    Robot robot1("R2D2", 3);
    Robot robot2("C3PO", 1);

    RoboticArm arm("Bob the arm", 4, 300);
    arm.print_info();
    arm.pick_object(1, 2);
    arm.place_object(3, 4);

    return 0;
}