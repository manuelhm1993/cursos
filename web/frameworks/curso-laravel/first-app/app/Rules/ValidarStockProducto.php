<?php

namespace App\Rules;

use App\Models\Product;
use Closure;
use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Translation\PotentiallyTranslatedString;

class ValidarStockProducto implements ValidationRule
{
    /**
     * Run the validation rule.
     *
     * @param  Closure(string, ?string=): PotentiallyTranslatedString  $fail
     */
    public function validate(string $attribute, mixed $value, Closure $fail): void
    {
        // Extraer el índice del objeto producto para buscarlo en db
        $index = explode('.', $attribute)[1];
        // $index = str($attribute)->split('/\./')[1];

        // Obtener el id del producto dentro del array
        $productID = request()->input("products.{$index}.id");

        // Buscar el producto en db
        $product = Product::find($productID);

        // La cantidad sea menor al stock del producto que se estamos validando
        if($product->stock < $value) {
            $fail("No hay suficiente stock en el inventario del producto {$product->nombre} para completar esta solicitud. Máximo {$product->stock} unidades");
        }
    }
}
