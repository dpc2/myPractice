#include <iostream>


// This is a comment, boyyyy
// Say hello to user, with username and age
void sayHello(std::string username, int userAge){
    std::cout << "Hello, " + username + "! You are " +
    std::to_string(userAge) + " years old :P\n" << std::endl;
}


int tripleNumber(int number){
    return number * 3;;
}


// Compute triple of a given number and print
void printTripleNumber(int number){
    // This is a comment
    std::cout << tripleNumber(number) << std::endl;    
}


int main(){
    sayHello("Huey", 3); // --------
    sayHello("Dewey", 4);
    sayHello("Louie", 5);

    int result = tripleNumber(4);
    std::cout << result << std::endl;

    return 0;
}