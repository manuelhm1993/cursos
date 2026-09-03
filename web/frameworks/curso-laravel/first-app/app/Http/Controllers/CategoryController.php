<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;

class CategoryController extends Controller
{
    public function index() {
        $categories = Category::orderBy('nombre', 'asc')->get();

        return view('categories.index', compact('categories'));
    }

    public function show(string $nombre) {
        $categories = Category::where('nombre', 'like', "%{$nombre}%")->get();

        return view('categories.index', compact('categories'));
    }

    public function create(string $nombre) {
        $category = Category::create([
            'nombre' => $nombre
        ]);

        return $category;
    }

    public function categoryProducts(Request $request) {
        return to_route('products.show', $request->nombre);
    }
}
