/**
 * Proceso de compilación:
 * 1. Preprocesado: ver todas las directivas e instrucciones que se incluyen para
 * importar librerías. Trae las librerías y genera un fichero que incluye todo el código 
 * de las librerías.
 * 2. Compilación: generar las instrucciones de ensamblado que dependen de la arquitectura
 * de la máquina donde se ejecuta la compilación.
 * 3. Ensamblado: transformar las instrucciones de ensamblado del paso 2 a código binario
 * 4. Enlazado: fusionar todos los archivos que se generaron en pasos anteriores en un
 * archivo ejecutable que finalmente será leído, interpretado y ejecutado por la máquina.
 */

#include <iostream>  // Directiva: instrucción que permite añadir contenido de bibliotecas externas a nuestro programa
using namespace std; // Sentencias | Declaraciones (terminan en ';'): especifica que se usará el espacio de nombres std 

int main() { // Función: agrupa bloques de código, pueden o no retornar un valor, esta es la función principal donde se ejecuta el programa
    cout << "Hola mundo" << endl;

    return 0;
}