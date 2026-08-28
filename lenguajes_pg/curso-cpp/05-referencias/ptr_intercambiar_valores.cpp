#include <iostream>
using namespace std;

void switchValues(int *a, int *b);
void imprimirResultados(string msg, int a, int b);

int main() {
    int a = 10, b = 20;
    
    imprimirResultados("Valores originales", a, b);
    switchValues(&a, &b);
    imprimirResultados("Intercambio", a, b);

    return 0;
}

void switchValues(int *a, int *b) {
    // Intercambio de valores
    int ptr_tmp = *a;
    *a = *b;
    *b = ptr_tmp;
}

void imprimirResultados(string msg, int a, int b) {
    cout << msg << endl; 
    cout << "a = " << a << "; b = " << b << ";" << endl;
}