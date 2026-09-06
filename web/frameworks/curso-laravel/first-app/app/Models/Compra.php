<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

#[Fillable([
    'nombre', 'apellido', 'email', 'telefono', 
    'tipo_envio', 'direccion', 'codigo_postal', 'pais', 'estado', 'municipio', 
    'total',
])]
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
