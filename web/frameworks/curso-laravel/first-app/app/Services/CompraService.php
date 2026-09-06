<?php

namespace App\Services;

use App\Http\Requests\API\FinalizarCompraRequest;
use App\Models\Compra;

class CompraService
{
    /**
     * @param FinalizarCompraRequest $request
     * @return Compra $compra
     */
    public function crearCompra(FinalizarCompraRequest $request): Compra
    {
        // Obtener los datos validados
        $validated = $request->validated();

        // Extraer el array de productos
        $productsDTO = $request->getProductsDTO();

        // Borrar el array de productos de los datos validados
        // unset($validated['products']);

        // 1. Guardar la compra (tabla compras)
        $compra = Compra::create($validated);

        // 2. Ensamblar los datos para la tabla pivot usando el DTO
        $pivotData = [];
        foreach($productsDTO as $dto) {
            $pivotData[$dto->id] = [
                'cantidad' => $dto->cantidad,
                'precio'   => $dto->product->precio, 
            ];
        }

        // 3. Inserción en la tabla intermedia (compra_productos)
        $compra->products()->attach($pivotData);

        return $compra;
    }
}
