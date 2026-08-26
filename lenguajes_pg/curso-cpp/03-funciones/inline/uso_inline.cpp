#include <iostream>
using namespace std;

// Reemplaza la llamada por el cuerpo de la función, más eficiente, pero genera más código al compilar
inline int sumar(int a, int b);

int main() {
    int a = 5, b = 3;

    int resultado = sumar(a, b);

    cout << a << " + " << b << " = " << (a+b) << endl;

    return 0;
}

inline int sumar(int a, int b) {
    return a + b;
}