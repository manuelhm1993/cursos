#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Permite crear un vector de 350 elementos con el mismo valor inicial para todos
    vector<double> salario_base(350, 2125.50);

    int i = 0;
    int n_salarios = salario_base.size();

    while(i < n_salarios) {
        cout << "Salario base del trabajador #" << (i + 1) << ": $" << salario_base[i] << endl;
        
        // El iterador siempre va al final
        i++;
    }

    return 0;
}