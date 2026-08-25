#include <iostream>
using namespace std;

int main() {
    /*
    // Declaración e inicialización de un array bidimensional
    int matriz[4][5] = {
        {15, 25, 8, -7, 92},
        {77, 12, 11, 7, 44},
        {56, 59, 43, 78, 12},
        {43, 95, 12, 87, 33}
    };

    // Acceder a los elementos del array bidimensional
    cout << "Elemento [0][2]: " << matriz[0][2] << endl;
    */

    // Declaración de un array bidimensional sin inicializar
    int matriz[4][5];

    // Calcular las dimensiones del array para el bucle for
    int filas    = sizeof(matriz) / sizeof(matriz[0]);       // end(matriz) - begin(matriz);
    int columnas = sizeof(matriz[0]) / sizeof(matriz[0][0]); // end(matriz[0]) - begin(matriz[0]);
    
    cout << "Rellenando el array de elementos" << endl;

    // Bucle for para recorrer posiciones e inicializarlas
    for(int i = 0; i < filas; i++) {
        for(int j = 0; j < columnas; j++) {
            cout << "Ingrese el valor del elemento [" << i << "][" << j << "]: "; cin >> matriz[i][j];
        }
    }

    cout << "\nMostrando los elementos del array" << endl;
    
    for(int i = 0; i < filas; i++) {
        cout << "Valores de la fila [" << i << "]: ";
        for(int j = 0; j < columnas; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}