#include <iostream>
using namespace std;

// Ejemplo de parámetros por defecto
void crearVentana(int ancho = 800, int alto = 600, string titulo = "MHenriquez GUI", bool completa = false);

int main() {
    // crearVentana();
    // crearVentana(350, 125);
    // crearVentana(900, 750, "Cafecitos Sugey");
    crearVentana(950, 800, "Cafecitos Sugey", true);

    return 0;
}

void crearVentana(int ancho, int alto, string titulo, bool completa) {
    cout << "Creando ventana:"
    << "\n- Título: " << titulo
    << "\n- Ancho: " << ancho << "px"
    << "\n- Alto: " << alto << "px"
    << "\n- Pantalla completa: " << ((completa) ? "si" : "no") << "\n\n";
}