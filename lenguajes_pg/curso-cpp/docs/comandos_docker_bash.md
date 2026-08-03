# Guía de uso de Docker, Bash y WSL2 para trabajar con C++ 20 y G++ 16.1.0

---

### Comando docker para crear un contenedor efímero y usar gcc 16.1.0
```bash 
docker run --rm -it -v ${PWD}:/app -w /app gcc:16.1 bash -c "g++ -std=c++20 uso_variables.cpp -o uso_variables_bin && ./uso_variables_bin"

# El comando se divide en dos partes: infraestructura (Docker) y compilación (GCC)

Parte 1: Infraestructura (El motor Docker)

El fragmento: docker run --rm -it -v ${PWD}:/app -w /app gcc:16.1

docker run: La orden maestra para instanciar un contenedor a partir de una imagen.
--rm: La directiva efímera. Le dice a Docker: "En cuanto el programa termine o falle, destruye el contenedor por completo". Cero basura en tu sistema.
-it: Es la combinación de dos flags (-i interactivo y -t TTY). El programa de C++ que escribiste tiene comandos cin >> que esperan que el usuario escriba algo. Si ejecutas Docker sin -it, el contenedor correría en el fondo, ciego y sordo, sin conectarse a tu teclado, y fallaría al llegar al cin. -it abre el túnel de comunicación directo entre tu teclado en WSL2 y la terminal interna del contenedor.
-v ${PWD}:/app: Bind Mount. Conecta tu directorio actual de Ubuntu (${PWD}) con una carpeta llamada /app dentro del contenedor. Así el contenedor puede ver tu archivo .cpp.
-w /app: Working Directory. Le dice al contenedor que, apenas nazca, se posicione directamente en la carpeta /app.
gcc:16.1: La imagen inmutable que se utilizará.

Parte 2: El Motor de Compilación y Ejecución (Bash y GCC)

El fragmento: bash -c "g++ -std=c++20 uso_variables.cpp -o uso_variables_bin && ./uso_variables_bin"

bash -c "...": Le dice al contenedor que abra una terminal bash interna y ejecute la cadena de texto exacta que está entre comillas.

g++ -std=c++20 uso_variables.cpp: Llama al compilador forzando las reglas modernas de C++20 sobre tu código fuente.
-o uso_variables_bin (Lo que preguntaste): Significa Output (Salida). En Linux, si tú compilas un archivo C++ y no le dices cómo llamarlo, el compilador lo bautizará automáticamente como a.out (Assembler Output). El flag -o te permite bautizar el binario resultante con un nombre lógico y profesional, en este caso, uso_variables_bin.
&&: El operador lógico AND. Significa: "Ejecuta el siguiente comando ÚNICAMENTE si la compilación anterior fue exitosa". Si tienes un error de sintaxis en tu C++, el proceso se detiene aquí y no intenta ejecutar basura.
./uso_variables_bin: Finalmente, ejecuta el binario recién creado dentro de la matriz de Linux.
```

--- 

### Automatización del comando en una función bash

```bash
1. Abrir el archivo de configuración de Bash en Ubuntu:
nano ~/.bashrc

2. Ir al final del archivo y crear la función:
# Compilador Efímero de C++20 y G++16.1.0 con Devolución de Permisos y Nombre Dinámico
dcpp() {
    # Extrae el nombre del archivo sin la extensión .cpp
    local filename="${1%.cpp}"
    local bin_name="${filename}_bin"
    
    # docker run --rm -it -v ${PWD}:/app -w /app gcc:16.1 bash -c "g++ -std=c++20 uso_variables.cpp -o uso_variables_bin && ./uso_variables_bin"
    docker run --rm -it -v ${PWD}:/app -w /app gcc:16.1 bash -c "g++ -std=c++20 $1 -o $bin_name && ./$bin_name && chown $(id -u):$(id -g) $bin_name"
}

3. Guardar (Ctrl+O, Enter), (Ctrl+X), Recargar la terminal:
source ~/.bashrc

4. Probar la función:
dcpp uso_variables.cpp
```