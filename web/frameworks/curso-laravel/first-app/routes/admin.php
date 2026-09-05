<?php

use App\Http\Controllers\Admin\CategoryController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Admin\ProductController;
use Illuminate\Support\Facades\Route;

// ----------------- Rutas únicas ----------------- //
Route::get('/', [DashboardController::class, 'index'])->name('dashboard');

// ----------------- Rutas de recursos ----------------- //
Route::resource('categories', CategoryController::class)->except([
    'show'
]);

Route::resource('products', ProductController::class)->except([
    'show'
]);