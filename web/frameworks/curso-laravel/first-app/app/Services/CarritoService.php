<?php

namespace App\Services;

class CarritoService
{
    /**
     * @param array $productsDTO
     * @return float
     */
    public function calculoTotal(array $productsDTO): float {
        $total = 0;

        foreach($productsDTO as $dto) {
            $total += ($dto->product->precio * $dto->cantidad);
        }

        return $total;
    }
}
