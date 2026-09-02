<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

// Route::get('/user', function (Request $request) {
//     return $request->user();
// })->middleware('auth:sanctum');

// Devolver todos los productos en formato json
Route::get('products', function() {
    $categories = [
        "Fideos" => [
            "Moñitos",
            "Fideos largos",
            "Cabello de ángel",
        ],
        "Verduras" => [
            "Tomates",
            "Lechuga",
            "Cebolla",
        ],
    ];

    $products = [];

    // Si la categoría no fue enviada, se muestran todos los productos
    foreach ($categories as $key => $value) {
        foreach($value as $product) {
            $products[] = $product;
        }
    }

    return response()->json($products);
});

Route::get('categories', function() {
    echo "endpoint categories API";
});
