# Arquitectura WebSockets para Actualización de Stock en Tiempo Real

## 1. Instalación de Broadcasting (Laravel Reverb)
Ejecutar el instalador nativo de Laravel para habilitar Reverb, actualizar variables de entorno e instalar las librerías cliente (`laravel-echo` y `pusher-js`):

```bash
sail artisan install:broadcasting

sail artisan reverb:start
```

> Si algo falla ver ./errores-soluciones.md

---

## 2. Evento Transmisible (`app/Events/StockActualizado.php`)
Definición del evento con transmisión inmediata (`ShouldBroadcastNow`) a través del canal público `productos`:

```php
<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Broadcasting\ShouldBroadcastNow;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class StockActualizado implements ShouldBroadcastNow
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public function __construct(
        public int $productId,
        public int $nuevoStock
    ) {}

    /**
     * Canal público por donde viajará la notificación.
     */
    public function broadcastOn(): array
    {
        return [
            new Channel('productos'),
        ];
    }

    /**
     * Payload JSON que recibe el WebSocket cliente.
     */
    public function broadcastWith(): array
    {
        return [
            'product_id'  => $this->productId,
            'nuevo_stock' => $this->nuevoStock,
        ];
    }
}
```

---

## 3. Disparo del Evento en Servidor (`app/Services/CompraService.php`)
Disparar el evento dentro del flujo de la transacción inmediatamente después del decremento atómico:

```php
use App\Events\StockActualizado;

// ...dentro del ciclo de procesamiento de productos:
$nuevoStock = Product::where('id', $dto->id)->value('stock');

// Emitir evento por WebSockets
StockActualizado::dispatch($dto->id, $nuevoStock);
```

---

## 4. Suscripción en Frontend (Vue 3 / Laravel Echo)
Recepción de eventos en tiempo real para actualizar la interfaz y bloquear compras de productos agotados:

```javascript
import { onMounted, onUnmounted } from 'vue';

onMounted(() => {
    window.Echo.channel('productos')
        .listen('StockActualizado', (e) => {
            // Buscar producto en la lista reactiva
            const producto = products.value.find(p => p.id === e.product_id);

            if (producto) {
                producto.stock = e.nuevo_stock;

                // Deshabilitar UI si el stock se agota
                if (producto.stock <= 0) {
                    producto.disponible = false;
                }
            }
        });
});

onUnmounted(() => {
    // Desconectar canal al desmontar componente
    window.Echo.leaveChannel('productos');
});
```

---

## 5. Matriz de Protección Integrada

* **Capa Frontend (Reactiva):** Escucha constante vía WebSockets que actualiza el estado local y deshabilita botones `[Comprar]` al instante sin hacer *HTTP polling*.
* **Capa Backend (Atómica):** Garantía de integridad a nivel base de datos mediante `where('stock', '>=', $cantidad)->decrement(...)` con transacciones atómicas en MySQL.