<?php

namespace App\Http\Controllers;

use App\Utilities\Common;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    private array $categories;

    public function __construct() {
        $this->categories = Common::getCategories();
    }

    public function show(?string $category = null) {
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

            $products = array_merge(...array_values($this->categories));

            return view('products.index', compact('products'));
        }

        // Si la categoría existe se muestran sus productos
        if (array_key_exists($category, $this->categories)) {
            $products = $this->categories[$category];

            return view('products.index', compact('products'));
        }

        echo "Categoría no encontrada";
    }
}
