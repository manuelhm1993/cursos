# Arquitectura de Contenedores Efímeros y Redes en Docker

**Arquitecto de Software:** Manuel Henriquez  
**Organización:** MHenriquez CA  
**Área:** Infraestructura, WSL2 y Docker Base  
**Propósito:** Manual táctico de comandos efímeros, gestión de permisos UNIX y resolución de dominios en red.

---

## 1. El Paradigma del Contenedor Efímero (`--rm`)

Un **contenedor efímero** es una instancia de ejecución temporal. Nace con un propósito único (como instalar dependencias, compilar binarios o inicializar un proyecto), sincroniza los archivos generados con tu sistema anfitrión (WSL2/Linux) a través de un volumen de enlace (*Bind Mount*), y se autodestruye de inmediato al concluir el comando.

### Ventajas de Infraestructura:
* **Sistema Base Inmaculado:** No requiere instalar Node.js, Composer, Python o herramientas globales en WSL2 ni en Windows.
* **Cero Contenedores Zombis:** Elimina automáticamente el contenedor al finalizar, evitando acumular espacio muerto en la tabla `docker ps -a`.
* **Persistencia Directa:** Los archivos y dependencias generadas quedan almacenados en tu directorio local con los permisos de tu usuario UNIX.

---

## 2. Leyenda Táctica de Banderas (Flags)

| Bandera / Flag | Explicación Técnica y Función |
| :--- | :--- |
| `--rm` | **Auto-destrucción:** Ordena a Docker eliminar el contenedor y su sistema de archivos temporal apenas finaliza la ejecución del proceso principal. |
| `-u $(id -u):$(id -g)` | **Mapeo de Permisos UNIX:** Asigna al proceso interno del contenedor el UID (*User ID*) y GID (*Group ID*) del usuario actual de Linux. Evita que los archivos creados (como `node_modules` o `package.json`) queden bloqueados como propiedad de `root`. |
| `-v $(pwd):/app` | **Bind Mount (Portal de Datos):** Conecta de forma bidireccional el directorio actual (`$(pwd)`) con la ruta `/app` interna del contenedor. Todo lo descargado o creado en `/app` persiste en tu disco. |
| `-w /app` | **Directorio de Trabajo (*Workdir*):** Establece el punto de aterrizaje interno. Todas las instrucciones (`npm`, `composer`, `pip`) se ejecutarán posicionadas dentro de `/app`. |
| `-p 3000:3000` | **Redireccionamiento de Puertos (`Host:Container`):** Abre un túnel de comunicación mapeando el puerto `3000` de tu máquina física al puerto `3000` donde la app escucha internamente. |

---

## 3. Regla Fundamental de Red: `localhost` vs `host.docker.internal`

En arquitectura de contenedores, el contexto de red cambia según la **perspectiva del emisor**:

[ Navegador Web Windows ]  ---> http://localhost:3000 ---> [ Túnel Docker -p 3000:3000 ]
                                                                   |
                                                                   v
[ Contenedor Node.js ] ----(host.docker.internal:27017)---> [ Puerto 27017 Anfitrión / Mongo ]

* **`localhost` (Perspectiva del Anfitrión):** Tu máquina física (Windows/WSL2). Desde tu navegador en Windows, accedes a `http://localhost:3000` para entrar al contenedor de Node.
* **`localhost` (Perspectiva del Contenedor):** Bucle cerrado interno de la caja aislada. Si Node intenta conectar a Mongo en `localhost:27017`, buscará a Mongo dentro de su propio contenedor y colapsará.
* **`host.docker.internal`:** Nombre de dominio DNS especial proporcionado por el motor de Docker. Le permite al contenedor de Node salir de su aislamiento y conectarse a servicios que escuchan en los puertos de la máquina anfitriona (como el contenedor de MongoDB con `-p 27017:27017`).
* **SOLO si los contenedores están en la misma red**, esto no es necesario, se apunta como dominio al nombre del contenedor

---

## 4. Comandos de Operación por Entorno

```bash
🟢 Node.js / Express (Ecosistema JavaScript)

1. Inicializar el archivo package.json
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app node:22.22.0-slim npm init -y

2. Instalar dependencias de producción (Express, Mongoose, dotenv)
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app node:22.22.0-slim npm install express mongoose dotenv

3. Ejecutar la aplicación exponiendo el puerto al exterior
docker run --rm -p 3000:3000 -v $(pwd):/app -w /app node:22.22.0-slim node index.js

🟣 PHP / Laravel (Ecosistema Composer)
# Crear un proyecto limpio de Laravel con Composer (Sin PHP local)
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app composer:2.8 composer create-project laravel/laravel mi_proyecto

🐍 Python / Django (Ecosistema Pip)
# Inicializar proyecto de Django con la versión slim de Python
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app python:3.14.6-slim bash -c "pip install django && django-admin startproject mi_api ."
```

### 4. Volúmenes fantasmas
Si no se indica un espacio para guardar la data de forma permanente a una imagen db como mongo o mysql este creará volúmenes fantasmas que se deben purgar de esta manera `docker volume prune -f`

Para evitar eso se debe usar el siguiente comando indicando el volúmen: 
```bash
docker run -d --name <nombre_contenedor> -p <puerto>:<puerto> \
  -v mongo_data:/data/db \
  -v mongo_config:/data/configdb \
  -e MONGO_INITDB_ROOT_USERNAME=<usuario> \
  -e MONGO_INITDB_ROOT_PASSWORD=<contraseña> \
  mongo:8.3
```

### 5. Networking
Los contenedores pueden comunicarse con el exterior a través del mapeo de puertos, pero entre otros contenedores no, están aislados. Para evitar esto se deben agrupar en redes, ya docker por defecto tiene 3 redes incluidas:

```bash
# Listar las redes docker
docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
74493afc99b6   bridge    bridge    local
1c5b84ce843e   host      host      local
4e9199377be4   none      null      local

# Crear una red propia
docker network create <nombre_red>
```

### 6. Crear una imagen propia
```bash
1. Se debe crear un archivo con nombre Dockerfile donde se automatizará la creación de la imagen
# Dockerfile

# Toda imagen se debe basar en otra imagen
FROM <nombre_imagen>

# Directorio de trabajo, es el /home de linux, pero dentro del contenedor
WORKDIR /app

# Los archivos que se van a copiar desde el anfitrión al contenedor
COPY package*.json ./

# Se ejecutan las dependencias primero para optimizar la compilación
RUN npm install

# Se repite el proceso de copiado para el código fuente
COPY . .

# Se expone un puerto para la comunicación con el exterior
EXPOSE 3000

# Se indica el comando de inicio de la app
CMD ["node", "index.js"]

2. Se compila la imagen
# Se crea la imagen con su etiqueta nombre:1
docker build -t <name>:<v1.0.0> .

3. Se crea un contenedor en base a la imagen previamente creada
docker run -d --name <nombre_contenedor> --network <nombre_red> -p 3000:3000 --env-file .env <nombre_imagen>

4. Para poder ver los cambios en tiempo real (La config se optimiza con .gitignore y .dockerignore para que el RUN ejecute la instalación de dependencias)
docker rm -f <nombre_contenedor>
docker run -d --name <nombre_contenedor> --network <nombre_red> -p 3000:3000 -v $(pwd):/app --env-file .env <nombre_imagen> node --watch index.js
```

### Consideraciones del punto 6
**En producción NUNCA** se usa el Bind Mount **(-v $(pwd):/app)** para inyectar código fuente. Eso es un riesgo de seguridad masivo y rompe la inmutabilidad.

En producción **se destruye y se vuelve a crear.** El flujo es este:

```bash
1. Terminar una nueva función (como un endpoint delete).
2. Compilar una nueva versión de la imagen: 
  2.1. docker build -t <nombre_imagen:n+1> .
3. Destruir el contenedor viejo en el servidor: 
  3.1. docker rm -f <nombre_contenedor>
4. Levantar nuevamente: docker run -d --name <nombre_contenedor> --network <nombre_red> -p 3000:3000 --env-file .env <nombre_imagen:n+1>
```

### 6. Infraestructura como Código (IaC)
Para evitar escribir cada comando por cada contenedor, variables de entorno y además redes, existe el docker-compose.yml. Esta herramienta poderosa lee el Dockerfile, permite automatizar todo el proceso de forma declarativa y colocar las imagenes, contenedores y dependencias paso a paso, él lee y ejecuta:
```bash
1. Crear el archivo: docker-compose.yml
# MHenriquez CA - Infraestructura como Código (IaC)
services:
  # Contenedor de db
  <nombre_dominio_contenedor>:
    image: <imagen:version>
    container_name: <nombre_contenedor>
    restart: always
    ports:
      - "<host:container>"
    # Interpolamos desde el .env local. No queda expuesto en GitHub.
    environment:
      - <MONGO_INITDB_ROOT_USERNAME>=${DB_USER}
      - <MONGO_INITDB_ROOT_PASSWORD>=${DB_PASSWORD}
    volumes:
      - <nombre_volumen>:/data/db
      - <nombre_volumen>:/data/configdb
  
  # Contenedor compilando una imagen propia de una app
  <nombre_dominio_contenedor>:
    build: .
    container_name: <nombre_contenedor>
    restart: always
    ports:
      - "<host:container>"
    depends_on:
      - <contenedor_del_que_depende>
    # Le inyectamos el archivo completo internamente
    env_file:
      - .env
# Al final del archivo, declaramos que los discos duros deben existir
volumes:
  mongo_data:
  mongo_config:

2. Ejecutar el comando: docker-compose up -d --build

3. Comandos de uso docker-compose:
- docker-compose logs -f: Ver los logs (¿Qué está pasando adentro?)
- docker-compose stop: Apagar todo al final del día (Sin destruir datos)
- docker-compose down: Destruir toda la infraestructura (Para limpiar la computadora)
```