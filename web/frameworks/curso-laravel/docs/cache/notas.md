# Arquitectura de Candados Atómicos (Cache::lock) en Redis

---

> Un candado atómico (atomic lock) es un mecanismo de sincronización que impide que múltiples peticiones simultáneas ejecuten un mismo bloque de código crítico al mismo tiempo, evitando condiciones de carrera (como vender más stock del disponible o duplicar cobros).

**El fundamento en Redis:** Redis procesa comandos bajo un modelo de un solo hilo (single-threaded). La operación de crear una clave condicional (SET key value NX PX 10000 -> establecer solo si No eXiste con expiración) se ejecuta a nivel de hardware de forma totalmente atómica. Si 50 usuarios hacen clic en "Comprar" en el mismo milisegundo, Redis garantiza que solo una petición logrará escribir la llave; las otras 49 rebotarán o esperarán su turno.

Anatomía de `Cache::lock($key, $seconds)->block($wait, $closure)`:

- **Identificador único ($key):** Debe ser dinámico (ej. finalizar_compra_cliente@email.com). Si usas una clave estática global, el primer comprador bloqueará las compras de todos los demás clientes del sistema.

- **Tiempo de Vida / TTL ($seconds):** Es el tiempo de auto-expiración en Redis. Si el servidor se apaga o falla a mitad de proceso, Redis eliminará la clave automáticamente al vencer los segundos configurados, liberando el recurso.

- **Tiempo de espera ($wait en block):** Especifica cuántos segundos esperará una segunda petición retenida a que la primera libere el candado antes de arrojar un LockTimeoutException.

- **Liberación de clave:** Al finalizar el $closure, Laravel ejecuta internamente un script en Lua que valida que solo la petición que creó el candado pueda borrarlo de la memoria RAM.