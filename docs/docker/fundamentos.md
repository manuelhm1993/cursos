# Manual de Infraestructura: WSL2 y Docker
**Arquitecto:** Manuel Henriquez
**Objetivo:** Aislamiento de procesos y despliegue profesional.

## FASE 1: Fundamentos de Linux y WSL2
El Subsistema de Windows para Linux (WSL2) ancla un kernel de Linux real a Windows, permitiendo rendimiento nativo sin los cuellos de botella de una Máquina Virtual pesada.
* **Sistema de Archivos:** WSL vive en `ext4`. Los proyectos deben alojarse en `/home/usuario/` (Linux) para máxima velocidad, no en `/mnt/c/` (Windows).
* **Permisos (chmod):** Controlan el nivel de acceso (Lectura `r`=4, Escritura `w`=2, Ejecución `x`=1). 
  * Estructura: `drwxrwxrwx` (Directorio | Usuario | Grupo | Otros).
  * Ejemplo: `chmod 755 archivo` otorga control total al dueño, y lectura/ejecución al resto.
* **Propiedad (chown):** Define quién es el dueño del archivo (`chown usuario:grupo archivo`).

## FASE 2: Motor de Contenedores (Docker Base)
El fin de la era "en mi máquina sí funciona".
* **Imagen:** Es un molde estático, de solo lectura, que contiene el SO, el código y las dependencias (Ej: `nginx:alpine`).
* **Contenedor:** Es la imagen cobrando vida. Un proceso aislado ejecutándose en el kernel de Linux. Es efímero y desechable.
* **Volúmenes (`-v`):** La solución a la volatilidad. Son discos virtuales blindados que se inyectan en el contenedor. Si el contenedor se destruye, los datos sobreviven.
* **Comandos Core:**
  * `docker pull [imagen]`: Descarga el molde.
  * `docker run -d -p 80:80 --name [nombre] [imagen]`: Crea, enciende y mapea puertos en segundo plano.
  * `docker exec [contenedor] [comando]`: Entra a un contenedor vivo a ejecutar una orden (ej: `sh -c`).
  * `docker ps` / `stop` / `rm` / `rmi`: Ciclo de vida y destrucción.

## FASE 3: Dockerización (El `Dockerfile`)
El arte de crear imágenes propias encapsulando código Python.
* **Aislamiento Total:** El contenedor reemplaza al `.venv` local. El sistema base se mantiene limpio.
* **Estrategia de Caché (Capas):** Docker construye de arriba hacia abajo.
  1. Se copia **primero** el `requirements.txt`.
  2. Se ejecuta `RUN pip install`.
  3. Se copia el código fuente al final (`COPY . .`).
  * *Razón:* Si el código fuente cambia, Docker usa la memoria caché para las librerías, reduciendo el tiempo de compilación de minutos a milisegundos.

## FASE 4: Orquestación e IaC (Docker Compose)
Infraestructura como Código. Reemplaza los comandos kilométricos de terminal por un manifiesto declarativo (`docker-compose.yml`).
* Permite definir servicios, redes virtuales compartidas y políticas de reinicio automático (`restart: always`).
* **Comando Maestro:** `docker-compose up -d --build` (Construye la imagen si es necesario, crea la red, mapea volúmenes y levanta los servicios en segundo plano).
* **Destrucción:** `docker-compose down` (Apaga y limpia la red virtual).