#include <iostream>
using namespace std;

int numero = 15;

void setNumero(int *numero);

int main() {
    setNumero(&numero);

    cout << numero << endl;

    return 0;
}

void setNumero(int *numero) {
    *numero += 10;
}