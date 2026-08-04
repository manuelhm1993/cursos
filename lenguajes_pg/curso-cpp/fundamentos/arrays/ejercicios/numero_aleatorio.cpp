#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    // Inicializa la semilla
    srand(time(0));

    int trafico_vehiculos[24][31][12];

    // Calcular las dimensiones del array en tiempo de ejecución
    int horas = sizeof(trafico_vehiculos) / sizeof(trafico_vehiculos[0]);
    int dias  = sizeof(trafico_vehiculos[0]) / sizeof(trafico_vehiculos[0][0]);
    int meses = sizeof(trafico_vehiculos[0][0]) / sizeof(trafico_vehiculos[0][0][0]);

    // Recorrer el array con 3 bucles anidados
    for(int i = 0; i < horas; i++) {
        for(int j = 0; j < dias; j++) {
            for(int k = 0; k < meses; k++) {
                // Validar que febrero solo llene 28 dias
                if(k == 1 and j > 27) {
                    continue;
                }

                // Validar que febrero, abril, junio, septiembre y noviembre llenen 30 días
                if((k == 1 || k == 3 || k == 5 || k == 8 || k == 10) and j > 29) {
                    continue;
                }

                trafico_vehiculos[i][j][k] = rand() % 1001; // Número aleatorio entre 0-1000
            }
        }
    }

    cout << "Cantidad de vehículos del día " << trafico_vehiculos[0][30][1] << endl;

    return 0;
}