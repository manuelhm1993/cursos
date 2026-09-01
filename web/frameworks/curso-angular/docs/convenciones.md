# CONTEXTO — CONVENCIONES MULTILENGUAJE (STACK GLOBAL)
**Versión:** 1.0 · **Fecha:** Agosto 2026[cite: 9]
**Objetivo:** Estandarizar la nomenclatura a través de los diferentes motores del stack para mantener una arquitectura de código predecible y limpia[cite: 9].

## 1. MATRIZ DE NOMENCLATURA POR LENGUAJE
| Elemento Arquitectónico | PHP (Laravel) | Python | Java | C++ | JavaScript / TS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Clases / Modelos** | `PascalCase`[cite: 9] | `PascalCase`[cite: 9] | `PascalCase`[cite: 9] | `PascalCase`[cite: 9] | `PascalCase`[cite: 9] |
| **Métodos / Funciones** | `camelCase()`[cite: 9] | `snake_case()`[cite: 9] | `camelCase()`[cite: 9] | `snake_case()` / `camelCase()`[cite: 9]| `camelCase()`[cite: 9] |
| **Variables Locales** | `$camelCase`[cite: 9] | `snake_case`[cite: 9] | `camelCase`[cite: 9] | `snake_case`[cite: 9] | `camelCase`[cite: 9] |
| **Propiedades (Clase)** | `$camelCase`[cite: 9] | `snake_case`[cite: 9] | `camelCase`[cite: 9] | `m_snake_case` o `snake_case_`[cite: 9] | `camelCase`[cite: 9] |
| **Constantes** | `UPPER_SNAKE`[cite: 9] | `UPPER_SNAKE`[cite: 9] | `UPPER_SNAKE`[cite: 9] | `UPPER_SNAKE`[cite: 9] | `UPPER_SNAKE`[cite: 9] |
| **Interfaces** | `NameInterface`[cite: 9] | `Clases ABC`[cite: 9] | `Adjetivo` o `Name`[cite: 9] | `IName` (Prefijo I)[cite: 9] | `IName` o `Name`[cite: 9] |
| **Nombres de Archivo** | `PascalCase.php`[cite: 9]| `snake_case.py`[cite: 9]| `PascalCase.java`[cite: 9]| `snake_case.cpp`[cite: 9] | `kebab-case.js`[cite: 9] |
| **Paquetes / Namespaces**| `PascalCase`[cite: 9] | `snake_case`[cite: 9] | `minúsculas`[cite: 9] | `snake_case`[cite: 9] | `kebab-case`[cite: 9] |

## 2. NOTAS ARQUITECTÓNICAS POR ECOSISTEMA
* **PHP (Laravel):** Basado estrictamente en PSR-4 y PSR-12[cite: 9]. El `Namespace` debe coincidir con la estructura de carpetas exacta (PascalCase)[cite: 9].
* **Python (PEP 8):** Privacidad simulada con guiones bajos (`_protegido`, `__privado`)[cite: 9]. Los módulos y paquetes son simplemente carpetas y archivos en minúsculas[cite: 9].
* **Java:** Las clases y los nombres de archivo deben ser **exactamente idénticos**[cite: 9]. Los paquetes siempre van en minúsculas puras (`com.mhenriquez.facturacion`)[cite: 9].
* **C++:** El lenguaje con menos convenciones oficiales, pero el estándar de la industria (Google C++ Style Guide o STL) prefiere `snake_case` para variables y métodos, y `PascalCase` para Tipos/Clases[cite: 9].
* **JavaScript:** `kebab-case` para nombres de archivos (ej. `user-profile.js`) es el estándar en frameworks modernos (React, Vue, Alpine), pero las clases internas mantienen `PascalCase`[cite: 9].

---

# CONTEXTO — GESTIÓN DE MEMORIA Y BASURA (STACK GLOBAL)
**Versión:** 1.0 · **Fecha:** Agosto 2026[cite: 9]
**Objetivo:** Mapa mental de Arquitecto sobre el manejo del Stack, Heap y recolección de basura entre lenguajes de alto, medio y bajo nivel[cite: 9].

## 1. FUNDAMENTOS UNIVERSALES DE LA MEMORIA
* **El Stack (Pila):** Memoria de ejecución rápida, rígida y ordenada (LIFO)[cite: 9]. 
    * Almacena el contexto de las funciones, variables primitivas (`int`, `bool`) y los **punteros/referencias**[cite: 9].
    * *Ciclo de vida:* Se limpia automáticamente en milisegundos en cuanto la función termina (Sale del Scope)[cite: 9].
* **El Heap (Montículo):** Memoria dinámica, masiva y compartida[cite: 9]. 
    * Almacena **objetos reales** (instancias de clases, arrays dinámicos, strings largos)[cite: 9]. Todo lo que se crea con `new` o requiere espacio dinámico[cite: 9].
    * *Ciclo de vida:* Caótico[cite: 9]. Sobrevive a la finalización de funciones[cite: 9]. Requiere un mecanismo para ser limpiado, o la RAM se agotará (Memory Leak)[cite: 9].

## 2. C++: EL DIOS DE LA MEMORIA (MANUAL PUREZA)
* **Enfoque:** Control total[cite: 9]. Poder infinito, responsabilidad absoluta[cite: 9].
* **El Mecanismo:** No hay Garbage Collector en segundo plano[cite: 9]. Si creas algo en el Heap con `new`, el bloque de RAM es tuyo hasta que llames explícitamente a `delete`[cite: 9].
* **El Peligro:** Memory Leaks (olvidar borrar) y Dangling Pointers (borrar un bloque pero seguir intentando acceder a él)[cite: 9].
* **Solución Nivel Senior (Modern C++):** RAII (Resource Acquisition Is Initialization) y Smart Pointers (`std::unique_ptr`, `std::shared_ptr`)[cite: 9]. Ellos destruyen automáticamente el Heap cuando la referencia en el Stack muere, simulando un GC pero con latencia cero[cite: 9].

## 3. JAVA 21: EL ORQUESTADOR (AUTOMATIZACIÓN EMPRESARIAL)
* **Enfoque:** Delegación segura para arquitecturas masivas (10,000+ conexiones)[cite: 9].
* **El Mecanismo:** La Máquina Virtual de Java (JVM) posee el Garbage Collector (ZGC, G1GC)[cite: 9].
* **Cómo Opera:**
    1.  Las referencias viven en el Stack, los Objetos en el Heap[cite: 9].
    2.  Cuando una función muere, la referencia en el Stack se destruye[cite: 9].
    3.  El Objeto en el Heap queda "sin flechas apuntándole" (huérfano)[cite: 9].
    4.  El GC, en un hilo secundario invisible, escanea la RAM (*Mark*) y destruye todo lo que no tiene referencias (*Sweep*)[cite: 9].
* **Rendimiento moderno:** En Java 21, recolectores como ZGC limpian terabytes de basura en menos de 1 milisegundo sin pausar los hilos de tu aplicación[cite: 9].

## 4. PYTHON: EL BURÓCRATA (REFERENCE COUNTING)
* **Enfoque:** Simplicidad extrema para el desarrollador[cite: 9].
* **El Mecanismo Primario:** Conteo de Referencias (*Reference Counting*)[cite: 9].
    * Cada objeto en Python tiene un campo invisible llamado `ob_refcnt`[cite: 9].
    * Si una variable apunta al objeto, el contador sube (+1)[cite: 9].
    * Si la variable muere o cambia, el contador baja (-1)[cite: 9].
    * Cuando llega a 0, Python destruye el objeto inmediatamente[cite: 9].
* **El Fallo de Python (Referencias Cíclicas):** Si el Objeto A apunta al Objeto B, y el Objeto B apunta al A, sus contadores son `1`, pero ambos son inaccesibles desde el programa principal[cite: 9]. 
* **La Red de Seguridad:** Para solucionar esto, Python tiene un "Generational Garbage Collector" secundario que se enciende de vez en cuando solo para buscar estos bucles cerrados y destruirlos, penalizando ligeramente el rendimiento general frente a Java[cite: 9].