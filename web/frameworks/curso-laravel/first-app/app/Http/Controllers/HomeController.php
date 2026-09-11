<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Session;

class HomeController extends Controller
{
    public function index() {
        // Guardar un dato de sesión o hacer put de usuario
        // session(['usuario' => 'Manuel']);
        // Session::put('usuario', 'Manuel');

        // Obtener el valor de una variable de sesión
        // $usuario = session('usuario', 'usuario');
        // $usuario = Session::get('usuario', 'usuario');

        // dd($usuario);

        $categories = Category::all();

        return view('home', compact('categories'));
    }
}
