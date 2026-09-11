<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    public function index(Request $request, ?string $category = null) {
        // 1. Obtención de productos segun la categoría
        if (is_null($category)) {
            $products = Product::with('category')->paginate(12);
        } 
        else {
            $categoryModel = Category::where('nombre', $category)->first();

            if (!$categoryModel) {
                return response()->json(['message' => 'Categoría no encontrada'], 404);
            }

            // Paginación sobre la relación cargando la categoría para evitar N+1
            $products = $categoryModel->products()->with('category')->paginate(12);
        }

        // 2. Si la petición viene por AJAX, retoma únicamente la partial con el HTML
        if ($request->ajax()) {
            return view('includes.products', compact('products'))->render();
        }

        // 3. Carga normal sincrónica
        return view('products.index', compact('products'));
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
