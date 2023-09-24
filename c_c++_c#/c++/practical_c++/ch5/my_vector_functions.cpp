#include "my_vector_functions.hpp"

#include <iostream>


void add_zeroes_to_vector(vector<double> &my_input, int zeroes){
    for (int i = 0; i < zeroes; i++){
        my_input.push_back(0);
    }
}

void print_my_vector(vector<double> my_input){
    for (double each_item: my_input){
        cout << each_item << ", ";
    }
    cout << endl;
}

void add_my_vectors(vector<double> &vector_1, const vector<double> &vector_2){
    for (double each_item: vector_2){
        vector_1.push_back(each_item);
    }
}

int return_occurences_of_string(const vector<string> &my_input, string my_match){
    int my_count = 0;
    for (string each_item: my_input){
        if (each_item == my_match){
            my_count++;
        }
    }
    return my_count;
}