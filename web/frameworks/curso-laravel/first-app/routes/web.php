<?php

use App\Http\Controllers\Admin\LoginController;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\CategoryController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\ProductController;

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