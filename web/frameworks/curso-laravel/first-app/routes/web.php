<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\CategoryController;
use App\Http\Controllers\HomeController;
use App\Utilities\Common;

$categories = Common::getCategories();

// HOME - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::get('/', [HomeController::class, 'index']);

// CATEGORÍAS - USO DE CONTROLADOR PARA DELEGAR LA LÓGICA DEL NEGOCIO
Route::prefix('categories')->name('categories.')->controller(CategoryController::class)->group(function() {
    Route::get('/', 'index')->name('index');
    Route::get('/{name}', 'show')->name('show');
});

// PRODUCTOS
Route::prefix('products')->name('products.')->group(function () use ($categories) {
    Route::get('/{category?}', function(?string $category = null) use ($categories) {
        // Si la categoría no fue enviada, se muestran todos los productos
        if (is_null($category)) {
            /*$products = [];
            foreach ($categories as $key => $value) {
                foreach($value as $product) {
                    $products[] = $product;
                }
            }*/

            /*$products = [];
            foreach ($categories as $value) {
                $products = array_merge($products, $value);
            }*/

            /*$products = array_reduce($categories, function($carry, $item) {
                return array_merge($carry, $item);
            }, []);*/

            $products = array_merge(...array_values($categories));

            return view('products.index', compact('products'));
        }

        // Si la categoría existe se muestran sus productos
        if (array_key_exists($category, $categories)) {
            $products = $categories[$category];

            return view('products.index', compact('products'));
        }

        echo "Categoría no encontrada";
    })->name('show');
});
