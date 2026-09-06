# ARQUITECTURA: PROTOTIPOS VS. SISTEMAS EN PRODUCCIÓN (LARAVEL)

**Objetivo:** Establecer la frontera técnica entre un proyecto personal y un ecosistema real utilizando Servicios, Proveedores y Caché.

## 1. MATRIZ COMPARATIVA

| Criterio Arquitectónico | Proyecto Personal (Prototipo) | Sistema Real (Producción) |
| :--- | :--- | :--- |
| **1. Delegación a Servicios** | Creas una clase genérica y la inyectas directamente. Laravel usa *Auto-Wiring* para resolverla mágicamente en la RAM. | Los servicios orquestan lógica de negocio pesada. Se aplican interfaces para cumplir el Principio de Inversión de Dependencias (DIP). |
| **2. Registro en `ServiceProvider`** | Rara vez se toca. Todo se inyecta de forma concreta porque la aplicación es pequeña y no requiere inicialización previa. | Obligatorio cuando el servicio requiere credenciales, debe ser un Singleton, o cuando enlazas una abstracción con su implementación concreta. |
| **3. Datos Globales (Navbar)** | Consultas las categorías desde el controlador (`Category::all()`) y las pasas manualmente a la vista en cada método. | Se utilizan **View Composers** registrados en un `ServiceProvider` para inyectar la variable automáticamente solo en el layout que la necesita. |
| **4. Impacto en Base de Datos** | Cada vez que el usuario navega a otra vista, el servidor ejecuta un `SELECT` golpeando físicamente el motor de base de datos. | Se implementa Caché. La consulta se ejecuta una sola vez y el resultado se guarda utilizando el driver `database`. |

---

## 2. IMPLEMENTACIÓN TÁCTICA (CÓDIGO)

### Caso 1 y 2: Servicios y Registro en Provider (DIP)
En producción, no inyectas la clase concreta en el controlador, inyectas un contrato (Interfaz). Luego, le dices a Laravel en el `AppServiceProvider` qué clase debe entregar cuando alguien pida ese contrato.

**1. El Contrato y el Servicio (`app/Services/`)**
```php
namespace App\Services\Contracts;

interface CompraServiceInterface {
    public function procesar(array $datos): void;
}

namespace App\Services;

class CompraServicio implements CompraServiceInterface {
    public function procesar(array $datos): void {
        // Lógica compleja de negocio
    }
}
```

**2. El Registro (`app/Providers/AppServiceProvider.php`)**
```php
public function register(): void
{
    // Enlazamos la interfaz con la clase física
    $this->app->bind(
        \App\Services\Contracts\CompraServiceInterface::class,
        \App\Services\CompraServicio::class
    );
}
```

### Caso 3 y 4: View Composers y Caché (Navbar Dinámico)
Para que tu Navbar tenga las categorías siempre disponibles sin destruir el rendimiento de la base de datos, interceptas la vista del layout e inyectas los datos cacheados. 

**En `app/Providers/AppServiceProvider.php` (Método `boot`)**
```php
use Illuminate\Support\Facades\View;
use Illuminate\Support\Facades\Cache;
use App\Models\Category;

public function boot(): void
{
    // Solo cuando Laravel ensamble 'layouts.public', ejecutará esta función
    View::composer('layouts.public', function ($view) {
        
        // Retenemos la consulta en caché por 24 horas usando el driver 'database'
        $categorias = Cache::remember('navbar_categories', 86400, function () {
            return Category::where('is_active', true)->get();
        });

        $view->with('categorias', $categorias);
    });
}
```