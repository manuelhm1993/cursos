<?php

namespace App\Observers;

use App\Mail\CompraPagada;
use App\Models\compra;
use Illuminate\Support\Facades\Mail;

class CompraObserver
{
    /**
     * Handle the compra "created" event.
     */
    public function created(compra $compra): void
    {
        //
    }

    /**
     * Handle the compra "updated" event.
     */
    public function updated(compra $compra): void
    {
        // Solo se ejecuta si un atributo del modelo es actualizado
        if($compra->pagado) {
            // Mail::to($compra->email)->send(new CompraPagada($compra));
        }
    }

    /**
     * Handle the compra "deleted" event.
     */
    public function deleted(compra $compra): void
    {
        //
    }

    /**
     * Handle the compra "restored" event.
     */
    public function restored(compra $compra): void
    {
        //
    }

    /**
     * Handle the compra "force deleted" event.
     */
    public function forceDeleted(compra $compra): void
    {
        //
    }
}
