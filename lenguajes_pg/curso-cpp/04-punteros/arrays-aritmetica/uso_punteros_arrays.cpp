#include <iostream>
using namespace std;

int main() {
    // 1. Un array es un puntero que apunta al primer elemento del array
    int numeros[] = {10, 20, 30};

    // 2. El valor del nombre de un array es la dirección de memoria del primer elemento
    cout << "Números es la dirección en memoria del primer elemento: " << numeros << endl;
    cout << "Números es la dirección en memoria del primer elemento: " << &numeros[0] << endl;

    // 3. El valor del puntero es el valor del primer elemento
    cout << "Puntero numeros apunta al valor del primer elemento: " << *numeros << endl;
    cout << "Puntero numeros apunta al valor del primer elemento: " << numeros[0] << endl;

    // 4. Un puntero del mismo tipo que los valores de un array, es intercambiable casi en todas las operaciones
    int *ptr_numeros = numeros;

    cout << "Comprobación que un puntero es intercambiable con un array: " << endl;
    cout << ptr_numeros << endl;
    cout << *ptr_numeros << endl;

    return 0;
}