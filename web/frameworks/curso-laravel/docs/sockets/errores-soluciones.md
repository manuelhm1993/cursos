# Solución de Errores: Instalación de Laravel Reverb y Conflictos de Dependencias

## 1. Conflicto de Dependencias en Composer (`guzzlehttp/psr7`)

### Síntoma
```text
Your requirements could not be resolved to an installable set of packages.
- laravel/reverb require guzzlehttp/psr7 ^2.6 -> found ... but the package is fixed to 3.1.0 (lock file version).
```

### Causa Técnica
El archivo `composer.lock` tenía congelada la librería `guzzlehttp/psr7` en la versión `3.1.0`. `laravel/reverb` requiere la rama `^2.6`. Como el comando interno de `install:broadcasting` ejecuta `composer update` estricto sin permitir cambios globales de versión, la instalación aborta.

### Solución
Forzar a Composer a resolver y ajustar (*downgrade/upgrade*) las dependencias secundarias bloqueadas mediante el flag `-W` (`--with-all-dependencies`):

```bash
sail composer require laravel/reverb -W
```

---

## 2. Bloqueo en Bucle por Claves `null` (`BroadcastManager`)

### Síntoma
```text
RuntimeException: Failed to create broadcaster for connection "reverb" with error: 
Pusher\Pusher::__construct(): Argument #1 ($auth_key) must be of type string, null given
```

### Causa Técnica
Al fallar el paso de Composer en la instalación automática, el framework alcanzó a escribir `BROADCAST_CONNECTION=reverb` en las configuraciones, pero **no** llegó a publicar las llaves `REVERB_APP_KEY` en el archivo `.env`. 

Al intentar ejecutar cualquier comando posterior de Artisan (incluyendo `reverb:install` o `composer dump-autoload`), Laravel bootstapea la aplicación, carga `routes/channels.php` e intenta validar el driver de broadcasting. Al leer `null` en el constructor de Pusher/Reverb, lanza una excepción fatal que impide ejecutar la propia herramienta Artisan.

### Solución (Desbloqueo en 4 Pasos)

1. **Desactivar temporalmente el driver en `.env`:**
   ```env
   BROADCAST_CONNECTION=log
   ```

2. **Ejecutar el instalador dedicado de Reverb para generar las llaves:**
   ```bash
   sail artisan reverb:install
   ```

3. **Reactivar la conexión en `.env`:**
   ```env
   BROADCAST_CONNECTION=reverb
   ```

4. **Regenerar el mapa de clases de Composer:**
   ```bash
   sail composer dump-autoload
   ```

### Instalar el scaffolding del front-end
```bash
sail npm install --save-dev laravel-echo pusher-js
```

### Exponer el puerto 8080 para el cliente laravel-echo y pusher-js
```yml
services:
    laravel.test:
        ports:
            - '${APP_PORT:-80}:80'
            - '${VITE_PORT:-5173}:${VITE_PORT:-5173}'
            - '${REVERB_SERVER_PORT:-8080}:8080'   # <-- Puerto para reverb
```

### Si se trabaja con redis se debe ejecutar el o los workers
```bash
sail artisan queue:work
```