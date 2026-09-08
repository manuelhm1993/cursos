# Protocolo Universal: Dockerizado de Proyectos PHP/Laravel

- **Aislamiento del Código:** Ubícate en tu directorio de trabajo nativo en Linux (WSL2) y genera el proyecto inyectando la imagen efímera de Composer.
- **Recuperación de Propiedad:** El contenedor opera inicialmente como root; retoma el control de los permisos en tu terminal inmediatamente antes de avanzar.
- **Inyección del Orquestador:** Instala Laravel Sail y selecciona MySQL para mantener la paridad estricta con tu stack de bases de datos.
- **Evasión de Puertos:** Modifica el archivo .env configurando puertos alternativos (ej. APP_PORT=8080 y FORWARD_DB_PORT=33060) para no colisionar físicamente con los servicios 80 y 3306 de tu instalación de Laragon.  
- **Compilación Aislada:** No utilices la instalación de Node de tu anfitrión. Ejecuta cualquier dependencia de frontend a través del orquestador (sail npm install y sail npm run dev) para garantizar el aislamiento por prefijos.

---

### Operación Táctica: Enlace Propiedades

Para tu plataforma inmobiliaria, el objetivo es replicar el entorno exacto de producción (PHP 8.3, Laravel 13, Livewire 4, Tailwind v4, MySQL) dentro de un ecosistema de contenedores.
- **Clonación Nativa:** Clona el repositorio directamente en el sistema de archivos ext4 de Ubuntu para garantizar la máxima velocidad de lectura del motor de Docker, alejándote del disco de Windows.
- **Instalación de Dependencias:** Utiliza tu comando automatizado dexec composer:2.9.4 install para poblar el directorio vendor/ sin depender de instalaciones globales.
- **Alineación Arquitectónica:** Configura las credenciales en tu .env, asegurando que DB_HOST apunte al DNS interno mysql y definiendo puertos de evasión exclusivos para este monolito.
- **Levantamiento:** Ejecuta sail up -d --build para encender y orquestar la infraestructura.
- **Compilación de Assets:** Ejecuta sail npm install seguido de sail npm run build para compilar los recursos de Tailwind v4 y Livewire directamente dentro del contenedor web.

--- 

### Protocolo de Despliegue (Banahosting)
Tu servicio de hosting compartido Deluxe no ejecuta Docker; la orquestación construida es una herramienta exclusiva para tu entorno local.
- **Preparación de la Carga:** El servidor alojará únicamente el código compilado. Archivos de infraestructura como docker-compose.yml o el entorno local .env no deben subirse.
- **Sincronización de Assets:** Dado que el servidor carece de Node.js, es imperativo compilar los recursos en local para que el directorio public/build/ quede versionado en tu rama master antes del push.
- **Despliegue Automatizado:** El webhook interceptará el push a master y sincronizará los directorios funcionales (app/, public/, config/, vendor/) en Banahosting.
- **Enrutamiento de Seguridad:** El Document Root en cPanel debe apuntar exactamente a la carpeta public/ del proyecto, manteniendo el núcleo de la aplicación protegido un nivel arriba del acceso a internet.