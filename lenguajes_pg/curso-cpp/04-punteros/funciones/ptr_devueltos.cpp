#include <iostream>
using namespace std;

// Definición de la clases
class Vehiculo {
    // Se usa la sintaxis 2 puntos para los modificadores de acceso
    private:
        string modelo_;
    
    // Método constructor
    public:
        Vehiculo(string modelo): modelo_(modelo) {}

    // Métodos accesores
    public:
        // La palabra const indica que el método es de solo lectura
        string getModelo() const {
            return modelo_;
        }

}; // Terminan en ;

// Prototipos de funciones
//
// Crea un nuevo Vehiculo y devuelve un puntero a él
Vehiculo* crearVehiculo(string modelo);

int main() {
    // Crear Vehiculo llamando a la función crearVehiculo
    Vehiculo* vehiculo = crearVehiculo("Mazda MX5");

    // Los métodos se acceden con el operador flecha estilo php (*vehiculo).getModelo()
    cout << "El modelo del vehículo es: " << vehiculo->getModelo() << endl;

    // Liberar la memoria (siempre que se usa new, al finalizar se usa delete)
    delete vehiculo;
    vehiculo = nullptr;

    return 0;
}

// Definición de funciones
Vehiculo* crearVehiculo(string modelo) {
    // Instanciar la clase dentro de un puntero
    Vehiculo *nuevoVehiculo = new Vehiculo(modelo);

    // Devolver el puntero
    return nuevoVehiculo;
}