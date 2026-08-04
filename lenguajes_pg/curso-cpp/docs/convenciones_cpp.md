# Convenciones de Nomenclatura en C++ (Estándar Moderno / Google C++ Style)

| Elemento | Convención Principal | Ejemplo | Regla / Nota |
| :--- | :--- | :--- | :--- |
| **Clases / Structs / Enums** | `PascalCase` | `class NetworkManager;` | Sustantivos. La primera letra de cada palabra en mayúscula. |
| **Variables Locales / Objetos**| `snake_case` | `int connection_timeout;` | Todo en minúsculas separadas por guion bajo (Estándar de la STL). |
| **Variables Miembro (Clases)** | `snake_case_` | `int player_health_;` | Terminan con guion bajo para diferenciarlas de variables locales. |
| **Funciones / Métodos** | `camelCase` (o `PascalCase`) | `void sendMessage();` | Verbos. La STL usa `snake_case`, pero en proyectos empresariales impera `camelCase` o `PascalCase` (Google). |
| **Constantes / `constexpr`** | `kPascalCase` | `const int kMaxRetries = 3;` | Prefijo `k` seguido de PascalCase (Google Style). |
| **Macros / Enums (Legacy)** | `UPPER_SNAKE_CASE`| `#define LOG_ERROR` | Todo mayúsculas. Usa `constexpr` o `enum class` en su lugar en C++ moderno. |
| **Namespaces (Paquetes)** | `snake_case` | `namespace data_models {}` | Minúsculas, nombres cortos. C++ no tiene "paquetes" como Java; usa namespaces. |
| **Archivos (.cpp / .h)** | `snake_case` | `network_manager.cpp` | Fundamental: Todo en minúsculas. Previene bugs críticos al mover código de Windows a Linux (case-sensitive). |
| **Carpetas / Directorios** | `snake_case` o `kebab-case` | `src/network_utils/` | Todo en minúsculas. |
