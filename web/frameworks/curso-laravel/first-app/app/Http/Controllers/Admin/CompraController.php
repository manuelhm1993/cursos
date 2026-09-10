<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Compra;
use Carbon\Carbon;
use Illuminate\Http\Request;

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

    /**
     * Métodos fuera de los CRUDs
     */
    public function eliminarCompras()
    {
        // Obtener la fecha de hoy
        $fechaDeHoy = Carbon::now();

        // Obtener las compras no pagadas
        $compras = Compra::where('pagado', false)->get();

        $data = [];

        foreach($compras as $compra) {
            // Parsear la fecha de la compra
            $fechaCompra = Carbon::parse($compra->created_at);

            // Obtener la fecha en dias
            $diferenciaDeDias = $fechaCompra->diffInDays($fechaDeHoy);

            // Si la compra tiene más de 31 dias sin pagarse, se elimina la compra
            if($diferenciaDeDias >= 31) {
                $data[] = $compra;

                $compra->delete();
            }
        }

        return response()->json(['data' => $data]);
    }
}
