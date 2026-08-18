CONTEXTO — GESTIÓN DE MEMORIA Y BASSURA (STACK GLOBAL)
Versión: 1.0 · Fecha: Agosto 2026
Objetivo: Mapa mental de Arquitecto sobre el manejo del Stack, Heap y recolección de basura entre lenguajes de alto, medio y bajo nivel.
═══════════════════════════════════════════════════════════════════

1. FUNDAMENTOS UNIVERSALES DE LA MEMORIA
───────────────────────────────────────────────────────────────────

* **El Stack (Pila):** Memoria de ejecución rápida, rígida y ordenada (LIFO). 
    * Almacena el contexto de las funciones, variables primitivas (`int`, `bool`) y los **punteros/referencias**.
    * *Ciclo de vida:* Se limpia automáticamente en milisegundos en cuanto la función termina (Sale del Scope).
* **El Heap (Montículo):** Memoria dinámica, masiva y compartida. 
    * Almacena **objetos reales** (instancias de clases, arrays dinámicos, strings largos). Todo lo que se crea con `new` o requiere espacio dinámico.
    * *Ciclo de vida:* Caótico. Sobrevive a la finalización de funciones. Requiere un mecanismo para ser limpiado, o la RAM se agotará (Memory Leak).

═══════════════════════════════════════════════════════════════════

2. C++: EL DIOS DE LA MEMORIA (MANUAL PUREZA)
───────────────────────────────────────────────────────────────────

* **Enfoque:** Control total. Poder infinito, responsabilidad absoluta.
* **El Mecanismo:** No hay Garbage Collector en segundo plano. Si creas algo en el Heap con `new`, el bloque de RAM es tuyo hasta que llames explícitamente a `delete`.
* **El Peligro:** Memory Leaks (olvidar borrar) y Dangling Pointers (borrar un bloque pero seguir intentando acceder a él).
* **Solución Nivel Senior (Modern C++):** RAII (Resource Acquisition Is Initialization) y Smart Pointers (`std::unique_ptr`, `std::shared_ptr`). Ellos destruyen automáticamente el Heap cuando la referencia en el Stack muere, simulando un GC pero con latencia cero.

═══════════════════════════════════════════════════════════════════

3. JAVA 21: EL ORQUESTADOR (AUTOMATIZACIÓN EMPRESARIAL)
───────────────────────────────────────────────────────────────────

* **Enfoque:** Delegación segura para arquitecturas masivas (10,000+ conexiones).
* **El Mecanismo:** La Máquina Virtual de Java (JVM) posee el Garbage Collector (ZGC, G1GC).
* **Cómo Opera:**
    1.  Las referencias viven en el Stack, los Objetos en el Heap.
    2.  Cuando una función muere, la referencia en el Stack se destruye.
    3.  El Objeto en el Heap queda "sin flechas apuntándole" (huérfano).
    4.  El GC, en un hilo secundario invisible, escanea la RAM (*Mark*) y destruye todo lo que no tiene referencias (*Sweep*).
* **Rendimiento moderno:** En Java 21, recolectores como ZGC limpian terabytes de basura en menos de 1 milisegundo sin pausar los hilos de tu aplicación.

═══════════════════════════════════════════════════════════════════

4. PYTHON: EL BURÓCRATA (REFERENCE COUNTING)
───────────────────────────────────────────────────────────────────

* **Enfoque:** Simplicidad extrema para el desarrollador.
* **El Mecanismo Primario:** Conteo de Referencias (*Reference Counting*).
    * Cada objeto en Python tiene un campo invisible llamado `ob_refcnt`.
    * Si una variable apunta al objeto, el contador sube (+1).
    * Si la variable muere o cambia, el contador baja (-1).
    * Cuando llega a 0, Python destruye el objeto inmediatamente.
* **El Fallo de Python (Referencias Cíclicas):** Si el Objeto A apunta al Objeto B, y el Objeto B apunta al A, sus contadores son `1`, pero ambos son inaccesibles desde el programa principal. 
* **La Red de Seguridad:** Para solucionar esto, Python tiene un "Generational Garbage Collector" secundario que se enciende de vez en cuando solo para buscar estos bucles cerrados y destruirlos, penalizando ligeramente el rendimiento general frente a Java.
