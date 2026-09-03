### Comandos
```bash
Para crear un proyecto con contenedores no se instala globalmente laravel, ni sus dependencias.
1. Hacer una instalación limpia de laravel sin starter-kit
- dexec composer:2.9.4 composer create-project laravel/laravel first-app
- cd first-app
2. Compilación del frontend Node 22.22.0-slim
- dexec node:22.22.0-slim npm install
- dexec node:22.22.0-slim npm run build
3. Motor de base de datos
- docker run -d --name mh_mysql_lv_app -p 33060:3306 -e MYSQL_DATABASE=first_app -e MYSQL_ROOT_PASSWORD=password mysql:8.4.3
4. Correr migraciones
- dexec php:8.3-apache php artisan migrate"
5. Exponer los puertos
- dportit 8000 php:8.3-apache php artisan serve --host=0.0.0.0 --port=8000
6. Uso de vite online
- dportit 5173 node:22.22.0-slim npm run dev -- --host 0.0.0.0
```

### Errores
```bash
1. Composer 2.9.4 está fijado en php 8.4, fijar la versión 8.3.33
- dexec composer:2.9.4 composer config platform.php 8.3.33
2. Forzar la versión 8.3 en las dependencias
- dexec composer:2.9.4 composer update
3. Ejecutar la migración nuevamente
- dexec php:8.3-apache php artisan migrate
```

### Instalación de PDO
```bash
docker run --rm -u root -v $(pwd):/var/www/html -w /var/www/html php:8.3-apache sh -c "docker-php-ext-install pdo_mysql && php artisan migrate"
docker run --rm -u root -v $(pwd):/var/www/html -w /var/www/html php:8.3-apache sh -c "docker-php-ext-install pdo_mysql && php artisan install:api"

Otra forma
Dockerfile
FROM php:8.3-apache
RUN docker-php-ext-install pdo pdo_mysql

docker build -t mh_php:8.3-dev .

dexec mh_php:8.3-dev php artisan migrate
```
### Uso de tinker
```bash
dexecit mh_php:8.3-dev env XDG_CONFIG_HOME=/tmp php artisan tinker
```
