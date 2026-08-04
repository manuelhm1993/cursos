#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> records {25, 45, 60, 35};

    // Permite reasignar valores, pero haciendo la comprobación de límites primero
    records.at(3) = 105;

    // Accede a la posición y comprueba que el límite sea correcto, si no, lanza una excepción
    cout << records.at(3) << endl;

    return 0;
}