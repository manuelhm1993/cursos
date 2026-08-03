# Nombre del Proyecto
---

Este proyecto sigue la arquitectura base de MHenriquez CA.

## 1. Stack Tecnológico

Aquí detallaremos las tecnologías.

### Backend

Aquí irán los detalles de PHP y Laravel.

## 2. Metodología
---

Aquí irán las reglas de los Sprints.

### Formato de Texto

El stack base exige **PHP 8.3** y *Laravel 13*. Recuerda que el archivo `.env` de producción siempre se sube vía FTP, nunca por terminal ni versionado.

### Checklists de Issues (Sprint 1)

- [x] Definir el stack y arquitectura permanente.
- [x] Crear el documento de metodología.
- [x] Configurar el entorno en WSL2.
- [x] Bautizar los volúmenes anónimos en Docker.

### Reglas de Desarrollo

1. Un paso a la vez.
2. Esperar confirmación antes de continuar.
3. No mezclar create/edit en un mismo paso.

### Recursos y Documentación

Toda la base de conocimiento técnica se encuentra en la organización oficial de [GitHub MHenriquez CA](https://github.com/MHenriquezCA). 

### Stack Principal

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Laravel](https://img.shields.io/badge/laravel-%23FF2D20.svg?style=for-the-badge&logo=laravel&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2306B6D4.svg?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white)

> **Nota:** Puedes usar la sintaxis de "Blockquote" (cita) poniendo un signo de mayor que `>` al inicio de la línea para resaltar notas o advertencias importantes, como esta.

### Configuración del Servidor

Para purgar los fantasmas de Docker según nuestra metodología, ejecuta:

```bash
docker compose down -v
docker volume prune -f
```

El array de base de datos en Laravel debe quedar estrictamente así:

```php
<?php
return [
    'connections' => [
        'mysql' => [
            'driver' => 'mysql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'database' => env('DB_DATABASE', 'forge'),
        ],
    ],
];
```

### Variables de Entorno (Producción)

| Variable | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `APP_ENV` | String | Sí | Define el entorno (`local`, `production`). |
| `DB_CONNECTION` | String | Sí | Motor de BD (ej. `mysql`, `sqlite`). |
| `FILESYSTEM_DISK` | String | No | Disco para uploads (`public` en tu stack). |