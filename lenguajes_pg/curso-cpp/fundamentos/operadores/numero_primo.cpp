#include <iostream>
using namespace std;

int main() {
    // Crear un programa C++ que permita determinar si un número ingresado por teclado es primo o no
    int numero    = 0;
    bool es_primo = true;

    cout << "Ingrese un número mayor a 0: "; cin >> numero;

    // Validar errores
    if(numero <= 0) {
        cout << "El número " << numero << " no se puede comprobar en este cálculo" << endl;
    }
    else {
        // Luego de la mitad del número todas las divisiones son inexáctas
        for(int i = 2; i <= (numero / 2); i++) {
            if((numero % i) == 0) {
                es_primo = false;
                break;
            }
        }

        // Comprobación de resultados
        if(numero == 1 || numero == 2 || es_primo) {
            cout << "El número " << numero << " es primo" << endl;
        }
        else {
            cout << "El número " << numero << " no es primo" << endl;
        }
    }

    return 0;
}