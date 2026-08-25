#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Imaginar que estos datos vienen de una db
    vector<double> precios = {
        50, 120, 75, 300, 90, 200,
    };

    // Aplicar un 15% de descuento a los precios superiores a 100
    int n_items = precios.size();
    const double descuento = 0.15;

    for(int i=0; i<n_items; i++) {
        // Dejar plano el código
        if(precios.at(i) <= 100) {
            continue;
        }

        // En caso de ser mayor a 100 se aplica el descuento
        precios.at(i) -= precios.at(i) * descuento;
    }

    for(int i=0; i<n_items; i++) {
        cout << "Precio final del producto #" << (i + 1) << ": $" << precios.at(i) << endl;
    }

    return 0;
}