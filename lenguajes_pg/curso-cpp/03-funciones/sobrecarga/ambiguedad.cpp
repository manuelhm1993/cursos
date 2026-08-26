#include <iostream>
using namespace std;

// Ambigüedad al usar sobrecarga y parámetros por defecto, se recomienda una u otra
void mostrar(int a = 10);
void mostrar(int a, double b = 20.5);

int main() {
    // ¿A cuál se llama si ambos son por defecto?
    mostrar();

    return 0;
}

void mostrar(int a) {
    cout << "Función con parámetro int: " << a << endl;
}

void mostrar(int a, double b) {
    cout << "Función con parámetro double: " << b << endl;
}