<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

use App\Models\Compra;
use App\Mail\CompraRealizada;
use Illuminate\Support\Facades\Mail;

class EnviarMailDeCompra implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct(private Compra $compra) {}

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        Mail::to($this->compra->email)->send(new CompraRealizada($this->compra));
    }
}
