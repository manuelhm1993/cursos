#include <iostream>
using namespace std;

int main() {
    // 1. Punteros a constantes
    const int kEdad = 10;
    const int kSalario = 450;
    const int *ptr_kEdad = &kEdad;

    // No se puede modificar la constante
    cout << *ptr_kEdad << endl;

    // Pero el puntero si puede apuntar a otra dirección
    ptr_kEdad = &kSalario;

    cout << *ptr_kEdad << endl;

    return 0;
}