#include <iostream>
using namespace std;

int main() {
    int edad = 0;

    cout << "Ingrese su edad: "; cin >> edad;

    if(edad < 18) {
        cout << "No tienes la edad suficiente para sacar la lincencia" << endl;
    }
    else {
        cout << "Tienes la edad suficiente para sacar la licencia" << endl; 
    }

    return 0;
}