<?php

namespace App\Listeners;

use App\Events\CompraRealizada;
use App\Services\CompraService;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Queue\InteractsWithQueue;

class CalcularTotalCompra
{
    /**
     * Create the event listener.
     */
    public function __construct(private CompraService $compraService) {}

    /**
     * Handle the event.
     */
    public function handle(CompraRealizada $event): void
    {
        // Calcular el total de la compra
        $event->compra->update(['total' => $this->compraService->calcularTotal($event->compra)]);
    }
}
