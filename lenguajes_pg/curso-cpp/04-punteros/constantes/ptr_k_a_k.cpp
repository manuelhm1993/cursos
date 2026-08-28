#include <iostream>
using namespace std;

int main() {
    // 3. Punteros constantes a constantes
    const int edad = 33;

    // La keyword const se usa dos veces y se inicializa inmediatamente
    const int* const ptr_edad = &edad;

    cout << *ptr_edad << endl;

    return 0;
}