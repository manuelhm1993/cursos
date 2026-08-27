#include <iostream>
using namespace std;

int main() {
    // Declarar una variable común y corriente
    int edad = 33;

    // El puntero se declara con '*' y el tipo de dato
    int *puntero_edad;

    // Luego se puede usar como una variable normal y almacena direcciones de memoria
    puntero_edad = &edad;

    // Mostrar el valor de edad
    cout << "1. Valor de la variable original: " << edad << endl;

    // Mostrar la dirección de memoria de la variable
    cout << "2. Dirección de memoria de la variable: " << puntero_edad << endl;

    // Mostrar el valor al que apunta el puntero
    cout << "3. Valor almacenado en la dirección física: " << *puntero_edad << endl;

    // Modificar el valor directamente en la memoria
    *puntero_edad = 34;

    // Mostrar la variable original después de hackearla
    cout << "4. Mostrar la variable original después del hackeo: " << edad << endl;

    return 0;
}