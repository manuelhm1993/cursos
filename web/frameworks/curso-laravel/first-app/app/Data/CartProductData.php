<?php

namespace App\Data;

use App\Models\Product;
use Spatie\LaravelData\Data;

class CartProductData extends Data {
    public Product $product;

    public function __construct(
        public int $id,
        public int $cantidad
    ) {
        $this->product = Product::find($this->id);
    }
}