# Trabajo en producción

---

> En producción nunca se utiliza un Seeder ni un Job programado para ejecutar el worker. El comando queue:work es un proceso demonio (daemon) de ejecución continua que debe permanecer activo las 24 horas, escuchando eventos en tiempo real.

> Si intentaras correrlo con un Seeder, bloquearías el despliegue; y si usaras un cron diario, los correos solo se procesarían una vez al día en lugar de hacerlo al instante.

**1. Servidores Tradicionales / VPS (Supervisor)**

En un servidor Linux tradicional, se utiliza un gestor de procesos del sistema operativo como Supervisor.

Supervisor vigila el comando php artisan queue:work en segundo plano. Si el proceso falla por falta de memoria, un error no controlado o el servidor se reinicia, Supervisor lo levanta automáticamente en milisegundos.

Configuración estándar (/etc/supervisor/conf.d/laravel-worker.conf):

```conf
[program:laravel-worker]
process_name=%(program_name)s_%(process_num)02d
command=php artisan queue:work redis --queue=emails,default --sleep=3 --tries=3 --max-time=3600
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
user=www-data
numprocs=2
redirect_stderr=true
stdout_logfile=/var/www/mi-app/storage/logs/worker.log
stopwaitsecs=3600
```

**2. Arquitecturas Docker / Contenedores**

En entornos de contenedores (como Sail o Kubernetes), el patrón de diseño exige un contenedor dedicado exclusivamente a procesar la cola.

Incorporas un servicio en tu compose.yaml que comparte el código de la aplicación pero cuyo punto de entrada es el worker:

```yml
queue-worker:
    build:
      context: ./vendor/laravel/sail/runtimes/8.3
      dockerfile: Dockerfile
    image: sail-8.3/app
    command: php artisan queue:work redis --queue=emails,default --tries=3
    restart: unless-stopped
    environment:
      WWWUSER: '${WWWUSER}'
      LARAVEL_SAIL: 1
    volumes:
      - '.:/var/www/html'
    networks:
      - sail
    depends_on:
      - redis
      - mysql
```

**3. El Estándar Profesional para Redis: Laravel Horizon**

Dado que estás utilizando Redis como driver de cola, la herramienta definitiva en el ecosistema de Laravel es Laravel Horizon (composer require laravel/horizon).

Panel de Control Visual: Te brinda una interfaz web en tiempo real para monitorear el rendimiento de las colas, trabajos fallidos, métricas de rendimiento y tiempos de ejecución.

Auto-Escalado: Balancea automáticamente la cantidad de workers de forma dinámica según la carga de trabajo recibida en Redis.

Comando Único: Reemplaza a queue:work ejecutando únicamente php artisan horizon gestionado por Supervisor o Docker.