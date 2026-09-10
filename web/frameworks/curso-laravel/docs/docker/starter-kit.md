# Protocolo: Creación de Proyecto Laravel + Livewire Starter Kit + Sail (Cero Contaminación)

Objetivo: Desplegar un proyecto con el Starter Kit oficial de Livewire (Volt + Flux UI), Pest y Docker (Sail) sin instalar PHP, Node ni Composer en el sistema anfitrión de WSL2.

---

## 1. Descarga Estéril del Starter Kit Oficial

Desde tu directorio de trabajo en Ubuntu/WSL2, invoca el contenedor efímero apuntando directamente al paquete del starter kit y retoma la propiedad de los archivos generados:

```bash
dexec composer:2.9.4 composer create-project laravel/livewire-starter-kit manicurista-api
sudo chown -R $USER:$USER manicurista-api
cd manicurista-api
```

---

## 2. Inyección de Infraestructura (Sail)

Genera la orquestación de Docker seleccionando MySQL y Mailpit mediante el runtime de desarrollo:

```bash
dexec mh_php:8.3-dev php artisan sail:install --with=mysql,mailpit
```

---

## 3. Blindaje de Entorno y Evasión de Puertos

### Evasión de colisiones (`.env`)
Modifica el archivo `.env` para garantizar que los contenedores no choquen con Laragon en Windows (puertos 80 y 3306) ni con otros proyectos activos:

```env
APP_PORT=8005
FORWARD_DB_PORT=33065
FORWARD_MAILPIT_PORT=1027
FORWARD_MAILPIT_DASHBOARD_PORT=8028
VITE_PORT=5175
```

### Anclaje estricto a PHP 8.3 (`docker-compose.yml`)
Abre `docker-compose.yml` y asegura la paridad con tu servidor de producción ajustando el servicio `laravel.test`:

```yaml
build:
    context: ./vendor/laravel/sail/runtimes/8.3
    dockerfile: Dockerfile
image: sail-8.3/app
```

---

## 4. Ignición del Entorno Aislado

Inicia los servicios en segundo plano:

```bash
sail up -d
```

Verifica la salud de los contenedores ejecutando `sail ps`.

---

## 5. Migraciones y Compilación de Assets

Con la infraestructura activa, corre las migraciones del starter kit e instala las dependencias de frontend utilizando las herramientas encapsuladas en Sail:

```bash
sail artisan migrate
sail npm install
sail npm run dev
```

El aplicativo estará corriendo en `http://localhost:8005` con autenticación completa, Livewire, componentes Flux UI y recarga en caliente de Vite, manteniendo tu terminal de WSL2 completamente limpia.