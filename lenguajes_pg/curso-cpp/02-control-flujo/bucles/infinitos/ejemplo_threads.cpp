#include <iostream>
#include <random> // Sustituye a cstdlib y ctime
#include <thread>
#include <chrono>

using namespace std;

// Inyección limpia: Solo traemos las herramientas exactas
using std::this_thread::sleep_for;
using std::chrono::seconds;

// Prototipos
double leerTemperatura();
void esperarSegundos(int segundos);

int main() {
    const double kLimiteTemperatura = 35.0;

    for(;;) {
        double temp_actual = leerTemperatura();

        cout << "Temperatura actual: " << temp_actual << "°C" << endl;

        if(temp_actual > kLimiteTemperatura) {
            cout << "¡ALERTA! Temperatura elevada detectada: " << temp_actual << "°C" << endl;
        }

        esperarSegundos(3);
    }

    return 0;
}

double leerTemperatura() {
    // La palabra 'static' es la magia aquí. 
    // Obliga a que la semilla y el motor se creen UNA SOLA VEZ en la memoria RAM,
    // sobreviviendo entre múltiples llamadas a la función.
    static random_device rd; 
    static mt19937 generador(rd()); 
    uniform_real_distribution<double> distribucion(20.0, 40.0); // Rango aleatorio

    return distribucion(generador);
}

void esperarSegundos(int segundos) {
    sleep_for(seconds(segundos));
}