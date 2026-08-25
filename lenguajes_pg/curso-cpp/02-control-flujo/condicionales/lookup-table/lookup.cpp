#include <iostream>
#include <unordered_map> // La librería para los diccionarios O(1)
#include <string>

using namespace std;

// 1. Declaramos la Lookup Table (diccionario)
unordered_map<string, string> codigos_http = {
    {"200", "OK - Peticion exitosa"},
    {"404", "Not Found - Recurso no encontrado"},
    {"500", "Internal Server Error - Falla en el servidor"}
};

string validateResponse(string input);

int main() {
    // Simulamos la entrada del usuario
    string input = "404";
    string resultado = validateResponse(input);

    cout << "Resultado para " << input << ": " << resultado << endl;

    // Probando el caso Default
    input = "700";
    resultado = validateResponse(input);

    cout << "Resultado para " << input << ": " << resultado << endl;

    return 0;
}

string validateResponse(string input) {
    // 2. La lógica de búsqueda con Default (El equivalente a .get() en Python)
    // Usamos .contains() exclusivo de C++20 + Operador Ternario
    string resultado = codigos_http.contains(input) ? codigos_http[input] : "Codigo desconocido (Default)";

    return resultado;
}