#include <iostream>
using namespace std;

int main() {
    int a = 3;
    float b = 4.0f;

    // Permite crear una variable de tipo dinámico estilo Python, pero se debe iniciar inmediatamente
    auto resultado = a + b;

    // Muesta la inicial del tipo de dato
    cout << typeid(resultado).name() << endl;

    return 0;
}