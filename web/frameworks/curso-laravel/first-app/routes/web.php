<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

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

// HOME
Route::get('/', function () use ($categories) {
    $products   = array_merge(...array_values($categories));
    $categories = array_keys($categories);

    return view('home', compact('categories', 'products'));
});

// CATEGORÍAS
Route::prefix('categories')->name('categories.')->group(function() use ($categories) {
    // Inyectar el objeto Request
    Route::get('/', function (Request $request) use ($categories) {
        // Manipular el objeto request para acceder a los params
        $to_find = $request->name;

        if(!is_null($to_find) && array_key_exists($to_find, $categories)) {
            echo "Existe <br>";
            return;
        }
        
        foreach ($categories as $category => $product) {
            echo "{$category} <br>";
        }
    })->name('index');

    Route::get('oferta', function() {
        return 'Oferta';
    })->name('oferta');

    Route::get('mas-vendidas', function() {
        return 'Más vendida';
    })->name('mas-vendidas');

    Route::get('/{name}', function(string $name) {
        return "Productos de $name";
    })->name('show');
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
