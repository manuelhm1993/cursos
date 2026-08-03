# Encapsulación de Comandos (Bash Functions)
Usar el principio (DRY - Don't Repeat Yourself). Es una obligación en sistemas Linux.

En lugar de crear un archivo Python o Node para esto, usamos el lenguaje nativo del sistema operativo: **Bash**. Crear una función global en **Ubuntu (WSL2).**

```bash
# Editar el archivo de configuración de terminal.
1. Abrir el archivo maestro de la terminal de Ubuntu:
nano ~/.bashrc

2. Inyectar la función
# Ir hasta el final del archivo y crear la función:

# ===================================================================
# MHenriquez CA: Automatización de Contenedores Efímeros
# ===================================================================

# Función 1: Ejecución limpia y silenciosa (Ej: npm install, composer)
function dexec() {
    # docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app node:22.22.0-slim npm install express mongoose dotenv
    docker run --rm -u $(id -u):$(id -g) -v $(pwd):/app -w /app "$@"
}

# Función 2: Ejecución con exposición de puertos (Ej: servidor de desarrollo)
function dport() {
    # Validamos que el usuario haya enviado al menos 2 argumentos
    if [ -z "$1" ]; then
        echo "Error de Arquitectura: Falta el puerto."
        echo "Uso correcto: dport <puerto> <imagen> <comando>"
        echo "Ejemplo: dport 3000 node:22.22.0-slim node index.js"
        return 1
    fi

    local port=$1
    shift # Extrae el puerto y deja el resto de argumentos intactos

    # docker run --rm -p 3000:3000 -v $(pwd):/app -w /app node:22.22.0-slim node index.js
    docker run --rm -p $port:$port -v $(pwd):/app -w /app "$@"
}

3. Guardar y Recargar
- Ctrl + O y luego Enter para guardar.
- Ctrl + X para salir de nano.
- Recargar la terminal para que lea el nuevo comando: 
source ~/.bashrc

# El Resultado (Tu nueva vida): 
A partir de este momento, en cualquier proyecto, en cualquier carpeta de Ubuntu, los comandos kilométricos se reducen a esto:

1. Sin configuración de puertos (dexec)
# Para instalar dependencias de Node:
dexec node:22.22.0-slim npm install

# Para crear un proyecto Laravel:
dexec composer:2.8 composer create-project laravel/laravel mi_proyecto

# Para Django:
dexec python:3.12-slim bash -c "pip install django && django-admin startproject mi_api ."

2. Con configuración de puertos (dport)
# Para ejecutar Node/Express en modo desarrollo (con auto-reinicio):
dport 3000 node:22.22.0-slim node --watch index.js

# Para levantar el servidor local de Laravel (PHP 8.3):
dport 8000 php:8.3-cli php artisan serve --host=0.0.0.0 --port=8000

# Para levantar el servidor local de Django (Python 3.12):
dport 8000 python:3.14.6-slim python manage.py runserver 0.0.0.0:8000
```