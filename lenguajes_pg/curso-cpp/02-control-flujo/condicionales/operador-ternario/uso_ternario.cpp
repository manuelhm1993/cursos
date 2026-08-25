#include <iostream>
using namespace std;

int main() {
    int numero = 0;

    cout << "Ingrese un número: "; cin >> numero;

    // Precedencia de operadores, el operador << tiene mayor prioridad que ?
    cout << "El número: " << numero << ((numero % 2 == 0) ? " es par" : " es impar") << endl;

    return 0;
}