/*Ejercicios propuestos:
1. Cuenta Regresiva (Tipo void): Recibe un número $N$. Imprime el número y se llama a sí misma restando 1. Cuando llegue a 0, imprime "¡Despegue!" y termina.
2. Suma de Dígitos (Retorna int): Recibe un número entero (ej. 123) y suma sus dígitos recursivamente ($1 + 2 + 3 = 6$). Pista: Usa módulo % 10 y división / 10.
3. Inversión de Texto (Tipo void): Recibe un std::string y un índice. Imprime el string al revés carácter por carácter de forma recursiva sin usar bucles.
4. Potencia (Retorna int): Recibe una base y un exponente (ej. $2^3$). Calcula el resultado multiplicando la base por sí misma de forma recursiva.
5. Fibonacci (Retorna int): El clásico letal. Recibe una posición $N$ y devuelve el número de la sucesión de Fibonacci en esa posición (donde $f(n) = f(n-1) + f(n-2)$).
*/
#include <iostream>
using namespace std;

void cuentaRegresiva(int numero); // Listo
int sumaDigitos(int numero); // Listo
void inversionTexto(string texto, int indice); // Listo
int potencia(int base, int exponente); // Listo
int fibonacci(int numero); // Listo

int main() {
    int numero = 0, base = 12, exponente = 0;
    int n_digitos = 123, indice = 0;
    string texto = "Manuel";

    cuentaRegresiva(numero);
    cout << base << "^" << exponente << " = " << potencia(base, exponente) << endl;
    cout << "La suma de los dígitos individuales de " << n_digitos << " es: " << sumaDigitos(n_digitos) << endl;
    inversionTexto(texto, indice); cout << "\n";
    cout << "El fibonacci de " << numero << " es: " << fibonacci(numero) << endl;

    return 0;
}

void cuentaRegresiva(int numero) {
    if(numero <= 0) {
        cout << "¡Despegue!" << endl;
    }
    else {
        cout << numero << " ";
        cuentaRegresiva(numero - 1);
    }
}

int sumaDigitos(int numero) {
    // Caso base
    if(numero == 0) {
        return 0;
    }
    
    // Caso recursivo
    return (numero % 10) + sumaDigitos(numero / 10);
}

void inversionTexto(string texto, int indice) {
    if(indice == texto.length()) return;
    else {
        inversionTexto(texto, indice + 1);
        cout << texto[indice];
    }
}

int potencia(int base, int exponente) {
    return (exponente == 0) ? 1 : base * potencia(base, exponente - 1);
}

int fibonacci(int numero) {
    return (numero <= 2) ? 1 : fibonacci(numero - 1) + fibonacci(numero - 2); 
}