#include <iostream>
#include <string>
#include <map>
using namespace std;

// Función que devuelve un iterador a un elemento específico en el mapa
auto buscarEnMapa(const map<string, int> &mapa, const string &key) {
    return mapa.find(key);
}

int main() {
    string key = "Platano";

    // Creando y llenando el mapa
    map<string, int> mapa = {
        {"Manzana", 1},
        {"Platano", 2},
        {"Naranja", 3}
    };

    // Buscar elemento en el mapa
    auto it = buscarEnMapa(mapa, key);

    // Verificar si el elemento fue encontrado y mostrar su valor
    if(it != mapa.end()) {
        cout << "Encontrado '" << key << "' con el valor: " << it->second << endl;
    }
    else {
        cout << "'" << key << "' no se ha encontrado en el mapa" << endl;
    }

    return 0;
}