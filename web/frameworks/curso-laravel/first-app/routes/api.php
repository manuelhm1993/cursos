<?php

use App\Http\Controllers\API\CarritoController;
use App\Http\Controllers\API\ProductController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

// Route::get('/user', function (Request $request) {
//     return $request->user();
// })->middleware('auth:sanctum');

// Devolver todos los productos en formato json
Route::name('api')->apiResource('products', ProductController::class);

Route::prefix('carrito')->controller(CarritoController::class)->group(function () {
    Route::post('/calcular-total','calcularTotal');
    Route::post('/finalizar-compra', 'finalizarCompra');
});
