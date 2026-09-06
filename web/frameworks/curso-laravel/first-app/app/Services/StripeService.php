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
        return PaymentIntent::create([
            // 2. Stripe exige el monto estrictamente en la unidad más pequeña (centavos)
            'amount' => intval($total * 100),
            'currency' => 'usd',
            // 3. Metadata crucial para rastrear la orden cuando llegue el Webhook asíncrono
            'metadata' => [
                'compra_id' => $compraId,
            ],
        ]);
    }
}
