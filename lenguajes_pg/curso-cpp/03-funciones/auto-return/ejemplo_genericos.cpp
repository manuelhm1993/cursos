#include <iostream>
using namespace std;

// Función de plantilla genérica para sumar dos valores
template <typename T, typename U>
auto sumar(T a, U b) {
    return a + b;
}

int main() {
    // Uso de la función con enteros
    auto sum1 = sumar(5, 3);
    cout << "Suma de enteros: " << sum1 << endl;

    // Uso de la función con un entero y un flotante
    auto sum2 = sumar(5, 2.5);
    cout << "Suma de entero y flotante: " << sum2 << endl;

    // Uso de la función con flotantes
    auto sum3 = sumar(3.0, 2.7);
    cout << "Suma de flotantes: " << sum3 << endl;

    return 0;
}