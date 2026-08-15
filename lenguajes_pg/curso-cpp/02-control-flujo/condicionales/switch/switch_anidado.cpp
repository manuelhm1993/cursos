#include <iostream>
using namespace std;

int main() {
    char idioma;    // E, I
    char categoria; // L, R, T

    cout << "---------- TIENDA ONLINE MHENRIQUEZ ----------"
    << "\nSeleccione un idioma: "
    << "\n1. Inglés"
    << "\n2. Español"
    << "\n(I-E): "; cin >> idioma;

    idioma = (char) tolower(idioma);

    switch(idioma) {
        case 'i':
            cout << "---------- CHOOSE A CATEGORY ----------"
            << "\n1. Books"
            << "\n2. Clothes"
            << "\n3. Technology"
            << "\n(B-C-T): "; cin >> categoria;

            categoria = (char) tolower(categoria);

            switch (categoria) {
                case 'b':
                    cout << "Welcome to book\'s category" << endl;
                    break;
                case 'c':
                    cout << "Welcome to clothes\'s category" << endl;
                    break;
                case 't':
                    cout << "Welcome to technology\'s category" << endl;
                    break;
                default:
                    cout << "Sorroy about that, option wasn\'t found" << endl;
                    break;
            }
            break;
        case 'e':
            cout << "---------- ESCOJA UNA CATEGORÍA ----------"
            << "\n1. Libros"
            << "\n2. Ropa"
            << "\n3. Tecnología"
            << "\n(L-R-T): "; cin >> categoria;

            categoria = (char) tolower(categoria);

            switch (categoria) {
                case 'l':
                    cout << "Bienvenido/a a la categoría libros" << endl;
                    break;
                case 'r':
                    cout << "Bienvenido/a a la categoría ropa" << endl;
                    break;
                case 't':
                    cout << "Bienvenido/a a la categoría tecnología" << endl;
                    break;
                default:
                    cout << "Disculpe, opción no encontrada" << endl;
                    break;
            }
            break;
        default:
            cout << "Opción no contemplada" << endl;
    }

    return 0;
}