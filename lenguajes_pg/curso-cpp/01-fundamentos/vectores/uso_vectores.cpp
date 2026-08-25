#include <iostream> 
#include <vector>   // Para poder trabajar con vectores se importa su librería
using namespace std;

int main() {
    // Clase de la librería estándar C++, equivalente a las listas
    vector<int> records(5);
    vector<char> letras {'z', 'w', 'r'}; // Especificar los elementos es opcional

    // Bucle for range, equivalente a foreach de Java
    for(int record : records) {
        // Si se declara un número de elementos, toma el valor por default de su tipo
        cout << record << endl;
    }

    int n_letras = letras.size();

    for(int i = 0; i < n_letras; i++) {
        cout << "Elemento #" << i << " - Letra: " << letras[i] << endl;
    }

    return 0;
}