<?php

namespace App\Exceptions;

use Exception;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Throwable;
use Override;

class StripeException extends Exception
{
    // Override no se debe implementar en un constructor
    public function __construct(
        string $message = "Error en Stripe", 
        int $code = Response::HTTP_CONFLICT, 
        Throwable|null $previous = null
    )
    {
        // El constructor no devuelve nada
        parent::__construct($message, $code, $previous);
    }

    // Este método formatea la respuesta
    public function render(Request $request) {
        if($request->isJson()) {
            return response()->json([
                'message' => $this->message,
            ], $this->code);
        }
    }
}
