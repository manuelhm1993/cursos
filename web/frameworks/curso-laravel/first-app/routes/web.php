<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\CategoryController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\ProductController;

// HOME - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::get('/', [HomeController::class, 'index']);

// CATEGORÍAS - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::prefix('categories')->name('categories.')->controller(CategoryController::class)->group(function() {
    Route::get('/', 'index')->name('index');
    Route::get('/{name}', 'show')->name('show');
});

// PRODUCTOS - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::prefix('products')->name('products.')->controller(ProductController::class)->group(function() {
    Route::get('/{category?}', 'show')->name('show');
});
