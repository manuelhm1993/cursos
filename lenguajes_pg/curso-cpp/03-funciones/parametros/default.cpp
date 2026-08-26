#include <iostream>
using namespace std;

// 1. Declaración (Prototipo): Aquí SÍ va el valor por defecto
void mostrarMensaje(string msg, int times = 1);

int main() {
    mostrarMensaje("Te amo Sugey", 3);

    return 0;
}

// 2. Definición: Aquí se OMITE el valor por defecto (= 1)
void mostrarMensaje(string msg, int times) {
    for(int i = 0; i < times; i++) {
        cout << msg << endl;
    }
}