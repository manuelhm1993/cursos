# Protocolo Táctico: Integración y Configuración de Redis en Laravel + Sail

Objetivo: Desplegar el motor en memoria Redis (`redis:alpine`) dentro del clúster de Sail sin tocar el sistema anfitrión, aplicando evasión de puertos y configurando los drivers de sesión, caché y colas bajo el cliente nativo `phpredis`.

---

## 1. Manifiesto de Infraestructura (`compose.yaml`)

Si tu entorno no incluía Redis desde la instalación inicial, incorpora el servicio dentro del bloque `services` en tu archivo `compose.yaml`
ejecutando el comando `sail artisan sail:add` y seleccionando redis, esto dará como resultado el siguiente cambio:

```yaml
services:
    laravel.test:
        # ... configuración existente ...
        depends_on:
            - mysql
            - mailpit
            - redis # Agregar dependencia

    redis:
        image: 'redis:alpine'
        ports:
            - '${FORWARD_REDIS_PORT:-6379}:6379'
        volumes:
            - 'sail-redis:/data'
        networks:
            - sail
        healthcheck:
            test:
                - CMD
                - redis-cli
                - ping
            retries: 3
            timeout: 5s
```

Asegura la persistencia agregando el volumen al final del archivo en la sección raíz `volumes`:

```yaml
volumes:
    sail-mysql:
        driver: local
    sail-redis:
        driver: local
```

---

## 2. Variables de Entorno y Evasión de Puertos (`.env`)

Ajusta tu archivo `.env` para enlazar el contenedor y prevenir conflictos con cualquier instancia de Redis o base de datos local en tu máquina:

```env
# Evasión de puerto hacia el host de Windows / WSL2
FORWARD_REDIS_PORT=63795

# Conexión interna de red (DNS de Sail)
REDIS_CLIENT=phpredis
REDIS_HOST=redis
REDIS_PASSWORD=null
REDIS_PORT=6379

# Migración de Drivers a memoria RAM
SESSION_DRIVER=redis
QUEUE_CONNECTION=redis
CACHE_STORE=redis
```

> **Nota de compatibilidad:** La imagen de PHP de Sail (`sail-8.3/app`) ya incluye precompilada la extensión de C **PhpRedis**. Por ende, no requieres instalar paquetes externos por Composer (como `predis/predis`).

---

## 3. Reinicio de la Infraestructura

Aplica los cambios en los contenedores reiniciando la orquestación:

```bash
./vendor/bin/sail down
./vendor/bin/sail up -d
```

Verifica que el servicio `redis` esté activo y en estado saludable:

```bash
./vendor/bin/sail ps
```

---

## 4. Verificación de Funcionamiento

### Prueba 1: Ping directo a memoria vía Tinker
Entra a la consola interactiva de Laravel:

```bash
./vendor/bin/sail artisan tinker
```

Ejecuta las siguientes operaciones atómicas:

```php
// 1. Validar conexión cruda con el socket
Illuminate\Support\Facades\Redis::ping();
// Retorna: "+PONG" o "PONG"

// 2. Probar lectura y escritura del Store de Caché
Illuminate\Support\Facades\Cache::put('conexion_test', 'ok', 60);
Illuminate\Support\Facades\Cache::get('conexion_test');
// Retorna: "ok"

exit;
```

### Prueba 2: Inspección desde el CLI nativo de Redis
Consulta directamente las claves almacenadas en la RAM del contenedor para comprobar que Laravel está prefijando y persistiendo las sesiones y llaves:

```bash
./vendor/bin/sail exec redis redis-cli keys "*"
```