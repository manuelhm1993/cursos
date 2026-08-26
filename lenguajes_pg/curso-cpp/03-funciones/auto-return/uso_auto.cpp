#include <iostream>
using namespace std;

// Igual que la inferencia de tipos en variables, se deduce el tipo por el compilador
auto sumar(int a, int b) -> int;

int main() {
    int x = 5, y = 3, resultado;

    resultado = sumar(x, y);

    cout << x << " + " << y << " = " << resultado << endl;

    return 0;
}

auto sumar(int a, int b) -> int {
    return a + b;
}