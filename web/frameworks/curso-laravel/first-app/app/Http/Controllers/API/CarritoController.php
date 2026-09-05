<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Product;
use Illuminate\Http\Request;

class CarritoController extends Controller
{
    private function calculoTotal(array $validatedProducts) {
        $total = 0;

        foreach($validatedProducts['products'] as $vp) {

            $product = Product::find($vp['id']);

            $total += ($product->precio * $vp['cantidad']);
        }

        return $total;
    }

    public function calcularTotal(Request $request) {
        $validatedProducts = $request->validate([
            'products'            => 'required|array',
            'products.*.id'       => 'required|integer|exists:products,id',
            'products.*.cantidad' => 'required|integer',
        ]);

        return response()->json(['total' => $this->calculoTotal($validatedProducts)]);
    }
}
