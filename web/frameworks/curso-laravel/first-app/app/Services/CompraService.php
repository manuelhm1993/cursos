<?php

namespace App\Services;

use App\Http\Requests\API\FinalizarCompraRequest;
use App\Mail\CompraRealizada;
use App\Models\Compra;
use Illuminate\Support\Facades\Mail;

class CompraService
{
    /**
     * @param FinalizarCompraRequest $request
     * @return Compra $compra
     */
    public function crearCompra(FinalizarCompraRequest $request): Compra
    {
        // 1. Obtener los datos validados, extraer los productos y borrarlos del array
        $validated = $request->validated();
        $productsDTO = $request->getProductsDTO();
        unset($validated['products']);

        // 2. Guardar la compra (tabla compras)
        $compra = Compra::create($validated);

        // 3. Ensamblar datos pivot y calcular el total simultáneamente (O(n) en RAM)
        $pivotData = [];
        $total = 0;
        foreach($productsDTO as $dto) {
            $pivotData[$dto->id] = [
                'cantidad' => $dto->cantidad,
                'precio'   => $dto->product->precio, 
            ];

            $total += ($dto->cantidad * $dto->product->precio);
        }

        // 4. Inserción masiva en la tabla intermedia (compra_productos)
        $compra->products()->attach($pivotData);

        // 5. Persistir el total calculado en el modelo padre
        $compra->update(['total' => $total]);

        return $compra;
    }

    public function eviarMail(Compra $compra): void
    {
        Mail::to($compra->email)->send(new CompraRealizada($compra));
    }
}
