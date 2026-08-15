#include <iostream>
using namespace std;

int main() {
    /**
     * Se le da beca al estudiante si: 
     * - Su calificación es superior a 8 ó si la distancia del domicilio al 
     * centro es superior a 20km y los ingresos familiares son inferiores a $5000
     */
    double calificacion = 0;
    double distancia    = 0;
    double presupuesto  = 0;

    cout << "-------------- PROGRAMA DE MHENRIQUEZ BECAS 2026 --------------" << endl;
    cout << "Ingrese la calificación del alumno: "; cin >> calificacion;
    cout << "Ingrese la distancia en km del domicilio del alumno: "; cin >> distancia;
    cout << "Ingrese el presupuesto familiar anual: "; cin >> presupuesto;

    if(calificacion > 16 || (distancia > 20 && presupuesto < 5000)) {
        cout << "Felicidades, eres candidato a beca" << endl;
    }
    else {
        cout << "No cumples con los requisitos" << endl;
    }

    return 0;
}