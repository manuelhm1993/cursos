<?php

namespace App\Services;

use Stripe\Stripe;
use Stripe\PaymentIntent;

class StripeService
{
    /**
     * Create a new class instance.
     */
    public function __construct()
    {
        // 1. Inicializa el SDK usando tu llave secreta
        Stripe::setApiKey(config('stripe.secret'));
    }

    public function crearIntencionDePago(float $total, int $compraId): PaymentIntent 
    {
        // throw new \Exception("Stripe no funciona");

        return PaymentIntent::create([
            // Multiplicamos por 100 y redondeamos para evitar pérdida de precisión en decimales
            'amount' => (int) round($total * 100), /* La banca prefiere cobros en centavos para evitar el punto flotante */
            'currency' => 'usd',
            'metadata' => [
                'compra_id' => $compraId,
            ],
        ]);
    }

    public function obtenerIntencionDePago(): void 
    {

    }
}
