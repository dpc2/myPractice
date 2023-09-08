#include <iostream>

using namespace std;

int main(){
    cout << "Hello world!" << 45 << " " << 8.2f << endl;

    // int age;
    // cout << "How old are you?\n";
    // cin >> age;
    // cout << "Your age is: " << age << endl;


    // // Read a string from the keyboard
    // char buffer[1000];
    // cout << "What would like you like to say?\n";
    // // cin >> buffer;
    // cin.getline(buffer, 1000, '\n');
    // cout << "You said: " << buffer << endl;

    // This doesn't work when your statement has spaces,
    // need to use getline()

    char buffer2[1000];
    cout << "What would like you like to say?\n";
    cin.getline(buffer2, 1000, '\n');
    cout << "You said: " << buffer2 << endl;


    return 0;
}