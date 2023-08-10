#include <iostream>

using namespace std;

namespace abc {
    int tripleNumber(int number){
        return number * 3;;
    }

    void cout(){}
};


void sayHello(std::string username, int userAge){
    cout << "Hello, " + username + "! You are " +
    to_string(userAge) + " years old :P\n" << endl;

    abc::cout();
}



void printTripleNumber(int number){
    cout << abc::tripleNumber(number) << endl;    
}


int main(){
    sayHello("Huey", 3); // --------
    sayHello("Dewey", 4);
    sayHello("Louie", 5);

    int result = abc::tripleNumber(4);
    cout << result << endl;

    return 0;
}