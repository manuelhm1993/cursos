CONTEXTO — CONVENCIONES MULTILENGUAJE (STACK GLOBAL)
Versión: 1.0 · Fecha: Agosto 2026
Objetivo: Estandarizar la nomenclatura a través de los diferentes motores del stack para mantener una arquitectura de código predecible y limpia.
═══════════════════════════════════════════════════════════════════

1. MATRIZ DE NOMENCLATURA POR LENGUAJE
───────────────────────────────────────────────────────────────────

| Elemento Arquitectónico | PHP (Laravel) | Python | Java | C++ | JavaScript / TS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Clases / Modelos** | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` |
| **Métodos / Funciones** | `camelCase()` | `snake_case()` | `camelCase()` | `snake_case()` / `camelCase()`| `camelCase()` |
| **Variables Locales** | `$camelCase` | `snake_case` | `camelCase` | `snake_case` | `camelCase` |
| **Propiedades (Clase)** | `$camelCase` | `snake_case` | `camelCase` | `m_snake_case` o `snake_case_` | `camelCase` |
| **Constantes** | `UPPER_SNAKE` | `UPPER_SNAKE` | `UPPER_SNAKE` | `UPPER_SNAKE` | `UPPER_SNAKE` |
| **Interfaces** | `NameInterface` | `Clases ABC` | `Adjetivo` o `Name` | `IName` (Prefijo I) | `IName` o `Name` |
| **Nombres de Archivo** | `PascalCase.php`| `snake_case.py`| `PascalCase.java`| `snake_case.cpp` | `kebab-case.js` |
| **Paquetes / Namespaces**| `PascalCase` | `snake_case` | `minúsculas` | `snake_case` | `kebab-case` |

═══════════════════════════════════════════════════════════════════

2. NOTAS ARQUITECTÓNICAS POR ECOSISTEMA
───────────────────────────────────────────────────────────────────

* **PHP (Laravel):** Basado estrictamente en PSR-4 y PSR-12. El `Namespace` debe coincidir con la estructura de carpetas exacta (PascalCase).
* **Python (PEP 8):** Privacidad simulada con guiones bajos (`_protegido`, `__privado`). Los módulos y paquetes son simplemente carpetas y archivos en minúsculas.
* **Java:** Las clases y los nombres de archivo deben ser **exactamente idénticos**. Los paquetes siempre van en minúsculas puras (`com.mhenriquez.facturacion`).
* **C++:** El lenguaje con menos convenciones oficiales, pero el estándar de la industria (Google C++ Style Guide o STL) prefiere `snake_case` para variables y métodos, y `PascalCase` para Tipos/Clases.
* **JavaScript:** `kebab-case` para nombres de archivos (ej. `user-profile.js`) es el estándar en frameworks modernos (React, Vue, Alpine), pero las clases internas mantienen `PascalCase`.
