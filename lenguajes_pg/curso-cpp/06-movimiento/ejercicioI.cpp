#include <iostream>
#include <utility> // Para std::move
using namespace std;

int main() {
    string msg1 = "Hola mundo";
    string msg2 = move(msg1); // Convertir msg1 en un R-value y mover el contenido a msg2

    // La expresión msg2 = msg1 equivale a ctrl-c + ctrl-v, pero move equivale a ctrl-x + ctrl-v
    cout << "El mensaje es: " << msg1 << endl;
    cout << "El mensaje es: " << msg2 << endl;

    return 0;
}