<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\Pivot;

#[Fillable(['compra_id', 'product_id', 'cantidad', 'precio'])]
class CompraProducto extends Model //Pivot
{
    public $incrementing = false;
}
