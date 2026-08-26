#include <iostream>
#include <vector>
using namespace std;

void iniciarPrograma();
void doblarValores(vector<int> &numeros);
void imprimirValores(vector<int> &numeros);

int main() {
    iniciarPrograma();

    return 0;
}

void iniciarPrograma() {
    vector<int> numeros = {1,2,3,4,5};

    cout << "Valores originales: ";
    imprimirValores(numeros);

    doblarValores(numeros);

    cout << "Valores doblados: ";
    imprimirValores(numeros);
}

void imprimirValores(vector<int> &numeros) {
    for(int numero: numeros) {
        cout << numero << " ";
    }
    cout << "\n";
}

void doblarValores(vector<int> &numeros) {
    // El for range puede afectar los valores si también se usan referencias
    for(int &numero: numeros) {
        numero *= 2;
    }
}