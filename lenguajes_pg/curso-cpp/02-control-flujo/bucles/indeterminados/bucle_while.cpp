#include <iostream>
using namespace std;

int main() {
    /* Crear un programa que solicite números hasta que se introduzca 0, la salida
    debe mostrar la suma de todos los números introducidos */
    int numero = 0, suma = 0;

    cout << "Ingrese un número o marque 0 para salir: "; cin >> numero;
    
    while(numero != 0) {
        suma += numero;

        cout << "Ingrese un número o marque 0 para salir: "; cin >> numero;
    }

    cout << "La suma de todos los números ingresados es: " << suma << endl;

    return 0;
}