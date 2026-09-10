<?php

namespace App\Services;

use App\Http\Requests\API\FinalizarCompraRequest;
use App\Mail\CompraRealizada;
use App\Models\Compra;
use App\Models\Product;
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

        // 3. Ensamblar datos pivot
        $pivotData = [];
        foreach($productsDTO as $dto) {
            $pivotData[$dto->id] = [
                'cantidad' => $dto->cantidad,
                'precio'   => $dto->product->precio, 
            ];

            // 4. Restar el stock de forma atómica (Sin cargar los modelos a memoria)
            $filasAfectadas = Product::where('id', $dto->id)
                ->where('stock', '>=', $dto->cantidad) // Valida que el stock no sea negativo
                ->decrement('stock', $dto->cantidad);

            if ($filasAfectadas === 0) {
                throw new \Exception("Stock insuficiente para el producto {$dto->id}");
            }
        }

        // 5. Inserción masiva en la tabla intermedia (compra_productos)
        $compra->products()->attach($pivotData);

        return $compra;
    }

    public function calcularTotal(Compra $compra): float 
    {
        $total = $compra->products->reduce(function(int $carry, Product $product) {
            return $carry + ($product->pivot->precio * $product->pivot->cantidad);
        }, 0);

        return $total;
    }

    public function eviarMail(Compra $compra): void
    {
        Mail::to($compra->email)->send(new CompraRealizada($compra));
    }
}
