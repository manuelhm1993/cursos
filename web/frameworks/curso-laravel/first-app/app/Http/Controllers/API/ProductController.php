<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // Devolver 10 productos por página de forma ascendente
        $products = Product::orderBy('precio', 'asc')
                        ->select('id', 'nombre', 'stock', 'precio')
                        ->paginate(10);

        return response()->json($products);

        $products = Product::orderBy('precio', 'asc')
                        ->paginate(10);

        // Uso de colecciones y el método map
        $data = $products->map(function (Product $product) {
            return [
                'id'         => $product->id,
                'nombre'     => $product->nombre,
                'stock'      => $product->stock,
                'precio'     => $product->precio,
            ];
        });

        // Uso de arrays y bucles
        $data = [];

        foreach($products as $product) {
            $data[] = [
                'id'         => $product->id,
                'nombre'     => $product->nombre,
                'stock'      => $product->stock,
                'precio'     => $product->precio,
            ];
        }

        return response()->json($data);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Product $product)
    {
        return response()->json([
                'id'         => $product->id,
                'nombre'     => $product->nombre,
                'stock'      => $product->stock,
                'precio'     => $product->precio,
            ]);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Product $product)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Product $product)
    {
        //
    }
}
