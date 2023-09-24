#include <iostream>
#include <vector>

using namespace std;

void add_zeroes_copy(vector<int> myList, int num_of_zeroes){
    for (int i=0; i < num_of_zeroes; i++){
        myList.push_back(0);
    }
    cout << "(In function): Size of my list: " << myList.size() << endl;
}

void add_zeroes_reference(vector<int> &myList, int num_of_zeroes){
    for (int i=0; i < num_of_zeroes; i++){
        myList.push_back(0);
    }
    cout << "(In function): Size of my list: " << myList.size() << endl;
}

// Passing vectory by reference, but protecting it with const so it can't be modified
void print_all_elements(const vector<int> &myList){
    for (int number: myList){
        cout << number << endl;
    }
    // myList.push_back(0);
}


int main(){
    
    vector<int> myList = { 5, 6, 7};
    cout << "Size of my list: " << myList.size() << endl;
    add_zeroes_copy(myList, 4);
    cout << "Size of my list (passed as copy): " << myList.size() << endl;

    add_zeroes_reference(myList, 4);
    cout << "Size of my new list (passed as reference): " << myList.size() << endl;

    return 0;
}