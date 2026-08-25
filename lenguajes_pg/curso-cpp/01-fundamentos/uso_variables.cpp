#include <iostream>
using namespace std;

int main() {
    string nombre = "Manuel"; // Inicializador estándar
    int edad {17};            // Inicializador de lista
    // double salario (450);  // Inicializador de constructor
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