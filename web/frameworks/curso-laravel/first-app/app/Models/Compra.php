<?php

namespace App\Models;

use App\Observers\CompraObserver;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Attributes\ObservedBy;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

#[Fillable([
    'nombre', 'apellido', 'email', 'telefono', 
    'tipo_envio', 'direccion', 'codigo_postal', 'pais', 'estado', 'municipio', 
    'total', 'pagado'
])]
#[ObservedBy([CompraObserver::class])] // Se registra el observer de la compra
class Compra extends Model
{
    public function products(): BelongsToMany
    {
        return $this->belongsToMany(Product::class, 'compra_productos')
                ->withTimestamps()
                ->withPivot(['cantidad', 'precio']);
                    /*->using(CompraProducto::class);*/
    }
}
