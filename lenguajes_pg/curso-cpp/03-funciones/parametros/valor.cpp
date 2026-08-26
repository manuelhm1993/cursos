#include <iostream>
using namespace std;

// Parámetros por valor: copia del valor pasado
void reasignarValor(int numero);

int main() {
    int numero = 10;

    cout << "Valor del número antes de llamar a la función: " << numero << endl;

    // Los parámetros por valor no afectan a la variabe original porque operan sobre una copia
    reasignarValor(numero);
    cout << "Valor del número después de llamar a la función: " << numero << endl;

    return 0;
}

void reasignarValor(int numero) {
    numero = 50;
}