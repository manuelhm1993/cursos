<?php

namespace App\Providers;

// use App\Events\CompraRealizada;
// use App\Listeners\CalcularTotalCompra;
// use Illuminate\Support\Facades\Event;

// use App\Models\Compra;
// use App\Observers\CompraObserver;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        //
        // Se puede registrar manualmente el evento y los oyentes, pero laravel 13 tiene autodiscover
        // Event::listen(
        //     CompraRealizada::class,
        //     CalcularTotalCompra::class,
        // );

        // Se puede registrar manualmente el observer de una clase, pero el atributo ObserverBy es el nuevo estándar
        // Compra::observe(CompraObserver::class);
    }
}
