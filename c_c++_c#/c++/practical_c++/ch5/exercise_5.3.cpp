#include "my_vector_functions.hpp"
#include <iostream>

int main()
{
    vector<string> my_string = {"apple", "banana", "cherry", "durian", "durian"};
    int my_result = return_occurences_of_string(my_string, "durian");
    cout << my_result << endl;
}