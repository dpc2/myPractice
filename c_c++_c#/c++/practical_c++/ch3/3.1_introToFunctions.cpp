#include <iostream>


void say_hello(){
    std::cout << "Hello" << std::endl;
    std::cout << "World\n" << std::endl;
}


int main(){
    say_hello();
    say_hello();
    say_hello();
    return 0;
}