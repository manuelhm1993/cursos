<?php

namespace App\Http\Controllers\API;

// Clases laravel
use Illuminate\Http\Request;

// Facades laravel
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\DB;

// Controladores
use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
use App\Http\Requests\API\FinalizarCompraRequest;

// Servicios
use App\Services\CarritoService;
use App\Services\CompraService;
use App\Services\StripeService;

// Eventos y Jobs
use App\Events\CompraRealizada;
use App\Jobs\EnviarMailDeCompra;

class CarritoController extends Controller
{
    // Inyección de dependencias con el servicio de compras
    public function __construct(
        private CompraService $compraService,
        private CarritoService $carritoService,
        private StripeService $stripeService
        ) {}

    // Métodos de clase
    public function calcularTotal(CarritoControllerRequest $request) {
        $products = $request->getProductsDTO();
        $total = $this->carritoService->calculoTotal($products);

        return response()->json(['total' => $total]);
    }

    public function finalizarCompra(Request $request) {
        // 1. Clave única por usuario/email para no bloquear a otros clientes
        $lockKey = 'finalizar_compra_' . $request->input('email');

        // 2. Definimos TTL de 10s (segundo parámetro) y tiempo máximo de espera de 5s en block()
        $data = Cache::lock($lockKey, 10)->block(5, function () use ($request) {
            // Se hace la validación dentro del lock para impedir que el stock se procese en paralelo
            $request = app(FinalizarCompraRequest::class);

            // Forma 1: Proteger las operaciones de db con transacciones si son un bloque use(), rollback y commit se hacen automáticamente
            $data = DB::transaction(function() use($request) {
                // Dormir el hilo de ejecución 5 segundos
                // sleep(5);

                // 1. Llamar al servicio para crear la compra y su tabla pivot
                $compra = $this->compraService->crearCompra($request);

                // 2. Cargar los productos en la compra
                $dataCompra = $compra->load('products');

                // 3. Disparar el evento para calcular el total
                CompraRealizada::dispatch($dataCompra);

                // 4. Crear la intención de pago
                $intencionPago = $this->stripeService->crearIntencionDePago($compra->total, $compra->id);

                return [
                    'compra'        => $dataCompra,
                    'client_secret' => $intencionPago->client_secret
                ];
            });

            return $data;
        });

        // Forma 2: fomra manual: DB::beginTransaction();

        // 5. Enviar el mail de notificación (Al implementar redis se usa un job para delegar a colas)
        EnviarMailDeCompra::dispatch($data['compra'])->onQueue('emails');

        // 6. Retornar la data + la llave secreta para que Vue 3 monte el formulario
        return response()->json($data);
    }
}
