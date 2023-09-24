#include <iostream>

using namespace std;

// Prototypes allow you to define the functions wherever you want,
// without compilation errors

int triple_number(int number);
void print_triple_number(int number);

int main()
{
    print_triple_number(4);
    return 0;
}

void print_triple_number(int number)
{
    cout << triple_number(number) << endl;
}

int triple_number(int number)
{
    return number * 3;
}
