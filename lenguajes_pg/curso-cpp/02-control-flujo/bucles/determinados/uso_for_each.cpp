#include <iostream>
using namespace std;

int main() {
    string email = "manuelhm1993@gmail.com";
    bool valido = false;

    // Inferencia de tipos: determina el tipo de datos de la colección
    for(auto e: email) {
        if(e == '@') {
            valido = true;
            break;
        }
    }

    cout << ((valido) ? "El correo es válido" : "El correo no es válido") << endl;

    return 0;
}