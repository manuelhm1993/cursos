#include <iostream>
using namespace std;

int main() {
    int numeros[] = {33, 23, 4};
    int *ptr_numeros = numeros;

    int n_items = sizeof(numeros) / sizeof(numeros[0]);

    for(int i=0;i<n_items;i++) {
        // Imprimir el valor de la posición actual del puntero y avanzar su posición
        cout << *(ptr_numeros++) << endl;
    }

    // Liberar recursos (si no se usó new, no hay que liberar el heap)
    ptr_numeros = nullptr;

    return 0;
}