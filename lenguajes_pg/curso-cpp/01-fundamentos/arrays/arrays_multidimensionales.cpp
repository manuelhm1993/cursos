#include <iostream>
using namespace std;

int main() {
    // Horas, días y meses - 15-05 3:00 am
    int trafico_vehiculos[24][31][12] = {
        {
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { 15 } // trafico_vehiculos[0][14][0] = día 15
        },
        {
            { 0, 0, 0, 0, 5 } // trafico_vehiculos[1][0][4] = mayo
        },
        {
            { 2 } // trafico_vehiculos[2][0][0] = 2 de la mañana
        }
    };

    // Asignación a una posición específica un valor
    trafico_vehiculos[2][14][4] = 4;

    // Muestra o rescate de la información
    cout << "Cantidad de vehículos el 15-05 2:00h = " << trafico_vehiculos[2][14][4] << endl;

    return 0;
}