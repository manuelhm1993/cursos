#include <iostream>
using namespace std;

int factorial(int numero);
int factorialRecursiva(int numero);

int main() {
    int numero;

    cout << "Ingrese un número: "; cin >> numero;

    cout << numero << "! = " << factorial(numero) << endl;
    cout << numero << "! = " << factorialRecursiva(numero) << endl;

    return 0;
}

int factorial(int numero) {
    int resultado = 1;

    for(int i=1;i<=numero;i++) {
        resultado *= i;
    }

    return resultado;
}

int factorialRecursiva(int numero) {
    return (numero == 0) ? 1 : numero * factorialRecursiva(numero - 1);
}