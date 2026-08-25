#include <iostream>
#include <array>
using namespace std;

int main() {
    // Array de strings
    string frases[3][5] = {
        {"Te amo Sugey", "Eres mi princesa", "Siempre te amaré", "Me encanta tu sonrisa", "Soy feliz contigo"},
        {"Desde niña me iluminas la vida", "Gracias por existir", "Te cuidaré siempre", "Eres más que suficiente", "Me haces mejor"},
        {"Solo pienso en ti", "Hasta programando pienso en ti", "Eres el python de mi vida", "Aunque seas peliona", "Te amo"}
    };

    // Determinar la longitud del array
    int x = end(frases) - begin(frases);
    int y = end(frases[0]) - begin(frases[0]);

    // Recorrer el array
    for(int i=0; i<x; i++) {
        for(int j=0; j<y; j++) {
            cout << frases[i][j] << endl;
        }
    }

    return 0;
}