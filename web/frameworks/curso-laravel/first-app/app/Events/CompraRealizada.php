<?php

namespace App\Events;

use App\Models\Compra;
use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

// Se implementa la interfaz ShouldBroadcast para activar el método broadcastOn
class CompraRealizada implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    /**
     * Create a new event instance.
     */
    public function __construct(private Compra $compra) {}

    /**
     * Get the channels the event should broadcast on.
     *
     * @return array<int, Channel>
     */
    public function broadcastOn(): array
    {
        // Crear un array de canales
        $channels = [];

        foreach ($this->compra->products as $product) {
            // El nombre del canal varía según el id del producto
            $channels[] = new Channel("products.{$product->id}");
        }

        // Devolver los canales públicos
        return $channels;
    }

    public function getCompra(): Compra 
    {
        return $this->compra;
    }
}
