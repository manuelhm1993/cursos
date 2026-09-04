<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Http\Requests\LoginRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function index() {
        return view('admin.login.index');
    }

    public function in(LoginRequest $request) {
        $login = Auth::attempt([
            'email'    => $request->email,
            'password' => $request->password
        ]);

        return ($login) ? to_route('admin.dashboard') : to_route('login.index');
    }

    public function out() {
        Auth::logout();
        
        return redirect('/');
    }
}
