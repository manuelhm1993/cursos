#include <iostream>
using namespace std;

int main() {
    int opcion = 0;

    cout << "-------------- MENÚ DE OPCIONES --------------" 
    << "\n1. Mostrar mensaje"
    << "\n2. Calcular una suma"
    << "\n3. Salir del programa"
    << "\nElija una opción (1, 2 o 3): "; cin >> opcion;
    
    switch(opcion) {
        case 1:
            cout << "MHenriquez te saluda" << endl;
            break;
        case 2:
            int a, b;

            cout << "Ingrese dos números: "; cin >> a >> b;

            cout << "Resultado: " << a << " + " << b << " = " << (a + b) << endl;
            break;
        case 3:
            cout << "Fin del programa" << endl;
            break;
        default:
            cout << "Opción no contemplada" << endl;
            break;
    }

    return 0;
}