<?php

namespace App\Utilities\Traits;

use App\Utilities\Data\CartProductData;

trait HasCartProductsDTO 
{
    private array $productsDTO = [];

    public function passedValidation(): void
    {
        if ($this->has('products')) {
            foreach($this->products as $product) {
                $this->productsDTO[] = CartProductData::from([
                    'id'       => $product['id'],
                    'cantidad' => $product['cantidad'],
                ]);
            }
        }
    }

    public function getProductsDTO(): array {
        return $this->productsDTO;
    }
}