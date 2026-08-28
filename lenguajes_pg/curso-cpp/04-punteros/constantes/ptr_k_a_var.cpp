#include <iostream>
using namespace std;

int main() {
    // 2. Punteros constantes a variables
    int edad = 33;

    // La keyword const va luego del tipo de dato y se inicializa inmediatamente
    int* const ptr_edad = &edad;

    // Permite modificar el valor de la variable a la que se apunta, pero no su dirección
    *ptr_edad = 34;

    cout << *ptr_edad << endl;

    return 0;
}