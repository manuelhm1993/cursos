#include <iostream>
using namespace std;

// Clase
class Vehiculo {
    // Propiedades de clase
    string modelo;
    string color;
    int cilindrada;
    int potencia;
    double precio;

    // Métodos de clase
    void arrancar() {
        cout << "El vehículo está arrancado." << endl;
    }

    void acelerar() {
        cout << "El vehículo está acelerando." << endl;
    }

    void frenar() {
        cout << "El vehículo está frenando." << endl;
    }

    void girar() {
        cout << "El vehículo está girando." << endl;
    }

    bool enMarcha() {
        return true;
    }
}; // Las clases en c++ terminan en ;

int main() {
    // Instancia o ejemplar de clase
    Vehiculo vehiculo_manuel, vehiculo_sugey;

    

    return 0;
}