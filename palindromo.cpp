#include <iostream>
#include <string>
#include <cctype> // Para std::tolower

bool esPalindromo(const std::string& str) {
    int left = 0;
    int right = str.length() - 1;
    
    while (left < right) {
        // Ignoramos caracteres no alfabéticos y diferenciamos mayúsculas de minúsculas
        while (left < right && !std::isalnum(str[left])) {
            ++left;
        }
        while (left < right && !std::isalnum(str[right])) {
            --right;
        }
        
        if (std::tolower(str[left]) != std::tolower(str[right])) {
            return false; // No es palíndromo
        }
        ++left;
        --right;
    }
    
    return true; // Es palíndromo
}

int main() {
    std::string input;
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, input);
    
    if (esPalindromo(input)) {
        std::cout << "\"" << input << "\" es un palíndromo." << std::endl;
    } else {
        std::cout << "\"" << input << "\" no es un palíndromo." << std::endl;
    }
    
    return 0;
}
