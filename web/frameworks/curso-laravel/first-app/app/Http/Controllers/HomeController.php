<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Session;

use function Laravel\Prompts\select;

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

        // Traer todas las categorías con sus productos asociados, seleccionando columnas necesarias
        $categories = Category::select([
                                'id', 'nombre'
                            ])
                            // Para que el enlace se haga se debe tener clave de uno que pasa a muchos
                            ->with('products:id,category_id,nombre')
                            ->get();

        return view('home', compact('categories'));
    }
}
