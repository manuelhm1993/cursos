<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
use App\Http\Requests\API\FinalizarCompraRequest;
use App\Services\CarritoService;
use App\Services\CompraService;
use App\Services\StripeService;

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
        // 1. Llamar al servicio para crear la compra y su tabla pivot
        $compra = $this->compraService->crearCompra($request);

        // 2. Calcular el total leyendo tu DTO ya procesado
        $total = $this->carritoService->calculoTotal($request->getProductsDTO());

        // 3. Integración con Stripe (Generar la Intención de Pago)
        $intencionPago = $this->stripeService->crearIntencionDePago($total, $compra->id);

        // 4. Enviar mails (Pendiente para futura iteración)

        // 5. Retornar la data + la llave secreta para que Vue 3 monte el formulario
        return response()->json([
            'compra'        => $compra->load('products'),
            'client_secret' => $intencionPago->client_secret
        ]);
    }
}
