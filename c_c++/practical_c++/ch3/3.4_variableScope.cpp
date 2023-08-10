#include <iostream>


void sayHello(std::string username, int userAge){
    std::cout << "Hello, " + username + "! You are " +
    std::to_string(userAge) + " years old :P\n" << std::endl;
}


int tripleNumber(int number){
    return number * 3;;
}


void printTripleNumber(int number){
    std::cout << tripleNumber(number) << std::endl;    
}

int a;

int main(){

    int number;
    int b;
    b = 4;
    a = 2;

    sayHello("Huey", 3);
    sayHello("Dewey", 4);
    sayHello("Louie", 5);

    int result = tripleNumber(4);
    std::cout << result << std::endl;

    printTripleNumber(4);

    {
        a = 4;
        b = 5;
        int c;
    }

    c = 3;

    return 0;
}