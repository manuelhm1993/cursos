#include <iostream>
using namespace std;

void setValor(int* valor);

int main() {
    int numero = 5;

    cout << "Valor original: " << numero << endl;

    setValor(&numero);

    cout << "Valor modificado: " << numero << endl;

    return 0;
}

void setValor(int* valor) {
    (*valor)+=5;
}