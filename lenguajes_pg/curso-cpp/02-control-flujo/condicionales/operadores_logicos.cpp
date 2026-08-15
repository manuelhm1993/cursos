#include <iostream>
using namespace std;

// Prototipo de la función
void toLowerCase(string &cadena);

int main() {
    int edad = 0;
    string ex_medico = "";

    cout << "Ingrese su edad: "; cin >> edad;
    cout << "¿Aprobaste el exámente médico?: (Si/No) "; cin >> ex_medico;

    toLowerCase(ex_medico);

    if(edad >= 18 && ex_medico == "si") {
        cout << "Puedes obtener el carnet de conducir" << endl; 
    }
    else {
        cout << "No cumples los requisitos" << endl;
    }

    return 0;
}

// Definición de la función
void toLowerCase(string &cadena) {
    int caracteres = cadena.length();

    // Convertir caracter a caracter en minúsculas el string
    for(int i = 0; i < caracteres; i++) {
        cadena[i] = (char) tolower(cadena[i]);
    }
}