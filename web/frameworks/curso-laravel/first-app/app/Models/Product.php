<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

#[Fillable(['nombre', 'precio', 'stock', 'imagen', 'category_id'])]
class Product extends Model
{
    use HasFactory;

    public function category(): BelongsTo
    {
        // Para devolver las categorías borradas se usa withTrashed
        return $this->belongsTo(Category::class)->withTrashed();
    }

    public function compras(): BelongsToMany
    {
        return $this->belongsToMany(Compra::class, 'compra_productos')
                ->withTimestamps()
                ->withPivot(['cantidad', 'precio']);
                    /*->using(CompraProducto::class); */
    }
}
