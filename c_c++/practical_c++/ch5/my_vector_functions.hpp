#ifndef MY_VECTOR_FUNCTIONS_H
#define MY_VECTOR_FUNCTIONS_H

#include <vector>
#include <string>

using namespace std;

void add_zeroes_to_vector(vector<double> &my_input, int zeroes);
void print_my_vector(vector<double> my_input);
void add_my_vectors(vector<double> &vector_1, const vector<double> &vector_2);
int return_occurences_of_string(const vector<string> &my_input, string my_match);

#endif