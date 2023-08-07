
#include <iostream>


void say_hello(std::string username, int userAge){
    std::cout << "Hello, " + username + "! You are " +
    std::to_string(userAge) + " years old :P\n" << std::endl;
}


int main(){
    say_hello("Huey", 3);
    say_hello("Dewey", 4);
    say_hello("Louie", 5);
    return 0;
}