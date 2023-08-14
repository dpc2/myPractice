#include <iostream>
#include <vector>

using namespace std;

void name_age()
{
    string name, age;

    cout << "What is your name and age? " << endl;
    cin >> name;
    cin >> age;

    cout << name + " is " + age + " years old." << endl;
}

int add_integers(int number_1, int number_2)
{
    return number_1 + number_2;
}

double myAverage(vector<double> myVector){
    // int mySize = myVector.size();
    // cout << mySize << endl;
    double result;
    for(int i = 0; i < myVector.size(); i++){
        result += myVector[i];
    }
    return result / myVector.size();
}


int main()
{
    // Exercise 1
        name_age();


    // Exercie 2
    int number_1;
    int number_2;
    cout << "Please enter two numbers: " << endl;
    cin >> number_1;
    cin >> number_2;

    int myResult = add_integers(number_1, number_2);
    cout << to_string(number_1) + " + " + to_string(number_2) + " = " + to_string(myResult) << endl;


    // Exercise 3
    // vector<double> myVector = {1.23, 4.56, 7.89, 10.12};
    vector<double> myVector;

    double myEntry;
    for(int i = 0; i < 4; i++){
        cout << "Please enter a number:\n";
        cin >> myEntry;
        myVector.push_back(myEntry); 
    }

    cout << myAverage(myVector) << endl;
}