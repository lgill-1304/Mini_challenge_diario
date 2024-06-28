#include <iostream>
#include <algorithm> // para std::sort
#include <vector>    // para std::vector (opcional)

int main() {
    // Definimos un vector de enteros desordenado
    std::vector<int> vec = {64, 25, 12, 22, 11};
    
    // Mostramos el vector original
    std::cout << "Vector original:" << std::endl;
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // Ordenamos el vector usando std::sort
    std::sort(vec.begin(), vec.end());
    
    // Mostramos el vector ordenado
    std::cout << "Vector ordenado:" << std::endl;
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}