#include "my_vector_functions.hpp"

int main()
{
    vector<double> my_vector = {4.5, 5.6, 6.7};
    print_my_vector(my_vector);
    add_zeroes_to_vector(my_vector, 5);
    print_my_vector(my_vector);
} 