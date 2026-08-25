#include <iostream>
using namespace std;

int main() {
    int opcion;
    
    do {
        cout << "Menú de opciones:"
        << "\n1. Opción 1"
        << "\n2. Opción 2"
        << "\n3. Salir"; 
        
        cout << "\nEligir opción: "; cin >> opcion;

        if(opcion != 3) cout << "Haz elegido la opción: " << opcion << endl;
        
    } while(opcion != 3);

    return 0;
}