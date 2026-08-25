/* Crear el juego del número mágico:
    1. El programa debe generar un número aleatorio entre 1 y 100
    2. Se debe solicitar un número con un máximo de 5 intentos para ganar
    3. Si se agotan los intentos se debe dar el resultado y preguntar si se quiere intentar otra vez s/S
    4. Se debe usar while anidado para resolverlo
*/
#include <iostream>
#include <cctype> // Para toupper()
#include <random> // Sustituye a cstdlib y ctime
using namespace std;

int main() {
    random_device rd; 
    mt19937 generador(rd()); 
    uniform_int_distribution<int> distribucion(1, 100); // Rango de 1 a 100

    char respuesta = 'S'; // Primitivo puro, no un objeto string
    int numero_secreto = distribucion(generador), intentos = 0, entrada = 0;

    // Evaluación O(1) directa y elegante
    while(toupper(respuesta) == 'S') {
        while(intentos < 5 && numero_secreto != entrada) {
            cout << "Ingrese un número [1-100]: "; cin >> entrada;
            
            intentos++;

            cout << "Intentos " << intentos << " de 5" << endl;

            if(intentos == 5 && entrada != numero_secreto) {
                cout << "Has alcanzado el límite de intentos." << " Era el número: " << numero_secreto << ". Fin del juego." << endl;
                break;
            }

            cout << (
                (entrada < numero_secreto) ? "Ingrese un número mayor." : 
                (entrada > numero_secreto) ? "Ingrese un número menor" : 
                "¡Felicidades! Adivinaste el número"
            ) << endl;
        }

        // Reiniciar las variables
        intentos = 0;
        entrada  = 0;
        numero_secreto = distribucion(generador);

        // Preguntar si desea o no seuir jugando
        cout << "¿Quieres jugar de nuevo? (s/n): "; cin >> respuesta;
    }
    
    return 0;
}