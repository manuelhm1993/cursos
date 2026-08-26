#include <iostream>
using namespace std;

// Para sobrecargar una función se debe tener secuencia, tipo o número de parámetros distintos
int sumar(int a, int b);
int sumar(int a, int b, int c);
float sumar(float a, float b);

int main() {
    cout << sumar(3, 4) << endl;       // Llama a la primera función
    cout << sumar(3, 4, 5) << endl;    // Llama a la segunda función
    cout << sumar(3.0f, 4.5f) << endl; // Llama a la tercera función

    return 0;
}

int sumar(int a, int b) {
    return a + b;
}

int sumar(int a, int b, int c) {
    return a + b + c;
}

float sumar(float a, float b) {
    return a + b;
}