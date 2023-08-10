#include <iostream>

using namespace std;

void name_age()
{
    string name, age;

    cout << "What is your name and age? ";
    cin >> name;
    cin >> age;

    cout << name + " is " + age + " years old." << endl;
}

int add_integers(int number_1, int number_2)
{
    return number_1 + number_2;
}

int main()
{
    // Exercise 1
        name_age();

    // Exercie 2
    int number_1;
    int number_2;
    cout << "Please enter two numbers: ";
    cin >> number_1;
    cin >> number_2;

    int myResult = add_integers(number_1, number_2);
    cout << to_string(number_1) + " + " + to_string(number_2) + " = " + to_string(myResult) << endl;
}