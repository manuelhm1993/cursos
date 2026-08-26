// Instrucciones del pre-procesador: librerías y espacios de nombres
#include <iostream>
using namespace std;

// Prototipo de función: indican que la función existe y que puede ser llamada
void iniciarPrograma();
double calcularPotencia(double base, double exponente);

// Función principal e inicio del programa
int main() {
    iniciarPrograma();

    return 0;
}

// Definición de función: define la lógica de los prototipos
void iniciarPrograma() {
    double base, exponente;

    cout << "Ingrese la base de la potencia: "; cin >> base;
    cout << "Ingrese el exponente de la potencia: "; cin >> exponente;
    
    cout << base << " ^ " << exponente << " = " << calcularPotencia(base, exponente) << endl;
}

double calcularPotencia(double base, double exponente) {
    double potencia = 1;

    for(int i=0;i<exponente;i++) {
        potencia *= base;
    }

    return potencia;
}