# Protocolo Definitivo: Laravel 13 + Livewire Starter Kit + Sail (Cero Contaminación)

Scaffolding completo con Livewire, Pest y Docker (Sail) sin dependencias globales en WSL2, permisos nativos de usuario y paridad estricta con PHP 8.3.

---

## 1. Descarga Estéril del Starter Kit Oficial (Laravel 13)

Desde tu directorio de trabajo en Ubuntu/WSL2, ejecuta la clonación efímera mapeando tu UID/GID para que los archivos nazcan a tu nombre, forzando la rama `:dev-main`[cite: 2]:

```bash
docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd):/app" -w /app composer:2.9.4 composer create-project laravel/livewire-starter-kit:dev-main manicurista-api
cd manicurista-api
```

*(Opcional - Verificación de features del installer):*
```bash
docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd):/app" -w /app mh_php:8.3-dev php artisan install:features --ansi
```
> Si responde `Command "install:features" is not defined`, confírmalo y continúa; es la firma exclusiva del CLI interactivo.

---

## 2. Inyección de Infraestructura (Sail)

Genera la orquestación seleccionando MySQL y Mailpit mediante el motor efímero[cite: 3]:

```bash
docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd):/app" -w /app mh_php:8.3-dev php artisan sail:install --with=mysql,mailpit
```

---

## 3. Blindaje de Entorno y Evasión de Puertos

### Limpieza y evasión (`.env`)
Abre `.env`. Elimina cualquier bloque residual de SQLite generado durante la creación inicial y ajusta los puertos para evitar colisiones con Laragon y otros contenedores[cite: 1, 3]:

```env
APP_PORT=8005
FORWARD_DB_PORT=33065
FORWARD_MAILPIT_PORT=1027
FORWARD_MAILPIT_DASHBOARD_PORT=8028
VITE_PORT=5175

# Validar bloque MySQL:
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=manicurista_api
DB_USERNAME=sail
DB_PASSWORD=password
```

### Anclaje estricto a PHP 8.3 (`compose.yaml`)
Abre `compose.yaml` y asegura la paridad con tu servidor de producción modificando el contexto de construcción del servicio `laravel.test`:

```yaml
build:
    context: ./vendor/laravel/sail/runtimes/8.3
    dockerfile: Dockerfile
image: sail-8.3/app
```

---

## 4. Ignición del Entorno Aislado

Inicia los contenedores en segundo plano:

```bash
./vendor/bin/sail up -d
```

*(O con tu alias de bash: `sail up -d`).*

Verifica que el stack reporte estado saludable (`healthy`/`running`):

```bash
./vendor/bin/sail ps
```

---

## 5. Migraciones y Compilación de Frontend

Con la flota activa, corre las migraciones e inicia el servidor de Vite encapsulado en Sail[cite: 1, 3]:

```bash
./vendor/bin/sail artisan migrate
./vendor/bin/sail npm install
./vendor/bin/sail npm run dev
```

La plataforma estará lista en `http://localhost:8005` con autenticación completa, Livewire reactivo, Flux UI y recarga en caliente de Vite sin haber instalado un solo paquete en tu sistema operativo base[cite: 2].