# HOJA DE RUTA — DEVOPS: WSL2 Y DOCKER EN WINDOWS 11
Versión: 1.0 · Objetivo: Transición de entorno local (Laragon) a contenedores aislados.

## FASE 1: Fundamentos de Infraestructura (WSL2 y Linux)
- [x] Entender qué es el Subsistema de Windows para Linux (WSL2) y por qué supera a una Máquina Virtual tradicional.
- [x] Instalación de WSL2 y Ubuntu 24.04 en Windows 11.
- [x] Comandos básicos de terminal Linux (Bash): navegación, permisos (`chmod`, `chown`), y gestión de paquetes (`apt`).
- [x] Integración del sistema de archivos: Cómo acceder a tus proyectos de Windows (`C:\Users\manue\devs`) desde Linux y viceversa.
- [x] Configuración de VS Code para WSL (Extensión WSL Remote).

## FASE 2: Motor de Contenedores (Docker Base)
- [x] Teoría: Diferencia entre una Imagen y un Contenedor.
- [x] Instalación de Docker Desktop en Windows 11 (configurado para usar el backend de WSL2, no Hyper-V).
- [x] Descargar imagen nginx: `docker pull nginx:alpine`, `docker images`.
- [x] Crear y mapear un contenedor: `docker run -d -p 8080:80 --name primer_contenedor_nginx nginx:alpine`.
- [x] Listar los contenedores corriendo: `docker ps`.
- [x] Verificar que el servidor corre correctamente: `http://localhost:8080/`.
- [x] Detener el contenedor: `docker stop primer_contenedor_nginx`.
- [x] Destruir el contenedor: `docker rm primer_contenedor_nginx`.
- [x] Comprobar contenedores prendidos y apagados: `docker ps -a`.
- [x] Comandos core de Docker CLI: `docker pull`, `docker run`, `docker ps`, `docker stop`, `docker rm`.
- [x] Gestión de volúmenes: Cómo persistir datos para que no se borren al destruir el contenedor (vital para bases de datos).
- [x] Crear un volúmen: `docker volume create web_devs`.
- [x] Crear un contenedor mapeando el volúmen a nginx: `docker run -d -p 8080:80 -v web_devs:/usr/share/nginx/html --name server1 nginx:alpine`.
- [x] Inyectar un archivo de afuera hacia adentro: `docker exec server1 sh -c 'echo "<h1>Los datos persistentes sobrevivieron. Tarea completada.</h1>" > /usr/share/nginx/html/index.html'`.

## FASE 3: Dockerización del Proyecto (Python)
- [x] Escribir tu primer `Dockerfile` desde cero para un bot de que consulta el precio del bitcoin y lo actualiza cada 10 segundos.
- [x] Selección de imágenes base óptimas (`python:3.12-slim` vs `alpine`).
- [x] Capas de Docker: Entender la caché de construcción (por qué copiar `requirements.txt` y hacer `pip install` antes de copiar el código fuente).
- [x] Construir (`docker build`) y ejecutar (`docker run`) tu propia imagen.
- [x] Construir la imagen: `docker build -t bot_extractor:v1 .`.
- [x] Encender el bot en segundo plano: `docker run -d --name mh_bot_info_bitcoin bot_extractor:v1`.
- [x] Monitorear los logs: `docker logs -f mh_bot_info_bitcoin`.

## Bug: Errno -2 Name or service not known
- [x] Error de DNS: `windows no inyecta correctamente en ocasiones los DNS`.
- [x] Apagar y destruir el contenedor dañado: `docker stop mh_bot_info_bitcoin && docker rm mh_bot_info_bitcoin`.
- [x] Levantarlo de nuevo inyectando los DNS: `docker run -d --dns 8.8.8.8 --name mh_bot_info_bitcoin bot_extractor:v1`.
- [x] Verificar los logs: `docker logs -f mh_bot_info_bitcoin`.


## FASE 4: Orquestación (Docker Compose)
- [x] Introducción a `docker-compose.yml`: Infraestructura como Código (IaC).
- [x] Borrar los contenedores anteriores y levantar el compose: `docker-compose up -d --build`
- [x] Levantar múltiples servicios simultáneos.
- [x] Ejercicio final: Conectar un contenedor de Python con un contenedor de Base de Datos aislado en la misma red de Docker.
- [x] Regla de Arquitectura: Aislar Laragon (puertos 80/3306) para que no colisione con los contenedores Docker.