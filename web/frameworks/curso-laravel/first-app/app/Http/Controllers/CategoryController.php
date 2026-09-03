<?php

namespace App\Http\Controllers;

use App\Utilities\Common;
use Illuminate\Http\Request;

class CategoryController extends Controller
{
    private array $categories;

    public function __construct() {
        $this->categories = Common::getCategories();
    }

    public function index(Request $request) {
        // Manipular el objeto request para acceder a los params
        $to_find = $request->name;

        if(!is_null($to_find) && array_key_exists($to_find, $this->categories)) {
            echo "Existe <br>";
            return;
        }
        
        foreach ($this->categories as $category => $product) {
            echo "<a href='".route('products.show', $category)."'>{$category}</a> <br>";
        }
    }

    public function show(string $name) {
        return to_route('products.show', $name);
    }
}
