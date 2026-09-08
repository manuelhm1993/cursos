<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Mail\CompraPagada;
use App\Models\Compra;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class CompraController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $compras = Compra::all();

        return view('admin.compras.index', compact('compras'));
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Compra $compra)
    {
        return view('admin.compras.edit', compact('compra'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Compra $compra)
    {
        $validated = $request->validate([
            'pagado' => 'required|bool'
        ]);

        $compra->update($validated);

        if($compra->pagado) {
            Mail::to($compra->email)->send(new CompraPagada($compra));
        }

        return to_route('admin.compras.index')->with([
            'success' => 'Compra actualizada exitosamente'
        ]);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Compra $compra)
    {
        $compra->delete();

        return to_route('admin.compras.index')->with([
            'success' => 'Compra eliminada exitosamente'
        ]);
    }
}
