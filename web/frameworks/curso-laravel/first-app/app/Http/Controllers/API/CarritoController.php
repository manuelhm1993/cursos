<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Http\Requests\API\CarritoControllerRequest;
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
}
