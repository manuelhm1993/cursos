#include <iostream>
using namespace std;

int main() {
    // 1. Desrefereciación de punteros nulos
    int* desrefering = nullptr;

    // Para evitar el error se comprueba si es nulo
    if(desrefering != nullptr) *desrefering = 10;

    // 2. Memory leaks
    int* memory_leak = new int[10];

    // Para evitar fugas de memoria se deben liberar los recursos antes de reasignarlos
    delete[] memory_leak;
    memory_leak = nullptr;

    // Ahora se puede reasignar sin problemas
    memory_leak = new int[20];

    // Y se vuelve a liberar
    delete[] memory_leak;
    memory_leak = nullptr;

    // 3. Desbodarmiento del buffer
    int overflow[5];

    // Tiene 5 elementos, pero va del [0-4] el 5 no está contemplado <5 no <=5
    for(int i=0;i<5;i++) {
        overflow[i] = i;
    }

    // 4. Double free
    int* double_free = new int;

    // Liberación del recurso (dos delete para el mismo recurso sin reasignación)
    delete double_free;
    double_free = nullptr;

    // Comprobar si el puntero no apunta a null
    if(double_free != 0) delete double_free;

    // 5. Punteros colgantes o dangling pointers
    int* dangling_pointer = new int[10];

    delete dangling_pointer;

    // Se debe apuntar a nulo para que el puntero no cuelgue
    dangling_pointer = nullptr;
    
    if(dangling_pointer != nullptr) *dangling_pointer = 5;

    // 6. Violación de acceso
    int numeros[5] = {0,1,2,3,4};
    int* access_violation = &numeros[5]; // La posición 5 no existe

    int valor = *access_violation;

    return 0;
}