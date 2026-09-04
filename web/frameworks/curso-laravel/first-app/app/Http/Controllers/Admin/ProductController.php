<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Category;
use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $products = Product::all();

        return view('admin.products.index', compact('products'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        $categories = Category::select('id', 'nombre')->get();

        return view('admin.products.create', compact('categories'));
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'category_id' => 'required|integer|exists:categories,id',
            'nombre'      => 'required',
            'stock'       => 'required|integer',
            'precio'      => 'required|numeric',
        ]);

        Product::create($validated);

        return to_route('admin.products.index')->with([
            'success' => 'Producto creado exitosamente'
        ]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Product $product)
    {
        $categories = Category::select('id', 'nombre')->get();

        return view('admin.products.edit', compact('categories', 'product'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Product $product)
    {
        $validated = $request->validate([
            'category_id' => 'required|integer|exists:categories,id',
            'nombre'      => 'required',
            'stock'       => 'required|integer',
            'precio'      => 'required|numeric',
        ]);

        $product->update($validated);

        return to_route('admin.products.index')->with([
            'success' => 'Producto actualizado exitosamente'
        ]);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Product $product)
    {
        $product->delete();
        
        return to_route('admin.products.index')->with([
            'success' => 'Producto eliminado exitosamente'
        ]);
    }
}
