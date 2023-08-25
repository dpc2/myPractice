#include "my_vector_functions.hpp"

int main()
{
    vector<double> vector_1 = { 1.2, 3.4, 5.6 };
    vector<double> vector_2 = { 7.8, 9.0, 1.2 };

    print_my_vector(vector_1);
    print_my_vector(vector_2);
    
    add_my_vectors(vector_1, vector_2);
    print_my_vector(vector_1);
}