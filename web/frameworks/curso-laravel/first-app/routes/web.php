<?php

use Illuminate\Support\Facades\Route;

// HOME
Route::get('/', function () {
    return view('welcome');
});

Route::prefix('categories')->name('categories.')->group(function() {
    Route::get('/', function () {
        $categories = [
            'Fideos',
            'Tomates',
            'Arroz'
        ];

        foreach ($categories as $category) {
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

Route::get('products/{category?}', function(?string $category = null) {
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

    // Si la categoría no fue enviada, se muestran todos los productos
    if (is_null($category)) {
        foreach ($categories as $key => $value) {
            echo "Categoría $key <br>";
            foreach($value as $product) {
                echo "Producto: $product <br>";
            }
        }
        return;
    }

    // Si la categoría existe se muestran sus productos
    if (array_key_exists($category, $categories)) {
        foreach ($categories[$category] as $product) {
            echo "Producto: $product <br>";
        }
        return;
    }

    echo "Categoría no encontrada";
});