#include <iostream>
#include <random>    // Libería para generar números aleatorios
using namespace std;

int main() {
    // Si se desea definir la cantidad de elementos de un array, se puede usar una constante
    const int n_personas = 10;

    // Declaración de un array e inicialización de sus elementos
    int edades[n_personas] {15, 20, 25};

    // Acceso al primer y segundo elemento de un array
    cout << "La edad del primer usuario es: " << edades[0] << endl;

    // Sobreescribir el valor de un elemento del array con un valor ingresado por el usuario
    cout << "Ingrese la edad del segundo usuario: "; cin >> edades[1];

    cout << "La edad del segundo usuario es: " << edades[1] << endl;

    // Crear una semilla para el motor aleatorio
    random_device rd;

    // Motor de generación Mersenne Twister
    mt19937 gen(rd());

    // Definir el rango de números aleatorios
    uniform_int_distribution<> distr(3, 9);

    // Generar el número aleatorio
    int numero_aleatorio = distr(gen);

    cout << "Número aleatorio generado [3-9]: " << numero_aleatorio << endl;

    // Al no indicar un valor para los elementos restantes, estos se inicializan a 0
    cout << "Elemento no iniciado, se toma el valor por defecto: " << edades[numero_aleatorio] << endl;

    return 0;
}