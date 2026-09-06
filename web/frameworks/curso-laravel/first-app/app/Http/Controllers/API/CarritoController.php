<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
use App\Http\Requests\API\FinalizarCompraRequest;
use App\Services\CarritoService;
use App\Services\CompraService;

class CarritoController extends Controller
{
    // Inyección de dependencias con el servicio de compras
    public function __construct(
        private CompraService $compraService,
        private CarritoService $carritoService
        ) {}

    // Métodos de clase
    public function calcularTotal(CarritoControllerRequest $request) {
        $products = $request->getProductsDTO();
        $total = $this->carritoService->calculoTotal($products);

        return response()->json(['total' => $total]);
    }

    public function finalizarCompra(FinalizarCompraRequest $request) {
        // 1. Obtener los datos validados

        // 2. Llamar al servicio para crear la compra y el detalle de la compra
        $compra = $this->compraService->crearCompra($request);

        // 3. Integrar mercado pago

        // 4. Enviar mails

        // 5. Retornar la data
        return response()->json([
            'compra' => $compra->load('products')
        ]);
    }
}
