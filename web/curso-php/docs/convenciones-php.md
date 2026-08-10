# 📐 Convenciones de Nomenclatura en PHP (PSR-4 / PSR-12 / PER-CS)

| Elemento | Convención | Ejemplo Correcto |
| :--- | :--- | :--- |
| **Archivos de Clases / Interfaces / Traits** | `PascalCase.php` (Coincidencia exacta con la estructura). | `ControladorUsuario.php`, `GestorFacturas.php` |
| **Archivos de Configuración / Rutas / Vistas** | `snake_case.php` o `kebab-case.blade.php`. | `database.php`, `api_routes.php`, `dashboard-admin.blade.php` |
| **Namespaces** | `PascalCase` (Refleja la ruta exacta de directorios). | `App\Http\Controllers`, `App\Services\Payment` |
| **Directorios de Clases (PSR-4)** | `PascalCase` (Alineado estrictamente al Namespace). | `app/Http/Controllers/`, `app/Services/` |
| **Clases** | `PascalCase` (Sustantivos singulares). | `GestorFacturas`, `Usuario` |
| **Interfaces** | `PascalCase` (Adjetivos descriptivos o sufijo `Interface`). | `Notificable`, `RepositorioUsuarioInterface` |
| **Traits** | `PascalCase` (Sufijo obligatorio `Trait`). | `RegistraErroresTrait`, `AuditableTrait` |
| **Métodos y Funciones** | `camelCase` (Verbos o frases de acción). | `calcularTotalImpuestos()`, `obtenerInfo()` |
| **Propiedades y Variables** | `camelCase` (Sustantivos descriptivos). | `$nombreUsuario`, `$totalAcumulado` |
| **Constantes** | `SCREAMING_SNAKE_CASE` (Con visibilidad explícita). | `public const MAX_INTENTOS_LOGIN = 5;` |

> **💡 Nota del Arquitecto:** A diferencia de Windows/Laragon que ignora las mayúsculas y minúsculas en el sistema de archivos, el kernel de Linux dentro de tus contenedores Docker es estrictamente **case-sensitive**. Si el nombre de tu archivo es `usuario.php` o la carpeta es `app/services/` pero tu namespace declara `App\Services\Usuario`, el autoloader de PSR-4 fallará con un `Class Not Found` catastrófico. Mantener esta matriz al 100% es tu salvavidas en producción.