# Herramientas de Diagnóstico y Telemetría en Laravel 13 (APIs y Sockets)

| Herramienta | Entorno Ideal | Fortalezas para API y Sockets | Limitación en Tu Stack |
| :--- | :--- | :--- | :--- |
| **Laravel Debugbar** | Vistas Blade / Monolitos HTML | Muestra consultas SQL, tiempos de ejecución y uso de memoria en pantalla. | Diseñado para respuestas HTML. En llamadas API REST exige abrir su visor en `/_debugbar/open` para no alterar el JSON. |
| **Laravel Telescope** | APIs REST, WebSockets, Jobs y Colas | Panel web independiente (`/telescope`) que inspecciona cargas JSON, eventos en tiempo real, Redis y excepciones sin tocar las respuestas HTTP. | Almacena métricas de inspección en MySQL/Redis (recomendado para desarrollo o staging). |
| **Clockwork** | APIs consumidas desde cliente (SPA/Mobile) | Inyecta telemetría en las cabeceras HTTP y la muestra en las DevTools (F12) del navegador o Postman. | Requiere instalar una extensión adicional en el navegador. |
| **Laravel Pulse** | Rendimiento y telemetría de servidor | Muestra picos de CPU, RAM, consultas lentas, cuellos de botella en Redis y concurrencia de workers en tiempo real. | Enfocado en métricas globales de salud de la máquina, no en el detalle profundo de una sola petición. |

---

## Criterio de Selección y Recomendaciones Tácticas

1. **Uso de Laravel Debugbar en APIs:**
   * Si el curso lo exige, manténlo instalado para aprender a identificar patrones de consultas duplicadas ($N+1$).
   * Para evitar que la inyección de HTML corrompa las respuestas JSON en Postman, consulta sus reportes navegando a:
     ```text
     http://localhost:8005/_debugbar/open
     ```

2. **Stack Recomendado para API REST + Sockets + Redis:**
   * **Laravel Telescope:** Instálalo con `composer require laravel/telescope --dev`. Es la herramienta estándar para desarrollo de APIs, ya que audita eventos disparados por WebSockets, reintentos de Jobs en Redis y peticiones JSON en segundo plano.
   * **Laravel Pulse:** Incorpóralo cuando comiences a medir carga masiva, concurrencia de sockets o el impacto del consumo de memoria en el contenedor de Redis.

**Paquete utilizado:** `sail composer require fruitcake/laravel-debugbar --dev`