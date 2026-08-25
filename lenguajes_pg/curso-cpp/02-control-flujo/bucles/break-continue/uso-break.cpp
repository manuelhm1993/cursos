#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Imaginar que estos datos vienen de una db
    vector<string> nombres = {
        "Manuel", "Sugey", "Ender", 
        "Fernando", "Carlos", "Génesis"
    };

    // Comprobar si Fernando está en los registros
    string persona_buscada = "Fernando";
    int i = 0;

    for(string nombre: nombres) {
        if(nombre.compare(persona_buscada) == 0) {
            cout << "Persona encontrada. Nombre: " << persona_buscada << " en la posición " << i << endl;
            break;
        }

        i++;
    }

    cout << i << endl;

    return 0;
}