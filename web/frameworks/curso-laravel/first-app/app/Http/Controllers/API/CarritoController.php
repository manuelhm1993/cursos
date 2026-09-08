<?php

namespace App\Http\Controllers\API;

use App\Events\CompraRealizada;
use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
use App\Http\Requests\API\FinalizarCompraRequest;
use App\Services\CarritoService;
use App\Services\CompraService;
use App\Services\StripeService;
use Illuminate\Support\Facades\DB;

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

    public function finalizarCompra(FinalizarCompraRequest $request) {
        // Proteger las operaciones de db con transacciones si son un bloque use(), rollback y commit se hacen automáticamente
        $data = DB::transaction(function() use($request) {
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

        // 5. Enviar el mail de notificación
        // $this->compraService->eviarMail($dataCompra);

        // 6. Retornar la data + la llave secreta para que Vue 3 monte el formulario
        return response()->json($data);
    }
}
