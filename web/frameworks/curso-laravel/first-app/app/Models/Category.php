<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\SoftDeletes;

#[Fillable(['nombre'])]
class Category extends Model
{
    use SoftDeletes; // Permite el borrado lógico de sus productos derivados

    public function products(): HasMany
    {
        return $this->hasMany(Product::class);
    }
}
