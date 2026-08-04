#include <iostream>
using namespace std;

int main() {
    const string nombre = "Manuel"; // Inicializador estándar & constante
    int edad {17};                  // Inicializador de lista
    double salario; 

    cout << "Ingrese el salario del empleado: "; cin >> salario;
    cout << "Ingrese la edad del empleado: "; cin >> edad;

    cout << "-------------------------------------------"
    << "\nDatos del empleado: "
    << "\n-------------------------------------------"
    << "\n- Nombre: "  << nombre // Para concatenar se usa esta sintaxis
    << "\n- Edad: "    << edad
    << "\n- Salario: " << salario << endl;

    return 0;
}