<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function index() {
        return view('admin.login.index');
    }

    public function in(Request $request) {
        $login = Auth::attempt([
            'email'    => $request->email,
            'password' => $request->password
        ]);

        $route = ($login) ? 'admin.dashboard' : 'login.index';

        return to_route($route);
    }

    public function out(Request $request) {
        Auth::logout();
        
        return redirect('/');
    }
}
