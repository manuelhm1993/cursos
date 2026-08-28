#include <iostream>
using namespace std;

// Se debe usar punteros porque las referencias no admiten valores nulos
void incrementarNoNulo(int*);

int main() {
    int* numero = nullptr;
    
    incrementarNoNulo(numero);

    cout << "Valor de numero: " << numero << endl;

    return 0;
}

void incrementarNoNulo(int *numero) {
    if(numero != nullptr) (*numero)++;
}