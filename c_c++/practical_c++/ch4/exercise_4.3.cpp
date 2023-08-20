#include <iostream>
#include <vector>

using namespace std;

double max_value(vector<double> input_vector){

    double my_max;

    for (double iterable: input_vector){
        if (my_max < iterable){
            my_max = iterable;
        }
    }

    cout << "The max value in this list is...\n";

    return my_max;
}

int main(){
    
    vector<double> my_list;

    double myEntry;

    while (myEntry != 0){
        cout << "Please enter a number:\n";
        cin >> myEntry;
        if (myEntry != 0){
            my_list.push_back(myEntry);
        }
    }

    cout << max_value(my_list) << endl;
    return 0;
}