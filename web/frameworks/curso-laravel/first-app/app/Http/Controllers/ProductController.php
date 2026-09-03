<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    public function index(?string $category = null) {
        // Si la categoría no fue enviada, se muestran todos los productos
        if (is_null($category)) {
            $products = Product::all();

            return view('products.index', compact('products'));
        }

        $category = Category::where('nombre', $category)->first();
        
        // Si la categoría existe se muestran sus productos
        if (!is_null($category)) {
            // Obtener los productos que pertenecen a la categoría
            $products = $category->products;

            return view('products.index', compact('products'));
        }

        echo "Categoría no encontrada <br>";
        echo "<a href='".url("/")."'>Volver a Home</a>";
    }

    public function create(int $category_id, string $nombre) {
        $category = Category::find($category_id);

        $product = $category->products()->create([
            'nombre' => $nombre,
        ]);

        return $product;
    }

    // Model binding
    public function show(Product $product) {
        return view('products.show', compact('product'));
    }
}
