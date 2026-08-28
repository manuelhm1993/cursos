#include <iostream>
#include <utility> // Para std::move
using namespace std;

// El uso de referencias indica que el parámetro es un L-value
void incrementarL(int &a);

// El uso de doble referencia indica que el parámetro es un R-value
void incrementarR(int &&a);

int main() {
    int numero = 15;  // numero es un L-value y 15 es un R-value
    // int tmp = numero; // tmp es un L-value y numero es un L-value evaluado como R-value

    cout << "El valor de numero es: " << numero << endl;
    
    incrementarL(numero); // Las referencias normales obligan a pasar un L-value, no un R-value
    // incrementarR(15); // Las referencias dobles obligan a pasar un R-value, no un L-value
    cout << "El valor de numero es: " << numero << endl;

    // La función move convierte un L-value en un R-value (semántica de movimiento)
    incrementarR(move(numero)); 
    
    cout << "El valor de numero es: " << numero << endl;

    return 0;
}

void incrementarL(int &a) {
    a+=5;
}

void incrementarR(int &&a) {
    a+=5;
}