<?php

namespace App\Console\Commands;

use App\Models\Compra;
use Carbon\Carbon;
use Illuminate\Console\Attributes\Description;
use Illuminate\Console\Attributes\Signature;
use Illuminate\Console\Command;

#[Signature('mh:eliminar-compras')]
#[Description('Elimina las compras con más de 30 dias sin ser canceladas')]
class EliminarCompras extends Command
{
    /**
     * Execute the console command.
     */
    public function handle()
    {
        // $this->info('Mensaje');    // Letras verdes
        // $this->warn('Mensaje');    // Letras amarillas
        // $this->error('Mensaje');   // Letras rojas
        // $this->comment('Mensaje'); // Ídem watn
        // $this->line('Mensaje');    // Letras blancas

        // Obtener la fecha de hoy
        $fechaDeHoy = Carbon::now();

        // Obtener las compras no pagadas
        $compras = Compra::where('pagado', false)->get();
        $i = 0;

        foreach($compras as $compra) {
            // Parsear la fecha de la compra
            $fechaCompra = Carbon::parse($compra->created_at);

            // Obtener la fecha en dias
            $diferenciaDeDias = $fechaCompra->diffInDays($fechaDeHoy);

            // Si la compra tiene más de 31 dias sin pagarse, se elimina la compra
            if($diferenciaDeDias >= 31) {
                $compra->delete();
                $i++;
            }
        }

        $this->line('Operación exitosa. Compras eliminadas: ' . $i);
    }
}
