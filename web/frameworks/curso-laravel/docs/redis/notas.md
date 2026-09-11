# Arquitectura de Estado en Laravel: Database vs. Redis (Sesiones, Colas y Caché)

Comprender el costo de persistencia del estado en PHP y la transición de base de datos relacional hacia almacenamiento en memoria RAM (Redis) para infraestructuras de alto rendimiento.

---

## 1. El Ciclo de Vida de PHP y la Necesidad de Estado

PHP opera bajo el modelo **Shared-Nothing (Stateless)**:
* Cada petición HTTP inicializa el entorno de ejecución desde cero y destruye toda la memoria RAM asignada al responder.
* Para recordar quién es un usuario autenticado, qué tareas asíncronas deben ejecutarse o qué datos ya fueron consultados, Laravel debe delegar el estado a un motor de persistencia externo mediante sus *drivers*.

---

## 2. El Peaje Oculto del Driver `database`

Usar MySQL como cuaderno de notas temporal convierte la base de datos transaccional en el cuello de botella del sistema.

| Mecanismo | Driver: `database` (El Problema) | Impacto en MySQL |
| :--- | :--- | :--- |
| **Sesiones** (`SESSION_DRIVER`) | Ejecuta un `SELECT` al inicio de cada petición para validar la cookie y un `UPDATE` al finalizar para actualizar la marca de tiempo. | **200 queries/segundo** con solo 100 usuarios activos navegando, sin haber consultado aún la lógica de negocio. |
| **Colas** (`QUEUE_CONNECTION`) | Los workers (`queue:work`) hacen *polling* ininterrumpido mediante `SELECT ... FOR UPDATE` y `UPDATE ... SKIP LOCKED`. | Desgaste continuo de I/O en disco y bloqueos de fila buscando registros en la tabla `jobs`, incluso con la cola vacía. |
| **Caché** (`CACHE_STORE`) | Guarda registros clave-valor en la tabla relacional `cache`. | **Paradoja de diseño:** Consulta el disco para evitar consultar el disco, compitiendo por el *Buffer Pool* y los bloqueos contra las ventas reales. |

---

## 3. Por Qué Redis Transforma la Arquitectura

Redis almacena estructuras de datos complejas directamente en memoria volátil (RAM), eliminando los cuellos de botella de disco relacional.

* **Latencia sub-milisegundo:** Respuestas en microsegundos (~0.1 ms frente a los 5–20 ms que toma un ciclo completo de I/O en MySQL).
* **TTL y purgado nativo:** La expiración de sesiones vencidas y cachés viejas ocurre a nivel de hardware/memoria de forma atómica; la base de datos relacional no tiene que ejecutar procesos de recolección de basura (*garbage collection*).
* **Consumo reactivo en Colas ($O(1)$):** En lugar de hacer consultas periódicas a una tabla, los workers se quedan a la espera mediante llamadas bloqueantes (`BLPOP`). Si no hay tareas pendientes, no se consume CPU ni ancho de banda; cuando entra un trabajo, se despacha instantáneamente.
* **Cache Tags:** Permite agrupar etiquetas (`Cache::tags(['productos', 'catalogo'])->put(...)`) para invalidar memorias masivamente sin barrer la base de datos completa (característica no soportada por el driver `database`).
* **Locks Atómicos Reales:** Soporte nativo para semáforos de concurrencia (`Cache::lock()`) con latencia casi nula, ideal para prevenir condiciones de carrera en pasarelas de pago y carritos de compra.

---

## 4. Desacoplamiento por Configuración (`.env`)

La mayor fortaleza de la arquitectura de Laravel es que la lógica de negocio no se acopla al motor de persistencia. La transición de bajo a alto volumen se resuelve ajustando la infraestructura en variables de entorno:

```env
# Configuración inicial / Hosting Compartido (Sin Redis disponible)
SESSION_DRIVER=database
QUEUE_CONNECTION=database
CACHE_STORE=database

# Configuración de Alto Rendimiento / Producción (VPS, Docker, Redis)
SESSION_DRIVER=redis
QUEUE_CONNECTION=redis
CACHE_STORE=redis
REDIS_CLIENT=phpredis
```

Cambiar esas variables traslada de inmediato entre el **60% y el 70% de la carga de lectura y escritura** fuera de MySQL, permitiendo que el motor relacional dedique todos sus hilos, memoria e índices exclusivamente a las transacciones críticas del negocio.