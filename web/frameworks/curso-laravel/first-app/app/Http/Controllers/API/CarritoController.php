<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
use App\Http\Requests\API\FinalizarCompraRequest;
use App\Models\Compra;
use App\Models\CompraProducto;
use App\Models\Product;

class CarritoController extends Controller
{
    private function calculoTotal(array $productsDTO) {
        $total = 0;

        foreach($productsDTO as $dto) {
            $total += ($dto->product->precio * $dto->cantidad);
        }

        return $total;
    }

    public function calcularTotal(CarritoControllerRequest $request) {
        return response()->json(['total' => $this->calculoTotal($request->getProductsDTO())]);
    }

    public function finalizarCompra(FinalizarCompraRequest $request) {
        // Obtener los datos validados
        $validated = $request->validated();

        // Extraer el array de productos
        $productsDTO = $request->getProductsDTO();
        
        // Borrar el array de productos de los datos validados
        // unset($validated['products']);

        // Guardar la compra
        $compra = Compra::create($validated);

        $data = [];

        foreach($productsDTO as $dto) {
            $data[] = CompraProducto::create([
                'compra_id'  => $compra->id,
                'product_id' => $dto->id,
                'cantidad'   => $dto->cantidad,
                'precio'     => $dto->product->precio,
            ]);
        }

        return response()->json(['data' => $data]);
    }
}
