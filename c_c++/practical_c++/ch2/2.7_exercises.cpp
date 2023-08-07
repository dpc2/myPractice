#include <iostream>
#include <vector>
#include <numeric>


int main(){

    // Exercise 1.1
    std::string username;
    int age;

    std::cout << "Hello User, what is your name?" << std::endl;
    std::cin >> username;
    std::cout << "Age?" << std::endl;
    std::cin >> age;

    std::cout << "Name: " << username << std::endl << "Age: " << age << std::endl;



    // Exercise 1.2
    int integer_1, integer_2;
    
    std::cout << "Enter two integers: ";
    std::cin >> integer_1;
    std::cin >> integer_2;

    int sum = integer_1 + integer_2;

    std::cout << integer_1 << " + " << integer_2 << " = " << sum << std::endl;



    // Exercise 1.3
    double float_1, float_2, float_3, float_4;

    std::cout << "Enter four floating point numbers: ";
    std::cin >> float_1;
    std::cin >> float_2;
    std::cin >> float_3;
    std::cin >> float_4;

    std::vector<double> my_floats = {float_1, float_2, float_3, float_4};
    double result = std::accumulate(my_floats.begin(), my_floats.end(), 0.0) / my_floats.size();

    std::cout << "The average is: " << result << std::endl;


    return 0;
}