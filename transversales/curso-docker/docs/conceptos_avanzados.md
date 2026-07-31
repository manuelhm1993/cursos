# Arquitectura de Contenedores Efímeros y Redes en Docker

**Arquitecto de Software:** Manuel Henríquez  
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
* SOLO si los contenedores están en la misma red, esto no es necesario, se apunta como dominio al nombre del contenedor

---

## 4. Comandos de Operación por Entorno

### 🟢 Node.js / Express (Ecosistema JavaScript)

```bash
# 1. Inicializar el archivo package.json
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app node:22.22.0-slim npm init -y

# 2. Instalar dependencias de producción (Express, Mongoose, dotenv)
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app node:22.22.0-slim npm install express mongoose dotenv

# 3. Ejecutar la aplicación exponiendo el puerto al exterior
docker run --rm -p 3000:3000 -v $(pwd):/app -w /app node:22.22.0-slim node index.js

### 🔴 PHP / Laravel (Ecosistema Composer)
# Crear un proyecto limpio de Laravel con Composer (Sin PHP local)
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app composer:2.8 composer create-project laravel/laravel mi_proyecto

### 🐍 Python / Django (Ecosistema Pip)
# Inicializar proyecto de Django con la versión slim de Python
docker run --rm -u $(id -u):$(id -g) -v$(pwd):/app -w /app python:3.12-slim bash -c "pip install django && django-admin startproject mi_api ."

### 4. Volúmenes fantasmas
Si no se indica un espacio para guardar la data de forma permanente a una imagen db como mongo o mysql este creará volúmenes fantasmas que se deben purgar de esta manera `docker volume prune -f`

Para evitar eso se debe usar el siguiente comando indicando el volúmen: `docker run -d --name monguito -p 27017:27017 \
  -v mongo_data:/data/db \
  -v mongo_config:/data/configdb \
  -e MONGO_INITDB_ROOT_USERNAME=mhenriquez \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  mongo:8.3`

### 5. Networking
Los contenedores pueden comunicarse con el exterior a través del mapeo de puertos, pero entre otros contenedores no, están aislados. Para evitar esto se deben agrupar en redes, ya docker por defecto tiene 3 redes incluidas:

`mhenriquez@MHenriquez:~/workspace/cursos/transversales/curso-docker/node_mongo$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
74493afc99b6   bridge    bridge    local
1c5b84ce843e   host      host      local
4e9199377be4   none      null      local
mhenriquez@MHenriquez:~/workspace/cursos/transversales/curso-docker/node_mongo$ docker network create mh_network`

### 6. Crear una imagen propia
`docker build -t <name> .`
`docker run -d --name mh_api_node_mongo --network mh_network -p 3000:3000 --env-file .env mh-api-node-mongo`