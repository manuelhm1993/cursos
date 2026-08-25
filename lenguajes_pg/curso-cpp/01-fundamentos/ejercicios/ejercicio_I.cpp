/**
 * Ejercicio práctico 1:
 * Simulación de un sistema contratista para remodelación de pisos
 * 1. ¿Cuántos metros quieres instalar con calidad media?
 * 2. ¿Cuántos metros quieres instalar con calidad alta?
 * 3. Precio mt calidad media = $ 35.5
 * 4. Precio mt calidad alta = $ 55.3
 * 5. IVA 21%
 * 6. Días de validez del presupuesto = 30
 */
#include <iostream>
using namespace std;

int main() {
    // Constantes
    const int kDiasValidez{30};
    const double kIva{0.21};
    const double kMetroCalidadMedia{35.5};
    const double kMetroCalidadAlta {55.3};

    // Variables
    int metros_media_instalar{0};
    int metros_alta_instalar{0};

    cout << "---------------------------------------------" << endl;
    cout << "Contratista MHenriquez C.A." << endl;
    cout << "---------------------------------------------" << endl;

    cout << "Ingrese la cantidad de mt^2 en calidad media: "; cin >> metros_media_instalar;
    cout << "Ingrese la cantidad de mt^2 en calidad alta: "; cin >> metros_alta_instalar;

    // Cálculos matemáticos
    double total_calidad_media = metros_media_instalar * kMetroCalidadMedia;
    double total_calidad_alta  = metros_alta_instalar * kMetroCalidadAlta;
    double total_importe = total_calidad_media + total_calidad_alta;

    cout << "---------------------------------------------" << endl;
    cout << "Presupuesto 26 de Julio de 2026" << endl;
    cout << "---------------------------------------------" << endl;
    cout 
    << "- Metros calidad media: " << metros_media_instalar
    << "\n- Metros calidad alta: " << metros_alta_instalar
    << "\n- Precio calidad media: $" << kMetroCalidadMedia
    << "\n- Precio calidad alta: $" << kMetroCalidadAlta
    << "\n- IMPORTE: $" << total_importe
    << "\n- IVA: $" << total_importe * kIva
    << "\n- Tiempo de validez: " << kDiasValidez << " días.";

    return 0;
}