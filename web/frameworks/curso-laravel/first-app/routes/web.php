<?php

use App\Http\Controllers\Admin\LoginController;
use App\Http\Controllers\CarritoController;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\CategoryController;
use App\Http\Controllers\CompraController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\ProductController;
use Illuminate\Support\Facades\URL;

// HOME - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::get('/', [HomeController::class, 'index']);

// CATEGORÍAS - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::prefix('categories')->name('categories.')->controller(CategoryController::class)->group(function() {
    Route::get('/', 'index')->name('index');
    Route::get('/category-products', 'categoryProducts')->name('category-products');
    Route::get('/create/{name}', 'create')->name('create');
    Route::get('/{name}', 'show')->name('show');
});

// PRODUCTOS - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::prefix('products')->name('products.')->controller(ProductController::class)->group(function() {
    Route::get('/{category?}', 'index')->name('index');
    Route::get('/show/{product}', 'show')->name('show');
    Route::get('/create/{category_id}/{name}/', 'create')->name('create');
});

// LOGIN
Route::prefix('login')->name('login.')->controller(LoginController::class)->group(function() {
    Route::get('/', 'index')->name('index');
    Route::get('/out', 'out')->name('out');
    Route::post('/', 'in')->name('in');
});

// COMPRA Y CARRITO
Route::get('/carrito', CarritoController::class)->name('carrito.index');
Route::get('/compras/cancelar-compra/{compra}', [CompraController::class, 'cancelarCompra'])->name('compra.cancelar-compra');

// URL CON HASH O FIRMA
Route::get('signature', function() {
    // Permite encriptar la url para evitar ataques de usuarios maliciosos
    $url = URL::signedRoute('compra.cancelar-compra', ['compra' => 34]);

    dd($url);
});