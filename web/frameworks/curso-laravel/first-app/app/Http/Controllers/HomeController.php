<?php

namespace App\Http\Controllers;

use App\Utilities\Common;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    private array $categories;

    public function __construct()
    {
        $this->categories = Common::getCategories();
    }

    public function index() {
        $products   = array_merge(...array_values($this->categories));
        $categories = array_keys($this->categories);

        return view('home', compact('categories', 'products'));
    }
}
