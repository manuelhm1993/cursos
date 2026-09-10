<?php

use App\Http\Controllers\Admin\CategoryController;
use App\Http\Controllers\Admin\CompraController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Admin\ProductController;
use Illuminate\Support\Facades\Route;

// ----------------- Rutas únicas ----------------- //
Route::get('/', [DashboardController::class, 'index'])->name('dashboard');

Route::get('/compras/eliminar-compras', [CompraController::class, 'eliminarCompras'])->name('compras.eliminar-compras');

// ----------------- Rutas de recursos ----------------- //
Route::resource('categories', CategoryController::class)->except([
    'show'
]);

Route::resource('products', ProductController::class)->except([
    'show'
]);

Route::resource('compras', CompraController::class)->except([
    'show', 'create', 'store'
]);