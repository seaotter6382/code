#include <iostream>  
#include <string>    

int main() {
    std::string word = "bob";
    std::string input;
    int guessing = 5;
    
    while (guessing > 0) {
        std::cout << "guess the word!\n";
        std::cin >> input;

        if (input == word) {
            std::cout << "you have guessed the word!!!\n";
            std::cout << "the word was " << word << std::endl;
            break;
        } else {
            std::cout << "you have " << guessing << " guesses left\n"; 
        }
        guessing = guessing - 1;
    }
    if (guessing == 0) {
        std::cout << "you have ran out of guesses!\n";
    }
    return 0;
}
