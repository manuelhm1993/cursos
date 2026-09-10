## Notas

> El instalador nativo de Laravel es quien empuja tu proyecto hacia PHP 8.5, no el contenedor efímero de Composer. La imagen composer:2.9.4 utiliza su propio motor interno de PHP únicamente para descargar los archivos base del framework, pero una vez que el código aterriza en tu disco, la versión operativa de tu servidor queda dictada de forma estricta por el manifiesto de Sail. 

**No necesitas buscar otra imagen de Composer**; el anclaje definitivo a la versión 8.3 para garantizar la paridad con Banahosting se realiza ajustando la configuración de la infraestructura antes del primer encendido.  

--- 

### Protocolo de Despliegue para Nuevos Proyectos

**Para instanciar cuarteles generales adicionales utilizando la caché que ya forjamos**, sin colisionar con tus ecosistemas actuales, la secuencia de ejecución es innegociable.
- **Generación Estéril:** Utiliza tu función silenciosa para descargar el código fuente ejecutando `dexec composer:2.9.4 composer create-project laravel/laravel nuevo-proyecto`.
- **Recuperación de Propiedad:** El contenedor efímero actuará como administrador supremo y secuestrará los permisos. Retoma el control de los archivos inmediatamente con `sudo chown -R $USER:$USER nuevo-proyecto`.
- **Inyección de Infraestructura:** Navega al interior del proyecto y genera el manifiesto del orquestador seleccionando MySQL mediante `dexec mh_php:8.3-dev php artisan sail:install`.
- **Anclaje de Versión:** Abre el archivo `docker-compose.yml` resultante. Laravel habrá preconfigurado `8.5`. Cambia las referencias exactas de context e image a `8.3`. Esto forzará al orquestador a utilizar la imagen sail-8.3/app que ya compilamos, saltándose la descarga y nivelando tu código con tu estándar de producción.
- **Evasión de Puertos:** Edita el archivo `.env`. Asigna puertos de salida estrictamente libres (por ejemplo, `APP_PORT=8001, FORWARD_DB_PORT=33061`) para esquivar tu instalación de Laragon en Windows y no chocar con la base de datos de tu primer proyecto Sail.  
- **Ignición Rápida:** Dispara el orquestador con sail up -d. Al tener los contenedores base en memoria, tu nuevo servidor nacerá en un par de segundos.