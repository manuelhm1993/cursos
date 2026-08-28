#include <iostream>
using namespace std;

int main() {
    /* Los punteros se deben inicializar inmediatamente por buena práctica o se 
    iguala a nulo para evitar que almacene valores residuales de la memoria. Al 
    ser declarado como una variable, se almacena en el stack 
    */
    int *int_ptr = nullptr;

    /* El operador new asigna un espacio en la memoria del heap y el puntero apunta
    *int_ptr está en el stack apuntando a un espacio reservado para int en el heap
    */
    int_ptr = new int;

    // Almacenar un valor en el heap
    *int_ptr = 33;

    // Imprimir la dirección en memoria en el heap asignada con new int
    cout << "Dirección de memoria del heap: " << int_ptr << endl;

    // Imprimir la dirección en memoria en el stack del puntero
    cout << "Dirección de memoria del stack: " << &int_ptr << endl;

    // Imprimir el valor dentro del heap al que apunta el puntero
    cout << "Valor al que apunta el puntero: " << *int_ptr << endl;

    // Liberar los recursos de la memoria heap (en lenguajes de más alto nivel lo gestiona el garbage collector)
    delete int_ptr;

    // A pesar que el heap fue liberado, el puntero contiene esa dirección (puntero colgante)
    cout << "Dirección de memoria del heap: " << int_ptr << endl;

    // Asignar el puntero a nulo
    int_ptr = nullptr;

    cout << "Memoria liberada del heap: " << int_ptr << endl;
    cout << "Memoria liberada del stack: " << &int_ptr << endl;

    return 0;
}