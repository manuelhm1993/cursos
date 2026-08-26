#include <iostream>
using namespace std;

// Parámetros por referencia: pasan la dirección de memoria de la variable
void reasignarValor(int &numero);

int main() {
    int numero = 10;

    cout << "Valor del número antes de llamar a la función: " << numero << endl;

    // Los parámetros por referencia afectan directamente a la variable original
    reasignarValor(numero);
    cout << "Valor del número después de llamar a la función: " << numero << endl;

    return 0;
}

void reasignarValor(int &numero) {
    numero = 50;
}