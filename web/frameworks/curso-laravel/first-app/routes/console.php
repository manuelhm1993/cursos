<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\Schedule;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');

// Elimina mensualmente las compras que tengan más de 30 días
Schedule::command('mh:eliminar-compra')->daily();

// Ejecuta los procesos de la cosa emails cada 5 segundos
// Schedule::command('queue:work -v --queue=emails')->everyFiveSeconds();